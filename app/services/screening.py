from typing import List,Tuple
from app.services.nlp.extract_skills import parse_cv as nlp_extract
from app.services.llm.extract_skills_llm import parse_cv as llm_extract
from app.services.nlp.embeddings import get_embedding
from app.services.get_data import read_data
from app.services.llm.llm_ranking import get_llm_response
#from app.services.vector_store import VectorStore ,'not required'
from app.model.schemas import CandidateResult, ScreeningRequest
from app.core.logger import logger

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Screener:
    #def __init__(self, vector_store: VectorStore):
        #self.vector_stores = vector_store

    def screen_candidates(self, request: ScreeningRequest) -> Tuple[List[CandidateResult],str]:
        """
        Orchestrates the full screening pipeline:
        - Parse CVs (NLP or LLM)
        - Extract skills
        - Generate embeddings
        - Compare with JD
        - Compute final scores
        """
        logger.info("Starting candidate screening...")

        # --- Step 1: Extract JD skills + embedding ---
        parsed_JD = self._extract_skills(request.message, request.parser, request.api_key, request.llm)
        jd_embedding = get_embedding(request.message)

        # --- Step 1: Data Collection  ---
        cv_carpus=read_data(cv)

        results = []

        # --- Step 2: Process each CV ---
        for filename, cv in cv_carpus.values:
            parsed_cv = self._extract_skills(cv, request.parser, request.api_key, request.llm)
            cv_embedding = get_embedding(cv)

            # --- Step 3: Compute scores ---
            skill_score = self._compute_skill_overlap(parsed_cv.skills, parsed_JD.skills)
            semantic_score = self._compute_semantic_similarity(cv_embedding, jd_embedding)
            experience_score = self._compute_experience_score(parsed_cv.expirence, parsed_JD.expirence)

            final_score = (
                0.4 * skill_score +
                0.4 * semantic_score +
                0.2 * experience_score
            )

            results.append(CandidateResult(
                candidate_id=filename,
                skills=parsed_cv.skills,
                skill_score=skill_score,
                semantic_score=semantic_score,
                experience_score=experience_score,
                final_score=final_score
            ))

            # Store embeddings for future queries
            #self.vector_store.add(cv.id, cv_embedding)

        # --- Step 4: Rank candidates ---
        results.sort(key=lambda r: r.final_score, reverse=True)
        logger.info("Screening complete. Returning results.")

        # --- Step 6: use llm
        llm_response="No API KEY is available so, LLM’s reasoning is not done!"
        if request.api_key:
            llm_response=get_llm_response(results[:10],request.api_key,parsed_JD,True)
        return results, llm_response

    def _extract_skills(self, text: str, parser: bool, api_key: str, model: str) -> List[str]:
        if parser=="llm":
            return llm_extract(text, api_key=api_key, model=model)
        return list(nlp_extract(text))

    def _compute_skill_overlap(self, cv_skills: List[str], jd_skills: List[str]) -> float:
        if not jd_skills:
            return 0.0
        overlap = set(cv_skills).intersection(set(jd_skills))
        return len(overlap) / len(jd_skills)

    def _compute_semantic_similarity(self, cv_emb: List[float], jd_emb: List[float]) -> float:
        cv_arr = np.array(cv_emb).reshape(1, -1)
        jd_arr = np.array(jd_emb).reshape(1, -1)
        return float(cosine_similarity(cv_arr, jd_arr)[0][0])

    def _compute_experience_score(self, cv_years: int, jd_required: int) -> float:
        if jd_required == 0:
            return 1.0
        return min(cv_years / jd_required, 1.0)

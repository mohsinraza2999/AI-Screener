from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form, File,UploadFile

class CVRequest(BaseModel):
    text: str

class JobRequest(BaseModel):
    text: str

class SkillResponse(BaseModel):
    skills: List[str]

class LLMRequest(BaseModel):
    text: str
    api_key: str
    model: str

# ---------- Request Models ----------

class CVInput(BaseModel):
    id: str
    text: str
    experience_years: Optional[int] = 0


class ScreeningRequest(BaseModel):
    api_key: str 
    llm: str 
    parser: str 
    message: str 
    cv: List[UploadFile] 
    
    
    
     


# ---------- Response Models ----------

class CandidateResult(BaseModel):
    candidate_id: str
    skills: List[str]
    skill_score: float
    semantic_score: float
    experience_score: float
    final_score: float


class ScreeningResponse(BaseModel):
    results: List[CandidateResult]

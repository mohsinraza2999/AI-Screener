from langchain_openai import ChatOpenAI
import app.services.llm.llm_ranking as llm_ranking
from app.core.logger import get_logger
from langchain.chains import ConversationChain
from app.services.llm.prompt_templates import get_parsing_prompt
from typing import Optional
logger = get_logger(__name__)



def parse_cv(cv_text: str, api_key: Optional[str] = None, model: Optional[str] = None):
    #openai.api_key = api_key
    logger.info("Starting skill extraction using LLM")

    prompt = f"""
    Extract key skills, certifications, and relevant experience from the following CV text:
    {cv_text}
    """

    try:
        llm = ChatOpenAI(model="gpt-4", openai_api_key=api_key, temperature=0)

        # ConversationChain without memory
        conversation = ConversationChain(
            llm=llm,
            verbose=True
        )
        
        llm_input=get_parsing_prompt(cv_text)
        extracted_data= conversation.predict(input=llm_input)
        logger.info("Skill extraction completed successfully")
        return extracted_data

    except Exception as e:
        logger.error(f"LLM parsing failed: {e}")
        return None
from langchain_openai import ChatOpenAI
from typing import Optional, List
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from app.services.llm.prompt_templates import get_ranking_prompt

def get_llm_response(llm_input,api_key,jd="",llm_ranking=False):


    llm = ChatOpenAI(model="gpt-4", openai_api_key=api_key, temperature=0)

    # LangChain operations
    memory = ConversationBufferMemory(max_token_limit=100, return_messages=True)

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )



    if llm_ranking:
        llm_input = get_ranking_prompt(llm_input,jd)
        ats=conversation.predict(input=llm_input)
        return ats
    # Query the model
    ats=conversation.predict(input=llm_input)
    return ats

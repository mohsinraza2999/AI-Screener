from langchain_core.language_models.llms import LLM
from typing import Optional, List
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from app.services.llm.prompt_templates import get_ranking_prompt

class LangLLM(LLM):
    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "LLM Wrapper for Langchain"

    def _call(self,prompt: str,stop: Optional[List[str]] = None,chatbot=None) -> str:

        #from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

        tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
        model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")


        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device_map="auto",  # optional: use GPU if available
        )

        generation_args = {
            "max_new_tokens": 200,
            "return_full_text": False,
            "temperature": 0.7,
            "do_sample": True,
            "top_p": 0.95,
            "top_k": 50
        }
        output = pipe(prompt, **generation_args)
        response = output[0]['generated_text']
        return response
    


def get_llm_response(llm_input,jd,llm_ranking=False):
    llm = LangLLM()


        #Langchain operations
    memory = ConversationBufferMemory(llm=llm, max_token_limit=100)
    conversation = ConversationChain(
        llm=llm, 
        memory = memory,
        verbose=True
    )


    if llm_ranking:
        llm_input = get_ranking_prompt(llm_input,jd)
        ats=conversation.predict(input=llm_input)
        return ats
    # Query the model
    ats=conversation.predict(input=llm_input)
    return ats

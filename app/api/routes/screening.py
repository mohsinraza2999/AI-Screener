from fastapi import APIRouter, Depends, HTTPException, Form, File,UploadFile
from fastapi.responses import JSONResponse
from app.model.schemas import ScreeningRequest, ScreeningResponse
from typing import List
from app.services.screening import Screener
from app.services.llm.llm_ranking import get_llm_response

#from app.services.vector_store import VectorStore

router = APIRouter()

# Initialize vector store + screener
#vector_store = VectorStore()
screener = Screener()


@router.post("/screen-candidate")
def screen_candidates(api_key: str = Form(...),
    llm: str = Form(...),
    parser: str = Form(...),
    message: str = Form(...),
    cv: List[UploadFile] = File(None)):
    try:
        if cv:
            results, llm_response = screener.screen_candidates(ScreeningRequest(api_key,llm,parser,message,cv))
            return JSONResponse({
        "reply": ScreeningResponse(results=results),
        "extracted": llm_response
    })
        else:
            if api_key:
                return JSONResponse({
        "reply": get_llm_response(message,api_key,None,False),
        "extracted": "No CV is provided"
    })
            return JSONResponse({
        "reply": "No API KEY and CVs",
        "extracted": "Please provide atleast one!"
    })


        extracted_texts=[]
        extracted_texts.append({
                "filename": "file.filename",
                "preview": "text" # just first 300 chars
            })
        
        return JSONResponse({
        "reply": ScreeningResponse(results=results),
        "fit_score": "80 %",
        "skill_match": ['python','AI'],
        "extracted": llm_response
    })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

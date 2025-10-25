from app.services.nlp.get_skills import extract_education, get_skill, get_expireince

def parse_cv(resume):
        return {
            "skills": get_skill(resume),
            "education":extract_education(resume),
            "expirence":get_expireince(resume)
        }

     
import re
import spacy
import nltk
nltk.download('stopwords')
nlp1 = spacy.load('en_core_web_sm')
ruler=nlp1.add_pipe('entity_ruler', after='parser')
skill_pattern_path = "app/services/nlp/jz_skill_patterns.jsonl"
ruler.from_disk(skill_pattern_path)
nlp = spacy.load('en_core_web_sm')



from nltk.corpus import stopwords

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','associate',"Bachelors","Masters"
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for id,texs in enumerate(text.split()):
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,|’]', r'', texs)
            if (tex.lower() in [x.lower() for x in EDUCATION]) & (tex not in STOPWORDS):
                edu[tex] = texs+" " + " ".join(text.split()[id+1:id+6])

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((edu[key], ''.join(year[0])))
        else:
            education.append(edu[key])
    return education


def get_skill(text):

    doc = nlp1(text)
    return set({ent.text for ent in doc.ents if ent.label_ == "SKILL"})

def get_expireince(resume):
    return re.findall(r'(\d+)\+?\s+years?', resume) or 0


def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 & len(number) <16:
            return number
    return None


def extract_emails(resume_text):
    email=re.findall(EMAIL_REG, resume_text)
    if email:
        return email[0]
    return None


def extract_name(resume_text):
    
    doc = nlp(resume_text)
    return [(X.text, X.label_) for X in doc.ents if X.label_ == 'PERSON'][0]
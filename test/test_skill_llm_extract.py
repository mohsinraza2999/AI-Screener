import pytest
from app.services.llm.extract_skills_llm import parse_cv

def test_llm_extraction_success(monkeypatch):
    # Mock OpenAI response
    class MockResponse:
        def __getitem__(self, key):
            return {
                'choices': [{
                    'message': {
                        'content': "Skills: Python, SQL, AWS"
                    }
                }]
            }

    def mock_create(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("openai.ChatCompletion.create", mock_create)

    cv_text = "Experienced in Python, SQL, and AWS cloud services."
    skill =["Python", "SQL", "AWS"]
    result = parse_cv(cv_text)
    search_in_data(result,skill)
    
    

def test_llm_extraction_failure(monkeypatch):
    def mock_create(*args, **kwargs):
        raise Exception("API error")

    monkeypatch.setattr("openai.ChatCompletion.create", mock_create)

    cv_text = "Some generic CV text."
    result = parse_cv(cv_text)
    search_in_data(result,[])



def search_in_data(data, terms):
    if not terms:
        # If terms is None, empty list, or empty dict
        assert not data, "Data should also be empty or None when terms are empty."
        return

    missing_terms = []

    for term in terms:
        found = False

        if isinstance(data, str):
            found = term in data

        elif isinstance(data, list):
            found = any(term in str(item) for item in data)

        elif isinstance(data, dict):
            found = any(term in str(k) for k in data.keys()) or any(term in str(v) for v in data.values())

        else:
            raise TypeError(f"Unsupported data type: {type(data).__name__}")

        if not found:
            missing_terms.append(term)

    assert not missing_terms, f"Missing terms: {', '.join(missing_terms)}"



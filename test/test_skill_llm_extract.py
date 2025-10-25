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
    result = parse_cv(cv_text)
    assert "Python" in result
    assert "SQL" in result
    assert "AWS" in result

def test_llm_extraction_failure(monkeypatch):
    def mock_create(*args, **kwargs):
        raise Exception("API error")

    monkeypatch.setattr("openai.ChatCompletion.create", mock_create)

    cv_text = "Some generic CV text."
    result = parse_cv(cv_text)
    assert result is None or []

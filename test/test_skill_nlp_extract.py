import pytest
from app.services.nlp.extract_skills import parse_cv

def test_extract_skills_basic():
    cv_text = """
    John Doe is a software engineer with experience in Python, SQL, and AWS.
    He has worked on machine learning projects and is familiar with Docker and Java.
    """
    expected_skills = {"Python", "SQL", "AWS", "Machine Learning", "Docker", "Java"}
    extracted = set(parse_cv(cv_text))

    # Check that all expected skills are found
    assert expected_skills.issubset(extracted)

def test_extract_skills_case_insensitivity():
    cv_text = "Expert in python, sql, and aws cloud services."
    extracted = set(parse_cv(cv_text))
    skill =["Python", "SQL", "AWS"]
    search_in_data(extracted,skill)

def test_extract_skills_empty_input():
    cv_text = ""
    extracted = parse_cv(cv_text)
    search_in_data(extracted,[])

def test_extract_skills_no_match():
    cv_text = "This CV contains no technical skills or keywords."
    extracted = parse_cv(cv_text)
    search_in_data(extracted,[])
    

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

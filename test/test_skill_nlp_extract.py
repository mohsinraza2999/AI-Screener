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
    assert "Python" in extracted.skills
    assert "SQL" in extracted.skills
    assert "AWS" in extracted.skills

def test_extract_skills_empty_input():
    cv_text = ""
    extracted = parse_cv(cv_text)
    assert extracted == {
            "skills": None,
            "education":None,
            "expirence":None
        }

def test_extract_skills_no_match():
    cv_text = "This CV contains no technical skills or keywords."
    extracted = parse_cv(cv_text)
    assert extracted == {
            "skills": None,
            "education":None,
            "expirence":None
        }
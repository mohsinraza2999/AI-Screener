import pytest
from nlp.extract_skills_nlp import extract_skills

def test_extract_skills_basic():
    cv_text = """
    John Doe is a software engineer with experience in Python, SQL, and AWS.
    He has worked on machine learning projects and is familiar with Docker and Java.
    """
    expected_skills = {"Python", "SQL", "AWS", "Machine Learning", "Docker", "Java"}
    extracted = set(extract_skills(cv_text))

    # Check that all expected skills are found
    assert expected_skills.issubset(extracted)

def test_extract_skills_case_insensitivity():
    cv_text = "Expert in python, sql, and aws cloud services."
    extracted = set(extract_skills(cv_text))
    assert "Python" in extracted
    assert "SQL" in extracted
    assert "AWS" in extracted

def test_extract_skills_empty_input():
    cv_text = ""
    extracted = extract_skills(cv_text)
    assert extracted == []

def test_extract_skills_no_match():
    cv_text = "This CV contains no technical skills or keywords."
    extracted = extract_skills(cv_text)
    assert extracted == []

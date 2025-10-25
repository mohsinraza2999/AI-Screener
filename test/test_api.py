import pytest
from app.api.routes import health

from fastapi.testclient import TestClient
import sys, os
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.api.main import app
client = TestClient(app)

results=['Loan is Approved','Loan is Not Approved']
def test_app():
    
    response = client.get("/")
    assert response.status_code == 200

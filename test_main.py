from fastapi.testclient import TestClient
# We import 'app' from the 'main.py' file
from main import app 

# Initialize the test client using your FastAPI app object
client = TestClient(app)

def test_read_root():
    """Tests the root endpoint (/) to ensure it returns 200 and the correct message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Containerized Quote API"}

def test_get_quote():
    """Tests the quote endpoint (/api/quote) to ensure it returns 200 and the required data structure."""
    response = client.get("/api/quote")
    # 1. Check for a successful status code
    assert response.status_code == 200
    
    # 2. Check the data structure
    data = response.json()
    assert "quote" in data and "author" in data
    
    # 3. Check for the specific author name to ensure the data is correct
    assert data["author"] == "Nelson Mandela"
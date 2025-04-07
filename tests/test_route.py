import json
from app import app
import tempfile

def test_birthdays_success():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("name,birthdate\nAlice,1990-01-01\nBob,1991-02-02\n")
        f.flush()

        # Patch the read_employees function
        from tasks import read_employees
        original = read_employees
        try:
            import tasks
            tasks.read_employees = lambda _: original(f.name)
            client = app.test_client()
            response = client.get("/birthdays")
            data = json.loads(response.data)

            assert response.status_code == 200
            assert data["January"] == 1
            assert data["February"] == 1
        finally:
            tasks.read_employees = original

def test_birthdays_server_error(monkeypatch):
    # Simulate read_employees throwing an error
    monkeypatch.setattr("tasks.read_employees", lambda _: (_ for _ in ()).throw(Exception("File error")))
    client = app.test_client()
    response = client.get("/birthdays")
    assert response.status_code == 500
    assert b"File error" in response.data

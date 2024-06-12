import pytest
from app.models.user_model import User

@pytest.fixture
def new_user():
    #return {"name": "testuser", "email": "testemail@example.com", "password": "testpassword", "rol":"role"}
    return {"name": "nombre", "email": "testemail@example.com", "password": "testpassword", "role": "testrole"}
#1
def test_register_user(test_client, new_user):
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201
    assert response.json["message"] == "Usuario creado exitosamente"

#2
def test_register_duplicate_user(test_client, new_user):
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 400
    assert response.json["error"] == "El nombre de usuario ya está en uso"

#3
def test_login_user(test_client, new_user):
    # Ahora intentar iniciar sesión con las credenciales válidas
    login_credentials = {
        "email": new_user["email"],
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 200  # Verifica que el inicio de sesión sea exitoso
    assert "access_token" in response.json 

#4
def test_login_invalid_user(test_client, new_user):
    login_credentials = {
        "email": "nonexistent@example.com",
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales inválidas"

#5
def test_login_wrong_password(test_client, new_user):
    login_credentials = {"email": new_user["email"], "password": "wrongpassword"}
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales inválidas"

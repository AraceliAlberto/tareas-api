#1 lista de usuaarios
"""def test_get_taks_as_member(test_client, member_auth_headers):
    # El usuario con el rol de "member" debería poder obtener la lista de takses
    response = test_client.get("/api/taks", headers=member_auth_headers)
    assert response.status_code == 200
    assert response.json == []"""

#2
def test_create_taks(test_client, admin_auth_headers):
    data = {"title": "tarea1", "description": "descripcion1", "status": "estado", "created_at": "creado", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "tarea1"
    assert response.json["description"] == "descripcion1"
    assert response.json["status"] == "estado"
    assert response.json["created_at"] == "creado"
    assert response.json["assigned_to"] == "20-04-23"

#3
def test_get_taks_as_member(test_client, member_auth_headers):
    response = test_client.get("/api/taks/1", headers=member_auth_headers)
    assert response.status_code == 200
    assert "title" in response.json
    assert "description" in response.json
    assert "status" in response.json
    assert "created_at" in response.json
    assert "assigned_to" in response.json

#4
def test_create_taks_as_member(test_client, member_auth_headers):
    data = {"title": "tarea1", "description": "descripcion1", "status": "estado", "created_at": "creado", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=member_auth_headers)
    assert response.status_code == 403

#5
def test_update_taks_as_member(test_client, member_auth_headers):
    data = {"title": "tarea1", "description": "descripcion1", "status": "estado", "created_at": "creado", "assigned_to": "20-04-23"}
    response = test_client.put("/api/taks/1", json=data, headers=member_auth_headers)
    assert response.status_code == 403

#6
def test_delete_taks_as_member(test_client, member_auth_headers):
    response = test_client.delete("/api/taks/1", headers=member_auth_headers)
    assert response.status_code == 403
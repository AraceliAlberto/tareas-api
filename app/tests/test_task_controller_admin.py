#1
def test_get_taks(test_client, admin_auth_headers):
    response = test_client.get("/api/taks", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []

#2
def test_create_task(test_client, admin_auth_headers):
    data = {"title": "tarea1", "description": "descripcion1", "status": "estado", "created_at": "creado", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "tarea1"
    assert response.json["description"] == "descripcion1"
    assert response.json["status"] == "estado"
    assert response.json["created_at"] == "creado"
    assert response.json["assigned_to"] == "20-04-23"

#3
def test_get_task(test_client, admin_auth_headers):
    # Primero crea un task
    data = {"title": "tarea2", "description": "descripcion2", "status": "estado2", "created_at": "creado2", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    task_id = response.json["id"]

    # Ahora obtén el task
    response = test_client.get(f"/api/taks/{task_id}", headers=admin_auth_headers)
    assert response.json["title"] == "tarea2"
    assert response.json["description"] == "descripcion2"
    assert response.json["status"] == "estado2"
    assert response.json["created_at"] == "creado2"
    assert response.json["assigned_to"] == "20-04-23"

#4
def test_get_nonexistent_task(test_client, admin_auth_headers):
    response = test_client.get("/api/taks/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "task no encontrado"

#5
def test_create_task_invalid_data(test_client, admin_auth_headers):
    data = {"title": "tarea3", "description": "descripcion3"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"

#6
def test_update_task(test_client, admin_auth_headers):
    # Primero crea un task
    data = {"title": "tarea3", "description": "descripcion3", "status": "estado3", "created_at": "creado3", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    task_id = response.json["id"]

    # Ahora actualiza el task
    update_data = {"title": "tareanuva", "description": "actualizada", "status": "libre", "created_at": "alvarez", "assigned_to": "20-04-23"}
    response = test_client.put(
        f"/api/taks/{task_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["title"] == "tareanuva"
    assert response.json["description"] == "actualizada"
    assert response.json["status"] == "libre"
    assert response.json["created_at"] == "alvarez"
    assert response.json["assigned_to"] == "20-04-23"

#7
def test_update_nonexistent_task(test_client, admin_auth_headers):
    update_data = {"title": "tareamal", "description": "actualizada", "status": "libre", "created_at": "alvarez", "assigned_to": "20-04-23"}
    response = test_client.put(
        "/api/taks/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "task no encontrado"

#8
def test_delete_task(test_client, admin_auth_headers):
    # Primero crea un task
    data = {"title": "tareanuva", "description": "actualizada", "status": "libre", "created_at": "alvarez", "assigned_to": "20-04-23"}
    response = test_client.post("/api/taks", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    task_id = response.json["id"]

    # Ahora elimina el task
    response = test_client.delete(
        f"/api/taks/{task_id}", headers=admin_auth_headers
    )
    assert response.status_code == 204

    # Verifica que el task ha sido eliminado
    response = test_client.get(f"/api/taks/{task_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "task no encontrado"

#9
def test_delete_nonexistent_task(test_client, admin_auth_headers):
    response = test_client.delete(f"/api/taks/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "task no encontrado"
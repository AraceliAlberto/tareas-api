from flask import Blueprint, request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from app.models.task_model import Task
from app.views.task_view import render_tasks_list, render_task_detail
from app.utils.decorators import jwt_required, role_required

task_bp = Blueprint("task", __name__)

@task_bp.route("/taks", methods=["GET"])
@jwt_required
def get_tasks():
    tasks = Task.get_all()
    return jsonify(render_tasks_list(tasks))

@task_bp.route("/taks/<int:id>", methods=["GET"])
@jwt_required
def get_task(id):
    task = Task.get_by_id(id)
    if task:
        return jsonify(render_task_detail(task))
    return jsonify({"error": "task no encontrado"}), 404

@task_bp.route("/taks", methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def post_task():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")
    print(title)

    if not title or not description or not status or not created_at or not assigned_to:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    task = Task(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)
    task.save()
    return jsonify(render_task_detail(task)), 201

@task_bp.route("/taks/<int:id>", methods=["PUT"])
@jwt_required
@role_required(role=["admin"])
def update_task(id):
    tasks = Task.get_by_id(id)

    if not tasks:
        return jsonify({"error": "task no encontrado"}), 404

    data = request.json
    
    if "title" in data:
        tasks.title = data['title']
    if "description" in data:
        tasks.description = data['description']
    if "status" in data:
        tasks.status = data['status']
    if "created_at" in data:
        tasks.created_at = data['created_at']
    if "assigned_to" in data:
        tasks.assigned_to = data['assigned_to']

    tasks.save()
    return jsonify(render_task_detail(tasks))

@task_bp.route("/taks/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(role=["admin"])
def delete_task(id):
    tasks = Task.get_by_id(id)
    if not tasks:
        return jsonify({"error": "task no encontrado"}), 404

    tasks.delete()
    return "", 204
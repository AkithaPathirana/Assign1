from flask import Blueprint, request, jsonify
from .models import Task

task_bp = Blueprint('task_bp', __name__)

# Create a new task
@task_bp.route('/', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')  # Set an empty string if 'description' is not provided
    new_task = Task(title=title, description=description)
    Task.add_task(new_task)
    return jsonify({
        'message': 'Task created successfully!', 
        'task': {
            'id': new_task.id, 
            'title': new_task.title, 
            'description': new_task.description
        }
    }), 201


# Get all tasks
@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.get_all_tasks()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]), 200

# Get a specific task by ID
@task_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.get_task(id)
    if task:
        return jsonify({'id': task.id, 'title': task.title, 'description': task.description}), 200
    return jsonify({'message': 'Task not found'}), 404

# Update a task by ID
@task_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    success = Task.update_task(id, title=data['title'], description=data.get('description', ''))
    if success:
        return jsonify({'message': 'Task updated successfully!'}), 200
    return jsonify({'message': 'Task not found'}), 404

# Delete a task by ID
@task_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    success = Task.delete_task(id)
    if success:
        return jsonify({'message': 'Task deleted successfully!'}), 200
    return jsonify({'message': 'Task not found'}), 404

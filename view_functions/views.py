from flask import Blueprint, request, jsonify
from models.posts import Post
from sample_data import posts_data

posts_bp = Blueprint('posts', __name__)


# Index
@posts_bp.route('/', methods=['GET'])
def index():
    return "Restful API's app is running..."


# Endpoint to create a new post
@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    if 'author' in data and 'content' in data:
        new_post = Post(len(posts_data) + 1, data['author'], data['content'])
        posts_data.append(new_post)
        return jsonify(new_post), 201
    else:
        return "Bad Request", 400


# Endpoint to get all posts
@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    return jsonify([post.to_dict() for post in posts_data])


# Endpoint to get a specific post by ID
@posts_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts_data if p.id == post_id), None)
    if post:
        return jsonify(post.to_dict())
    else:
        return "Not Found", 404


# Endpoint to update a specific post by ID using PUT
@posts_bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json
    post = next((p for p in posts_data if p.id == post_id), None)
    if post and 'author' in data and 'content' in data:
        post.author = data['author']
        post.content = data['content']
        return jsonify(post.to_dict())
    else:
        return "Not Found", 404


# Endpoint to update a specific post by ID using PATCH
@posts_bp.route('/posts/<int:post_id>', methods=['PATCH'])
def patch_post(post_id):
    data = request.json
    post = next((p for p in posts_data if p.id == post_id), None)
    if post:
        if 'author' in data:
            post.author = data['author']
        if 'content' in data:
            post.content = data['content']
        return jsonify(post.to_dict())
    else:
        return "Not Found", 404


# Endpoint to delete a specific post by ID
@posts_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in posts_data if p.id == post_id), None)
    if post:
        posts_data.remove(post)
        return "No Content", 204
    else:
        return "Not Found", 404

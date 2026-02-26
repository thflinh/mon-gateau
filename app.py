from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
from bson.objectid import ObjectId
import os
import uuid

app = Flask(__name__)

# Where to save uploaded images (relative to app root)
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[-1].lower() in ALLOWED_EXTENSIONS


def save_uploaded_file(file):
    """Save an uploaded image; return URL path like /static/images/uploads/xxx.jpg."""
    if not file or not file.filename or not allowed_file(file.filename):
        return None
    ext = file.filename.rsplit(".", 1)[-1].lower()
    name = f"{uuid.uuid4().hex}.{ext}"
    path = os.path.join(UPLOAD_FOLDER, name)
    file.save(path)
    return f"/static/images/uploads/{name}"


def request_to_cake_data():
    """
    Read request as either JSON or multipart form + optional image file.
    Returns (data dict, error_response or None).
    """
    if request.content_type and "multipart/form-data" in request.content_type:
        form = request.form
        image_url = (form.get("image") or "").strip()
        uploaded = request.files.get("image_file")
        if uploaded and uploaded.filename:
            image_url = save_uploaded_file(uploaded) or image_url
        ingredients_str = form.get("ingredients") or ""
        steps_str = form.get("steps") or ""
        data = {
            "name": (form.get("name") or "").strip(),
            "description": (form.get("description") or "").strip(),
            "category": (form.get("category") or "").strip(),
            "difficulty": (form.get("difficulty") or "Easy").strip(),
            "prep_time": (form.get("prep_time") or "").strip(),
            "bake_time": (form.get("bake_time") or "").strip(),
            "servings": int(form.get("servings") or 0) or 0,
            "ingredients": [s.strip() for s in ingredients_str.split("\n") if s.strip()],
            "steps": [s.strip() for s in steps_str.split("\n") if s.strip()],
        }
        data["image"] = image_url
        return data, None
    # JSON body
    data = request.get_json(silent=True) or {}
    if not isinstance(data.get("ingredients"), list):
        data["ingredients"] = []
    if not isinstance(data.get("steps"), list):
        data["steps"] = []
    return data, None


def to_json(doc):
    """Convert MongoDB doc: ObjectId -> str for JSON serialization."""
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


MONGO_URI = os.environ.get("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is not set. Add it to .env or your shell.")
client = MongoClient(MONGO_URI)
db = client["cakedb"]
cakesCollection = db["cakes"]

@app.route("/api/debug")
def debug():
    """Check DB connection and document count (remove in production)."""
    try:
        count = cakesCollection.count_documents({})
        return jsonify({"status": "ok", "cakes_count": count})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/cakes", methods=["GET"])
def get_cakes():
    cakes = [to_json(c) for c in cakesCollection.find()]
    return jsonify(cakes)


@app.route("/api/cakes", methods=["POST"])
def create_cake():
    data, err = request_to_cake_data()
    if err:
        return err

    required_fields = [
        "name",
        "description",
        "category",
        "difficulty",
        "prep_time",
        "bake_time",
        "servings",
        "ingredients",
        "steps",
    ]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return (
            jsonify({"error": f"Missing fields: {', '.join(missing)}"}),
            400,
        )
    if not isinstance(data.get("ingredients"), list) or not isinstance(
        data.get("steps"), list
    ):
        return jsonify({"error": "ingredients and steps must be arrays"}), 400
    if "image" not in data:
        data["image"] = ""

    result = cakesCollection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return jsonify(data), 201


@app.route("/api/cakes/<cake_id>", methods=["PUT"])
def update_cake(cake_id):
    """Update an existing cake by ID."""
    try:
        oid = ObjectId(cake_id)
    except Exception:
        return jsonify({"error": "Invalid cake id"}), 400

    existing = cakesCollection.find_one({"_id": oid})
    if not existing:
        return jsonify({"error": "Cake not found"}), 404

    data, err = request_to_cake_data()
    if err:
        return err
    # If no image provided in form/upload, keep existing
    if not data.get("image") and existing.get("image"):
        data["image"] = existing["image"]

    required_fields = [
        "name",
        "description",
        "category",
        "difficulty",
        "prep_time",
        "bake_time",
        "servings",
        "ingredients",
        "steps",
    ]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return (
            jsonify({"error": f"Missing fields: {', '.join(missing)}"}),
            400,
        )
    if not isinstance(data.get("ingredients"), list) or not isinstance(
        data.get("steps"), list
    ):
        return jsonify({"error": "ingredients and steps must be arrays"}), 400

    result = cakesCollection.update_one({"_id": oid}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "Cake not found"}), 404

    updated = cakesCollection.find_one({"_id": oid})
    return jsonify(to_json(updated)), 200


@app.route("/api/cakes/<cake_id>", methods=["DELETE"])
def delete_cake(cake_id):
    """Delete a cake by ID."""
    try:
        oid = ObjectId(cake_id)
    except Exception:
        return jsonify({"error": "Invalid cake id"}), 400

    result = cakesCollection.delete_one({"_id": oid})
    if result.deleted_count == 0:
        return jsonify({"error": "Cake not found"}), 404

    return jsonify({"status": "deleted", "id": cake_id}), 200

@app.route("/api/search", methods=["GET"])
def search_cake():
    query = request.args.get("q")
    if not query:
        return jsonify([])
    cakes = [to_json(c) for c in cakesCollection.find({"name": {"$regex": query, "$options": "i"}})]
    return jsonify(cakes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



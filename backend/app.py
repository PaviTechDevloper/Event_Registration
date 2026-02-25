from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "event.db"

# Create table automatically
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            event_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Register API
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO registrations
        (name, department, age, phone, email, event_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["department"],
        data["age"],
        data["phone"],
        data["email"],
        data["event_type"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Registration Successful!"})


# Fetch All Registrations
@app.route("/registrations", methods=["GET"])
def get_registrations():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registrations")
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "age": row[3],
            "phone": row[4],
            "email": row[5],
            "event_type": row[6],
            "created_at": row[7]
        })

    conn.close()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
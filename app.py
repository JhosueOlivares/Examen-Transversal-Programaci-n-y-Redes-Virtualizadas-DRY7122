from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Configuración de Flask
app = Flask(__name__)

# Configuración de la base de datos
def init_db():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL)''')
        conn.commit()

# Inicializar la base de datos
init_db()

# Ruta para agregar usuarios
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

    return jsonify({'message': 'Usuario agregado exitosamente'}), 201

# Ruta para validar usuarios
@app.route('/validate_user', methods=['POST'])
def validate_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = c.fetchone()

        if result and check_password_hash(result[0], password):
            return jsonify({'message': 'Usuario validado exitosamente'}), 200
        else:
            return jsonify({'message': 'Credenciales inválidas'}), 401

# Ejecutar la aplicación en el puerto 5800
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)

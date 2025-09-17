from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista inicial de estudiantes
estudiantes = [
    {"id": 1, "nombre": "Ana Flores", "carrera": "Auditoria"},
    {"id": 2, "nombre": "Luís Loza", "carrera": "Sistemas"},
    {"id": 3, "nombre": "Nanta Pinto", "carrera": "Derecho"}
]

# Ejercicio 1 - Rutas básicas
@app.route('/')
def inicio():
    return "Bienvenido al sistema de estudiantes"

@app.route('/curso')
def curso():
    return jsonify({
        "curso": "Gestión de estudiantes",
        "semestre": "II-2025",
        "estudiantes": "Kevin"
    })

# Ejercicio 2 - API de gestión de estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify(estudiantes)

@app.route('/estudiantes/<int:id>', methods=['GET'])
def obtener_estudiante(id):
    estudiante = next((e for e in estudiantes if e['id'] == id), None)
    if estudiante:
        return jsonify(estudiante)
    return jsonify({"error": "Estudiante no encontrado"}), 404

@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    nuevo_estudiante = request.get_json()
    
    if not nuevo_estudiante or 'nombre' not in nuevo_estudiante or 'carrera' not in nuevo_estudiante:
        return jsonify({"error": "Datos incompletos"}), 400
    
    # Generar nuevo ID
    nuevo_id = max([e['id'] for e in estudiantes]) + 1 if estudiantes else 1
    
    estudiante = {
        "id": nuevo_id,
        "nombre": nuevo_estudiante['nombre'],
        "carrera": nuevo_estudiante['carrera']
    }
    
    estudiantes.append(estudiante)
    return jsonify({"mensaje": "Estudiante agregado correctamente"}), 201

@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    global estudiantes
    estudiante = next((e for e in estudiantes if e['id'] == id), None)
    
    if not estudiante:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    
    estudiantes = [e for e in estudiantes if e['id'] != id]
    return jsonify({"mensaje": "Estudiante eliminado correctamente"})

if __name__ == '_main_':
    app.run(debug=True)
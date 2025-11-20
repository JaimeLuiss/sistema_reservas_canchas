from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal del sistema
@app.route('/')
def home():
    return "🏟️ Sistema de Reservas de Canchas Deportivas - Versión 1.0"

# Punto de entrada principal
if __name__ == '__main__':
    # Inicia el servidor en modo depuración
    app.run(debug=True)

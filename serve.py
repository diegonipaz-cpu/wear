"""
Servidor local para la PWA.
Necesita HTTPS para que el telefono pueda acceder a la camara.

Instala: pip install flask pyopenssl
Ejecuta: python serve.py
Luego en el telefono: https://IP_DEL_PC:5000
(acepta el aviso de certificado no confiable)
"""
import socket
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    print(f"\n Abre en el telefono: https://{ip}:5000\n")
    print(" Acepta el aviso de seguridad del certificado en el navegador.\n")
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc', debug=False)

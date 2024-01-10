from flask import Flask, jsonify
from multiprocessing import Queue
import os
import bcrypt
import importlib
import logging


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.setLevel(logging.ERROR)
cola_respuesta = Queue()



# Crear una cola para compartir la respuesta global
cola_respuesta = Queue()

def obtener_respuesta():
    
    with open('database.txt', 'r') as archivo:
        # Lee todo el contenido del archivo
        contenido = archivo.read()
        
    #--------------------------------------------------------------------------------------------------------
    #Aqui va su codigo de programacion.
    
    resp = int(contenido)
    resp = resp + 50
        
    
    
    #Aqui termina su codigo de programacion
    #----------------------------------------------------------------------------------------------------------
    
    
    
     
    # Imprime el contenido leído
    

    if not cola_respuesta.empty():
        respuesta = cola_respuesta.get()
        return respuesta
    else:                              #por aqui enviamos los resultados a silverbullet
        return jsonify(Resultado=f"la suma es:'{resp}' ")

@app.route('/respuesta', methods=['GET'])
def obtener_respuesta_route():
    return obtener_respuesta()

if __name__ == '__main__':
    app.run(port=5001, use_reloader=False, debug=False)

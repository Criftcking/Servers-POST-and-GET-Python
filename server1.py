from flask import Flask, request, jsonify
from multiprocessing import Queue, Process, freeze_support
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.setLevel(logging.ERROR)
cola_respuesta = Queue()




@app.route('/datos', methods=['POST'])
def recibir_datos():
    datos = request.form['dato']
    # Realizar alguna lógica con los datos recibidos
    respuesta = datos
    variable = respuesta

    # Abre el archivo en modo escritura
    with open('database.txt', 'w') as archivo:
        # Escribe el valor de la variable en el archivo
        archivo.write(variable)

    cola_respuesta.put(datos)  # Agregar la respuesta a la cola

    return jsonify(Solicitud=respuesta)

def iniciar_servidor():
    app.run(port=5000, use_reloader=False, debug=False)

if __name__ == '__main__':
    freeze_support()
    p = Process(target=iniciar_servidor)
    p.start()
    p.join()

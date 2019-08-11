from flask import Flask, request

from controller.file_controller import FileController

app = Flask(__name__)
file_control = FileController()


@app.route("/spec")
def init():
    return 'Ok'


@app.route("/get_customer_information/<id>")
def get_json(id):
    id_json = str(id) + '.json'
    return file_control.read_json(id_json)


@app.route("/post_customer_information", methods=['POST'])
def post_json():
    current_data = request.get_json()
    return file_control.write_json(current_data)


app.run()

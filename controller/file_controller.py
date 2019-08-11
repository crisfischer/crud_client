import json
import os


class FileController(object):

    def list_dir(self):
        return os.listdir("/home/cristianefischer/projetos/api/client")

    def read_json(self, id_json):
        if id_json in self.list_dir():
            with open('client/' + id_json) as jd:
                return json.loads(jd.read())
        return "Não existe!"

    def write_json(self, id_name, current_data):
        id_name = str(current_data.get("id")) + '_' + str(current_data.get("name")) + '.json'
        if id_name not in self.list_dir():
            with open('client/' + id_name, 'w') as jf:
                json.dump(current_data, jf)
            return 'Adicionado com sucesso o id: {id_name}'.format(id_name=id_name)
        return 'Error. Não pode adicionar!'

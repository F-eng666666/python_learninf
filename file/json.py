import json
import pathlib



current_path = str(pathlib.Path(__file__).parent.resolve())
class Read():
    def read_json(self):
        file_path = current_path+"\jsontest.json"
        print(file_path)
        file = open(file_path)
        json.load(file)
        #return json.load(open('jsontest.json','r',encoding="utf-8"))['item']


read = Read()
read.read_json()
# print(read)
#pprint.pprint(read.read_json())



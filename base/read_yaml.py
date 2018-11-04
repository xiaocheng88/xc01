import os
import yaml


class ReadYaml():
    def __init__(self,filename):
        self.ya_path = os.getcwd()+os.sep+"data"+os.sep+filename
    def read_yaml(self):
        with open(self.ya_path,"r",encoding="utf-8")as f:
            return yaml.load(f)

#     def get_data(self):
#         with open("../data/get_data.yaml","r",encoding="utf-8")as f:
#             return yaml.load(f)
# if __name__ == '__main__':
#     list1 = []
#     for data in ReadYaml().get_data().values():
#         list1.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
#     print(list1)
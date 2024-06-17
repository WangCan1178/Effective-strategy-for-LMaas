import json
from abc import ABCMeta, abstractmethod
from datetime import datetime

''''''
def div_file(data):
    return data.split("\n")

def save_file(input_file, method_name, data):
    file_name, append = input_file.rsplit(".",1)
    intermediate_filename = f"{file_name}_{method_name}.{append}"
    with open(intermediate_filename, 'w') as file:
        file.write(data)

# 将字典格式转为json格式并保存
def save_json(save_file,data):
    total_data=[]
    with open(save_file,'r') as file:
        existing_data=json.load(file)
    total_data=existing_data
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    data['date'] = time_string

    total_data.append(data)
    print(111)
    with open(save_file,'w') as file:
        json.dump(total_data,file,indent=4)
        print(222)


class Method(metaclass=ABCMeta):
    def __init__(self):
        pass
    def __str__(self):
        return self.__class__.__name__
    @abstractmethod
    def process(self, data):
        pass
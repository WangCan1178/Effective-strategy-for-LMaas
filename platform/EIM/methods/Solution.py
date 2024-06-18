import sys, json, copy
import logging
from EIM_model.Util import Method,div_file


def getData_by_QueryAndModel(datas, sample_query, model):
    for sample in datas:
        if sample['query'] == sample_query and sample['model'] == model:
            # print(111)
            return sample


# 成本优先 级联路线：cohere_command→ai21_j2grande→openai_gpt4
class cost_priority(Method):
    @staticmethod
    def process(data):
        file_input='D:\\Python\\PythonProject\\EIM_proj\\EIM_model\\files\\datas_test.json'
        with open(file_input,'r',encoding='utf-8') as file:
            datasets=json.load(file)
        sample=getData_by_QueryAndModel(datasets,data,"cohere_command-light")
        if sample==None:
            return None,None,0,None
        cost = sample['cost']
        if sample['is_right']==1:
            model="cohere_command-light"
            tip=""
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"ai21_j2-grande")
        cost += sample['cost']
        if sample['is_right']==1:
            tip="cohere_command-light的答案错误!"
            model="ai21_j2-grande"
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"openai_gpt-4-0613")
        cost += sample['cost']
        model="openai_gpt-4-0613"
        tip="cohere_command-light和ai21_j2-grande的答案错误!"
        return tip,model,cost,sample['output']

# 性能优先 级联路线：cohere_command→openai_gpt4→ai21_j2grande
class responce_priority(Method):
    @staticmethod
    def process(data):
        # sys.path.append("D:\\Python\\PythonProject\\EIM_proj")

        # 测试数据id   id8075: gsm8k:null
        # file_input = '../files/datas_test.json'
        file_input = 'D:/Python/PythonProject/EIM_proj/EIM_model/files/datas_test.json'
        with open(file_input,'r',encoding='utf-8') as file:
            datasets=json.load(file)
        sample=getData_by_QueryAndModel(datasets,data,"cohere_command-light")
        cost = sample['cost']
        if sample['is_right']==1:
            model="cohere_command-light"
            tip=""
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"openai_gpt-4-0613")
        cost += sample['cost']
        if sample['is_right']==1:
            tip="cohere_command-light的答案错误!"
            model="openai_gpt-4-0613"
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"ai21_j2-grande")
        cost += sample['cost']
        model="ai21_j2-grande"
        tip="cohere_command-light和openai_gpt-4-0613的答案错误!"
        return tip,model,cost,sample['output']

#
class right_priority(Method):
    @staticmethod
    def process(data):
        # sys.path.append("D:\\Python\\PythonProject\\EIM_proj")

        # 测试数据id   id8075: gsm8k:null
        # file_input = 'D:/Python/PythonProject/EIM_proj/EIM_model/files/datas_test.json'
        file_input = '../files/datas_test.json'
        with open(file_input,'r',encoding='utf-8') as file:
            datasets=json.load(file)
        sample=getData_by_QueryAndModel(datasets,data,"openai_gpt-4-0613")
        cost = sample['cost']
        if sample['is_right']==1:
            model="openai_gpt-4-0613"
            tip=""
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"ai21_j2-grande")
        cost += sample['cost']
        if sample['is_right']==1:
            tip="openai_gpt-4-0613的答案错误!"
            model="ai21_j2-grande"
            return tip,model,cost,sample['output']

        sample=getData_by_QueryAndModel(datasets,data,"cohere_command-light")
        cost += sample['cost']
        model="cohere_command-light"
        tip="openai_gpt-4-0613和ai21_j2-grande的答案错误!"
        return tip,model,cost,sample['output']


def Solution(Solution_method=None, input_set=None):
    if Solution_method=="cost_priority":
        return cost_priority()
    elif Solution_method=="responce_priority":
        return responce_priority()
    elif Solution_method=="right_priority":
        return right_priority()
    # else:
    #     print("类型错误！！！")

#

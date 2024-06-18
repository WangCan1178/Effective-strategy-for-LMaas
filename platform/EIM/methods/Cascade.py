import sys, json, copy
import logging

logging.disable(logging.CRITICAL)
# sys.path.append("src/")

import os
os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'
# os.environ['AI21_STUDIO_API_KEY'] = 'AI21_STUDIO_API_KEY'
os.environ['AI21_STUDIO_API_KEY'] = 'JZpUSU0xDkFMdwTMjK5eFYK7z2UiK0lv'
# os.environ['COHERE_STUDIO_API_KEY'] = 'COHERE_STUDIO_API_KEY'
os.environ['COHERE_STUDIO_API_KEY'] = '4nNT1zz4k17hAr3f8PqvnTdEfEu7SUYlmhzm1s1W'
os.environ['TEXTSYNTH_API_SECRET_KEY'] = 'TEXTSYNTH_API_SECRET_KEY'
os.environ['ANTHROPIC_API_KEY'] = 'ANTHROPIC_API_KEY'
from IPython.display import display
import FrugalGPT
supported_LLM = FrugalGPT.getservicename()
# print("supported LLMs:",supported_LLM)

dev = FrugalGPT.loadcsvdata("D:/Python/PythonProject/EIM_proj/FrugalGPT/data/HEADLINES/train.csv")
dev = dev[0:500]
prefix = open('D:\Python\PythonProject\EIM_proj\FrugalGPT\config\prompt\HEADLINES\prefix_e8.txt').read()
data = FrugalGPT.formatdata(dev,prefix)

# train the model
MyCascade = FrugalGPT.LLMCascade()
service_names = ['ai21/j1-jumbo','cohere/command','ai21/j1-large']
user_budget = 0.002
result = MyCascade.train(data,budget=user_budget,service_names=service_names)
print(result)

# MyLLMforAll = FrugalGPT.LLMforAll()
# query = "Question: Who is Matei Zaharia in 2023?\nAnswer:"
# service_name = supported_LLM[-1]
# genparams = FrugalGPT.GenerationParameter(max_tokens=50, temperature=0.1, stop=['\n\n\n\n'])
# answer = MyLLMforAll.get_completion(query,service_name,genparams=genparams)
# cost = MyLLMforAll.get_cost()
# print("API:",service_name,"answer:",answer,"cost:",cost)








# import sqlite3
# # 连接到SQLite数据库
# conn = sqlite3.connect('D:\Python\PythonProject\EIM_proj\FrugalGPT\db\HEADLINES.sqlite')  # 替换为您的数据库文件路径
#
# # 创建游标对象
# cursor = conn.cursor()
#
# # 执行SQL查询
# cursor.execute('SELECT * FROM unnamed')
#
# # 获取查询结果的列名
# column_names = [description[0] for description in cursor.description]
#
# # 获取查询结果
# results = cursor.fetchall()
#
# print(result)
# # 关闭游标和数据库连接
# cursor.close()
# conn.close()
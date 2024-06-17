import tiktoken
from EIM_model.Util import Method
from Util import div_file


def num_tokens_from_string(string: str) -> int:
    """返回文本字符串中的Token数量"""
    encoding_name="cl100k_base"
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

#
# input_file="../files/input.txt"
# with open(input_file,'r') as file:
#     text=file.read()
#
#  data=[]
# for query in div_file(text):
#     num=tiktoken()
# num=num_tokens_from_string(text)
# print(num)
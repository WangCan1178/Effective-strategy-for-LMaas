import string
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from EIM_model.Util import Method, div_file
from gptrim import trim
from selective_context import SelectiveContext

class Prompt_Reducer(Method):
    def process(self, data):
        newdata = ""
        for query in div_file(data):
            # Create a lemmatizer object for English
            lemmatizer = WordNetLemmatizer()
            stop_words = set(stopwords.words('english'))
            # Split the input text into words (tokenization)
            words = query.split()
            # Apply lemmatization, remove stopwords, strip whitespace, and remove special characters
            filtered_words = [lemmatizer.lemmatize(word) for word in words if
                              word.lower() not in stop_words and word.strip() != '']
            # Remove single quotes, hyphens, and punctuation marks
            filtered_words = [word.replace("'", "").replace("-", "") for word in filtered_words]
            filtered_words = [''.join(char for char in word if char not in string.punctuation) for word in
                              filtered_words]
            # Reconstruct the processed text from the filtered words
            trimmed_query = ' '.join(filtered_words)
            newdata += trimmed_query+"\n"
        return newdata



class Gptrim(Method):
    def process(self, data):
        newdata = ""
        for query in div_file(data):
            trimmed_query = trim(query)
            newdata += trimmed_query+"\n"
        return newdata

class Selective(Method):
    def process(self,data):
        newdata=""
        for query in div_file(data):
            sc = SelectiveContext(model_type='gpt2', lang='en')
            context, reduced_content = sc(query)
            newdata += context+"\n"
        return newdata



def Input(input_method=None, input_set=None):
    if input_method == "prompt_reducer":
        return Prompt_Reducer()
    elif input_method == "gptrim":
        return Gptrim()
    elif input_method=='selective':
        return Selective()
    # else:
    #     print("Input类型错误！！！")




# class Input:
#     def  __init__(self, input_method=None, input_set=None):
#         if input_method == "prompt_reducer":
#             self.method =  Prompt_Reducer()
#         elif input_method == "gptrim":
#             self.method =  Gptrim()
#
#     def run(self, data):
#         self.method.process(data)
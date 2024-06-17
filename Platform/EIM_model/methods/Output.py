from EIM_model.Util import Method

class answer_abstract(Method):
    @staticmethod
    def process(data):
        # keywords=["The answer is "]
        data_new = data.replace("\n", "")
        keywords="The answer is "
        if keywords in data_new:
            start_index=data.find(keywords)
            # 答案提取
            result=data[start_index+len(keywords):]
            result = result.strip(".")
            return result
        else:
            # print(111)
            # 提取生成答案的最后一句
            sentences = data.split(".")
            # print("sentences:",sentences)
            if len(sentences)<=2:

                last_sentence = sentences[-1]
            else:
                last_sentence = sentences[-2]
            # print("last_sentence:",last_sentence)
            last_sentence = last_sentence.strip()
            last_sentence=last_sentence.replace("Answer", "").replace("Therefore", "")
            last_sentence=last_sentence.replace(".","").replace(",","")
            last_sentence = last_sentence.replace(":", "")
            return last_sentence



def Output(out_method=None):
    if out_method=="answer_abstract":
        return answer_abstract()
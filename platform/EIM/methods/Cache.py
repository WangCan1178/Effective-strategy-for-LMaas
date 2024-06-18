import time
from EIM_model.Util import Method, div_file
from gptcache import cache
from gptcache.adapter import openai
from gptcache.embedding import Onnx
from gptcache.manager import CacheBase, VectorBase, get_data_manager
from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation

import os

def response_text(openai_resp):
    return openai_resp['choices'][0]['message']['content']

class exactCache(Method):
    @staticmethod
    def process(query):
        os.environ["OPENAI_API_KEY"] = "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"
        cache.init()
        cache.set_openai_key()
        # ----------------------------------
        start_time=time.time()
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'user',
                    'content': query
                }
            ],
        )
        consuming=time.time()-start_time
        print("consuming:", consuming)
        if consuming>1.0:
            flag=True
        else:
            flag=False
        return flag,response_text(response)


class similarCache(Method):
    @staticmethod
    def process(query):
        os.environ["OPENAI_API_KEY"] = "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"
        onnx = Onnx()
        data_manager = get_data_manager(CacheBase("sqlite"), VectorBase("faiss", dimension=onnx.dimension))
        cache.init(
            embedding_func=onnx.to_embeddings,
            data_manager=data_manager,
            similarity_evaluation=SearchDistanceEvaluation(),
        )
        cache.set_openai_key()

        # --------------------------------
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'user',
                    'content': query
                }
            ],
        )
        consuming = time.time() - start_time
        print("consuming:",consuming)
        if consuming>1.5:
            flag=True
        else:
            flag=False
        return flag, response_text(response)



def Cache(cache_method=None):
    if cache_method == "exactCache":
        return  exactCache()
    elif cache_method == "similarCache":
        return similarCache()
    # else:
    #     print("Cache类型错误！！！")


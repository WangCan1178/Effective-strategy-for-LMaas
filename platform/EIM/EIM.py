import json
# from methods import Cache, Input, Output, Solution
from EIM_model.methods import Cache,Input,Output,Solution
from Util import save_json
class EIM:
    def  __init__(self, input_method=None, cache_method=None, solution_method=None, output_method=None,input=None,input_file="../files/input.txt"):
        self.input_method = Input.Input(input_method)
        self.cache_method = Cache.Cache(cache_method)
        self.solution_method = Solution.Solution(solution_method)
        self.output_method = Output.Output(output_method)
        self.input = input
        self.data = input
        self.input_file=input_file
        print("Input:",self.input)
        print("Input Method:", self.input_method)
        print("Cache Method:", self.cache_method)
        print("Solution Method:", self.solution_method)
        print("Output Method:", self.output_method)
        # print("Data:",self.data)


    def save_file(self, input_file, method_name, data):
        file_name, append = input_file.rsplit(".", 1)
        newfile_name = f"{file_name}_{method_name}.{append}"
        self.input_file = newfile_name
        with open(newfile_name, 'w') as file:
            file.write(data)

    def process(self):
        # 输入处理
        result={}
        # result["totle_method"]=""
        result["data"]=self.data
        # ----------------Input--------------------------
        if self.input_method:
            result_input=self.input_method.process(self.data)
            if result:
                # self.save_file(self.input_file, str(self.input_method), result_input)
                # 更新totle_method
                mid_method=str(self.input_method)
                result["totle_method"]=mid_method
                # 保存输入优化结果
                result[str(self.input_method)] = result_input
            else:
                print("result_input is None")
        else:
            mid_method="Input_None"

            result["totle_method"] = mid_method
            print("Input pass!!!")

        # ----------------Cache--------------------------
        if self.cache_method:
            flag,result_cache=self.cache_method.process(self.data)
            result_cache=result_cache.replace("\n", "")
            # 更新totle_method
            pre_method=result["totle_method"]
            mid_method=f"{pre_method}→{str(self.cache_method)}"
            result["totle_method"] = mid_method
            # 保存数据缓存结果
            result["cache_flag"]=flag
            result[str(self.cache_method)]=result_cache
        else:
            tip="Cache_None"
            pre_method = result["totle_method"]
            mid_method = f"{pre_method}→{tip}"
            result["totle_method"] = mid_method
            print("Cache pass!!!")

        # ----------------Solution--------------------------
        if self.solution_method:
            keys=list(result.keys())
            third_key=keys[2]
            print("third_key:",third_key)
            tip, model, cost,answer=self.solution_method.process(result[third_key])
            # answer=answer.replace("\n", "")
            # 更新totle_method
            pre_method = result["totle_method"]
            mid_method=f"{pre_method}→{str(self.solution_method)}"
            result["totle_method"] = mid_method
            # 保存级联结果
            result["solution_tip"]=tip
            result["solution_model"]=model
            result["solution_cost"]=cost
            result["solution_result"]=answer
        else:
            tip = "Solution_None"
            pre_method = result["totle_method"]
            mid_method = f"{pre_method}→{tip}"
            result["totle_method"] = mid_method
            print("Solution pass!!!")

        # ----------------output--------------------------
        if self.output_method:
            result_values = list(result.values())
            if result['solution_tip']==None:
                result_output = self.output_method.process(result_values[4])
            else:
                if result['cache_flag'] == False:
                    result_output = self.output_method.process(result_values[4])
                else:
                    result_output = self.output_method.process(result['solution_result'])
            # 更新totle_method
            pre_method = result["totle_method"]
            mid_method = f"{pre_method}→{str(self.output_method)}"
            result["totle_method"] = mid_method
            # 保存输出优化结果
            result["output"]=result_output
        else:
            tip = "Output_None"
            pre_method = result["totle_method"]
            mid_method = f"{pre_method}→{tip}"
            result["totle_method"] = mid_method
            print("Solution pass!!!")

        file="D:\\Python\\PythonProject\\upload\\EIM_proj\\EIM_model\\files\\result.json"
        save_json(file,result)

        return result



        # for method in [self.input_method, self.cache_method, self.solution_method, self.output_method]:
        #     if self.input == None:
        #         if method:
        #             # print(method)
        #             self.data = method.process(self.data)
        #             self.save_file(self.input_file, str(self.input_method), self.data)
        #             result[method]=self.data
        #     else:
        #         if method:
        #             self.data=method.process(self.data)
        #             # 保存json
        #             result[method] = self.data
        # return result
        # 结果评估

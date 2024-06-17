import streamlit as st

import sys
sys.path.append("D:\\Python\\PythonProject\\EIM_proj")
sys.path.append("D:\\Python\\PythonProject\\EIM_proj\\EIM_model")
sys.path.append("D:\\Python\\PythonProject\\EIM_proj\\EIM_model\\files")
from EIM_model import EIM
from EIM_model.Util import div_file

# 设置页面，加载session
def init_page():
    st.set_page_config(
        page_title="My_services",
        page_icon="❤️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("""
        <style>
            .stButton .edgvbvh10 {
                background-color: #e8d8ff;
                border: 0px solid transparent;
                margin:0px 0px 0px 0px;
            }

            .stButton .edgvbvh10:hover {
                background-color:#f2e6ff;
            }

            .stDownloadButton .edgvbvh10 {
                background-color: #A682FF;
                border: 1px solid #A682FF;
                margin:0px 0px 0px 0px;
            }
            .stDownloadButton .edgvbvh10 .e16nr0p34{
                color: #FFFFFF;
            }
            .stDownloadButton .edgvbvh10:hover {
                background-color: #9166FF;
                border: 1px solid #9166FF;
                margin:0px 0px 0px 0px;
            }

        </style>
        """, unsafe_allow_html=True)

    # if "model" not in st.session_state:
    #     st.session_state['model'] = AutoModelForSeq2SeqLM.from_pretrained('/data/wangcan/T5/model-t5-base/checkpoint-75000')
    # if "tokenizer" not in st.session_state:
    #     st.session_state['tokenizer'] = AutoTokenizer.from_pretrained('/data/wangcan/T5/model-t5-base/checkpoint-75000')
    # if "now_id" not in st.session_state:
    #     st.session_state["now_id"] = 0





init_page()
st.markdown('''
    ### Using platform
    ''')
# st.title("Using platform")
# option = st.sidebar.checkbox("上传文件")
page = st.selectbox("Supports text-based dialogue and file upload services.：", ["Text-based dialogue", "Upload file"])


def get_description(option):
    descriptions = {
        "prompt_reducer":"Text input can be optimized by tokenization and stemming to effectively reduce the number of tokens when using the GPT model.",
        "gptrim":"The NLTK library provides various text preprocessing tools, including text cleaning, text normalization, and tokenization, for optimizing text processing.",
        "selectiveContext": "Utilizing self-information to filter out low-information content, thereby improving efficiency in fixed context length.",
        "exactCache": "Exact search involves searching for an exact match of a query in the cache repository.",
        "similarCache": "Semantic search involves searching for similar queries in the cache repository.",
        "cost_priority": "Model routing：cohere_command→openai_gpt4→ai21_j2grande。",
        "responce_priority": "Model routing：cohere_command→ai21_j2grande→openai_gpt4。",
        "right_priority": "Model routing：openai_gpt4→ai21_j2grande→cohere_command。",
        "answer_abstract": " Can assist you in extracting key answers from the generated content.",
    }
    return descriptions.get(option, "Please select an option.")


# @st.cache
# def service(input_method, cache_method, solution_method, output_method, input):
#     eim = EIM(input_method=input_method, cache_method=cache_method, solution_method=solution_method,
#               output_method=output_method,
#               input=input)
#     # eim=EIM_model(input_method=option_1, cache_method=None, solution_method=None, output_method=None, input=query, input_file=None, input_set=None)
#     result = eim.process()
#     return result


if page == "Upload file":
    # select, process =  st.columns(2)
    # with select:
    # 创建五个下拉框和对应的文本内容
    with st.container():
        st.markdown("##### Input Abstract")
        option_1 = st.selectbox("Input Abstract", ["prompt_reducer", "gptrim","selectiveContext"], label_visibility="collapsed")
        st.write(get_description(option_1))
    st.empty()

    with st.container():
        st.markdown("##### Semantic Cache ")
        option_2 = st.selectbox("Please select an option.", ["exactCache", "similarCache"], label_visibility="collapsed")
        st.write(get_description(option_2))
    st.empty()

    with st.container():
        st.markdown("##### Solution Design ")
        option_3 = st.selectbox("Please select an option.", ["cost_priority", "responce_priority", "right_priority"], label_visibility="collapsed")
        st.write(get_description(option_3))
    st.empty()

    with st.container():
        st.markdown("##### Output Enhancement ")
        option_4 = st.selectbox("Please select an option.", ["answer_abstract"], label_visibility="collapsed")
        st.write(get_description(option_4))
    st.empty()

    with st.container():
        st.markdown("##### Select File")
        # option_1 = st.selectbox("File Format", ["txt", "json"], label_visibility = "collapsed")
        uploaded_file_1 = st.file_uploader("Upload file", type=['txt', 'csv', 'pdf'], label_visibility="collapsed")
    st.empty()
    if uploaded_file_1 is not None:
        file_content = uploaded_file_1.read().decode("utf-8")
        with st.chat_message("user"):
            st.write("The text content is：")
            for query in div_file(file_content):
                st.write(query)


    button_sub = st.button("Submit",use_container_width=True)
    if button_sub:
        for query in div_file(file_content):
            query = query.strip()
            eim = EIM.EIM(input_method=option_1, cache_method=option_2, solution_method=option_3,
                          output_method=option_4,
                          input=query, input_file=None)
            result = eim.process()
            result_keys = list(result.keys())
            result_values = list(result.values())
            with st.chat_message("assistant"):
                st.write("The service composition mode ：", result_values[1])
                st.write("The result after input optimization：", result_values[2])
                if result['solution_tip']==None and result['cache_flag']==True:
                    st.write("No answer found in the data cache, using cascading models：", option_3)
                    st.write("Calling model：gpt-4-0613")
                    st.write("Result：", result_values[4])
                    st.write("The result of answer extraction ：", result['output'])
                elif result['solution_tip']==None and result['cache_flag']==False:
                    st.write("Similar question found in the data cache.，")
                    # st.write("调用模型：gpt-4-0613")
                    st.write("Result：", result_values[4])
                    st.write("The result of answer extraction ：", result['output'])
                else:
                    if result['cache_flag'] == False:
                        st.write("Answer found in the data cache! The result is:", result_values[4])
                        st.write("The result of answer extraction ：", result['output'])
                    else:
                        st.write("No answer found in the data cache, using cascading models.：", option_3)
                        st.write(result['solution_tip'], "    Calling the model：", result['solution_model'])
                        st.write("Result：", result['solution_result'])
                        st.write("The total cost of the cascading models is", result['solution_cost'])
                        st.write("he result of answer extraction ：", result['output'])

                st.divider()




else:
    with st.container():
        st.markdown("##### Input Abstract")
        option_1 = st.selectbox("Input Abstract", ["prompt_reducer", "gptrim","selectiveContext"], label_visibility="collapsed")
        st.write(get_description(option_1))
    st.empty()

    with st.container():
        st.markdown("##### Semantic Cache ")
        option_2 = st.selectbox("Please select an option.", ["exactCache", "similarCache"], label_visibility="collapsed")
        st.write(get_description(option_2))
    st.empty()

    with st.container():
        st.markdown("##### Solution Design ")
        option_3 = st.selectbox("Please select an option.", ["cost_priority", "responce_priority", "right_priority"], label_visibility="collapsed")
        st.write(get_description(option_3))
    st.empty()

    with st.container():
        st.markdown("##### Output Enhancement ")
        option_4 = st.selectbox("Please select an option.", ["answer_abstract"], label_visibility="collapsed")
        st.write(get_description(option_4))
    st.empty()

    # st.write("")
    query = st.text_area(label="Please enter your question.", max_chars=1000)
    buttom = st.button("Submit",use_container_width=True)
    if buttom:
        # eim = EIM_model(input_method=option_1, cache_method=None, solution_method=None, output_method=None, input=query=None, input_set=None)
        eim = EIM.EIM(input_method=option_1, cache_method=option_2, solution_method=option_3, output_method=option_4, input=query,
                      input_file=None)
        # EIM_model.testfun()
        result = eim.process()
        result_keys=list(result.keys())
        result_values=list(result.values())

        # ---------------------------显示结果--------------------------------
        if result['solution_tip'] == None and result['cache_flag'] == True:
            with st.chat_message("assistant"):
                st.write("The service composition mode is：", result_values[1])
                st.write("The result after input optimization：", result_values[2])
                st.write("No answer found in the data cache, using cascading models.", option_3)
                st.write("using model：gpt-4-0613")
                st.write("Result：", result_values[4])
                st.write("The result of answer extraction is：", result['output'])
        elif result['solution_tip'] == None and result['cache_flag'] == False:
            with st.chat_message("assistant"):
                st.write("The service composition mode is：", result_values[1])
                st.write("The result after input optimization：", result_values[2])
                st.write("Similar question found in the data cache!")
                # st.write("调用模型：gpt-4-0613")
                st.write("Result：", result_values[4])
                st.write("The result of answer extraction is：", result['output'])

        else:
            if result['cache_flag'] == False:
                st.write("The service composition mode is：",result_values[1])
                st.write("The result after input optimization：", result_values[2])
                st.write("Answer found in the data cache! The result is:：",result_values[4])
                st.write("The result of answer extraction is：",result_values[9])
            else:
                st.write("The service composition mode is：",result_values[1])
                st.write("The result after input optimization：", result_values[2])
                st.write("No answer found in the data cache!")
                st.write("using cascading models：",option_3)

                text_1 = result['solution_model'] + "  :  " + result['solution_result']
                text_2 = "Explanation：" + result['solution_tip'] + "so use" + result['solution_model']
                text_3 = "     The total cost of the cascading models is：" + str(result['solution_cost'])
                st.write('<div style="background-color: #DCDCDC; padding: 10px;">',
                         text_1, unsafe_allow_html=True)
                st.write('<div style="background-color: #DCDCDC; padding: 10px;">',
                         text_2, unsafe_allow_html=True)
                st.write('<div style="background-color: #DCDCDC; padding: 10px;">',
                         text_3, unsafe_allow_html=True)

                st.write("The result of answer extraction is：",result_values[9])
                st.write("The current query has been successfully stored in the cache repository.")

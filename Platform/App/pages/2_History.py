import streamlit as st
import json

def init_page():
    st.set_page_config(
        page_title="Rerformance evaluation",
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

init_page()
st.markdown('''
    ### Transcript of historical conversations
    ''')
# st.title("Transcript of historical conversations ")

# 将历史对话信息储存下来
if "history" not in st.session_state:
    st.session_state.history = []

# 显示历史信息
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# input_file = "..\files\data.json"
# with open(r"..\files\data.json", 'r') as file:
with open(r"D:\Python\PythonProject\upload\EIM_proj\EIM_model\files\result.json", 'r',encoding='utf-8') as file:
    data = json.load(file)
    length=len(data)
    for i in range(length-1,-1,-1):
        with st.chat_message("user"):
            st.markdown(data[i]['date'])
            st.markdown(data[i]['data'])

        with st.chat_message("assistant"):
            st.markdown(data[i]['totle_method'])
            if data[i]['solution_result']==None:
                sample=data[i]
                sample_values=list(sample.values())
                st.markdown(sample_values[4])
            else:
                st.markdown(data[i]['solution_result'])
        st.divider()

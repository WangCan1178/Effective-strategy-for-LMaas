import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="auto",
)

# tab1, tab2 = st.columns(2)
# with tab1:
st.write("# Welcome to Effective-strategy-for-LMaas platform!")

# st.sidebar.success("Select a demo above.")
st.markdown(
    """
    This website is an open-source website built by Streamlit. 
    It integrates current advanced optimization methods, including input optimization, data caching, model cascading, and output enhancement, based on different optimization stages. 
    You can freely combine your service optimization framework on this website and interact with large models.^_^

    **👈 Switching tabs from the sidebar** to see  of what Streamlit can do!
    ### Want can you do?
    - View detailed descriptions of the optimization methods provided by this system,which in the "introduction" tab
    - Engaging in conversation with the LLM via the dialogue box, and this function in the "Services" tab
    - Engaging in conversation with the LLM via uploading a txt format file, and this function also in the "Services" tab
    - View the history of conversation records,which in the "history" tab

    ### See more information!
    - Methods and experiments about thr paper provided to show details, visit by clicking the "introduction" tab
    - The project is open source on github at [https://github.com/W-caner/Effective-strategy-for-LMaas](https://github.com/W-caner/Effective-strategy-for-LMaas)

    # [GETTING START NOW!](http://localhost:8501/Service)
"""
)

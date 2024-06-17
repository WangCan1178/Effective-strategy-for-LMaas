import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="auto",
)



# 创建一个占据整个页面宽度的空白区域
st.markdown('''
    ### Effective invocation methods
    ''')
# st.title("Effective invocation methods")
page = st.selectbox(" ", ["Effective Invocation Method", "Input Abstract", "Semantic Cache", "Solution Design",
                          "Output Enhancement"])

# 根据选择的页面显示不同的内容
if page == "Semantic Cache":
    st.markdown(
        ''' 
        **Caching is a common computer technique used to temporarily store the results of computations or data. Its primary purpose is to improve access speed and performance by reducing redundant work on original data or computations, thereby reducing system response time. In the development of language models, caching plays a significant role in accelerating computations and other aspects. Currently, commonly used data caching methods include traditional caching and neural caching. This system provides two methods, semantic search and absolute search, implemented through traditional caching.**
        ##### Traditional caching：
        Currently, the paradigm of this caching method consists of three components: the cache manager, similarity evaluator, and post-processor. The cache manager is responsible for storing content, typically in the form of question-answer key-value pairs, selecting an appropriate storage method, and managing eviction. The similarity evaluator is used to determine if the cached answer matches the input query. The post-processor organizes the final response to be returned to the user. It adjusts the randomness of the response based on the requested parameters. If a similar response is not found in the cache, the post-processor forwards the request to the LLM to generate a response, which is then stored in the cache.
        ''')
    image_1 = "D:\\Python\\PythonProject\\EIM_proj\\App\\files\\Cache_1.png"
    st.image(image_1, caption='Framework of Traditional Cache')
    st.markdown(
        ''' 
        ##### Neural caching：
        Neural caching is a caching system that utilizes neural networks or deep learning models to learn and store data representations. Its applications are primarily focused on fields such as natural language processing (NLP) and computer vision, where it is used to learn and store complex semantic representations.
        ''')
elif page == "Input Abstract":
    st.markdown(
        ''' 
        **Input optimization primarily involves preprocessing data, such as cleaning, tokenization, and segmentation, to ensure its suitability for the inference process of large-scale language models. By employing techniques such as input format optimization and data augmentation, it is possible to meet the requirements of low latency, high quality, and cost-effectiveness, thereby maximizing the potential of large-scale language models in service delivery. This platform provides three different methods, namely Prompt_Reduce, Gptrim, and Selective, to achieve input optimization.**
        ##### Prompt_Ruduce：
        Text input can be optimized by tokenization, stemming, and removing whitespace to effectively reduce the number of tokens when using the GPT model.
        ##### Gptrim：
        The NLTK library provides various text preprocessing tools, including text cleaning, text normalization, and tokenization, for optimizing text processing.
        ##### Selective：
        Utilizing self-information to filter out low-information content, thereby improving efficiency in fixed context length.
        ''')
elif page == "Effective Invocation Method":
    st.markdown(
        '''
        Language Model as a Service (LMaaS) enables users to accomplish tasks without the need for specialized knowledge, simply by paying the service provider. 
        However, the existing large-scale Language Models (LLMs) services vary in terms of latency, performance, and pricing. 
        Therefore, **this platform has comprehensively organized the LLM invocation strategies.** 
        The LLM invocation framework provided by this platform integrates existing methods across different optimization stages, including input abstraction, semantic caching, model cascading, and output enhancement.
        '''
    )
    image_2 = "D:\\Python\\PythonProject\\upload\\EIM_proj\\App\\files\\framework.png"
    st.image(image_2, "Framework of Effective Invocation Method")

elif page == "Output Enhancement":
    st.markdown(
        '''
        Once the input and LLM service integration solution is determined, the answer obtained for a particular call remains fixed. Answer guidance still relies on techniques that consider the context, but the emphasis is on using methods to condense tokens and aggregate answers for improved accuracy.
        '''
        '''
        The answer extraction methods provided by this system can assist you in quickly obtaining key answers from generated sentences, simplifying the inference process.
        '''
        '''
        ##### example:
        '''
    )
    st.text_area('Sentence generated by GPT-4：',
                 "The king cab upgrade is $7,500.Leather seats are one-third the cost of the king cab upgrade, so they are $7,500 / 3 = $2,500.Running boards are $500 less than the leather seats, so they are $2,500 - $500 = $2,000.The upgraded exterior lightpackage is $1,500.Adding up all the extra features, the total cost of the truck is $7,500 + $2,500 + $2,000 + $1,500 = $13,500.Adding the base price of the truck to the cost of the extra features gives a total cost of $30,000 + $13,500 = $43,500.Therefore, the total cost of Bill's new truck is $43,500.",
                 height=130)
    st.markdown(
        '''
        **Result after answer extraction:** 43500
        '''
    )


else:
    st.markdown(
        '''
        Model cascading is an approach to utilizing large-scale language model services with heterogeneous costs and performance. It considers different query scenarios and objectives and dynamically selects the most suitable LLM API based on the available information, providing a flexible and efficient solution. The construction of the solution involves two main factors: the scoring function, which reflects the performance of each LLM service based on the query and available LLM services, and the router, which implements dynamic API selection and query routing based on the results generated by the scoring function.
        '''
    )
    st.markdown(
        '''
        This system utilizes DistilBert as the scorer and trains models using the datasets: 'gsm8k', 'legalbench', 'math', 'med_qa', and 'mmlu'. The models cohere_command, ai21_j2grande, and openai_gpt4 are evaluated sequentially for their performance on different tasks.
        Regarding the determination of the router, this system utilizes multi-objective optimization to train the cascading paths. Ultimately, it provides different cascading routes based on the specific needs of the user.
        '''
        '''
        **cost_priority：** cohere_command→openai_gpt4→ai21_j2grande
        '''
        '''
        **responce_priority：** cohere_command→ai21_j2grande→openai_gpt4
        '''
        '''
        **right_priority：** openai_gpt4→ai21_j2grande→cohere_command
        '''
    )

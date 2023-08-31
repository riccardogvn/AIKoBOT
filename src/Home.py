import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="AIKoBOT 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[riccardogvn/AIKoBOT](https://github.com/riccardogvn/AIKoBOT)")



    st.write("**X:** [@Riccardo_G](https://twitter.com/Riccardo_G)")
    st.write("**Mail** : riccardogiovanelli.mail@gmail.com")
    st.write("**Originally created by Yvann, updated and changed by Riccardo Giovanelli**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>AIKoBOT, data assistant for Tradie in Antiquities Market 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>AIKoBOT is a chatbot which combinines Langchain, ChatGPT and Streamlit. 
    It uses large language models to provide context-sensitive interactions based on your data. 
    It supports PDF, TXT, CSV, JSON and Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 AIKoBOT pages")
st.write("""
- **AIKoBOT_chat**: General Chat on data (PDF, TXT,CSV, JSON) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **AIKoBOT_sheet** (beta): Chat on tabular data (CSV, XLXS, JSON) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **AIKoBOT_Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")







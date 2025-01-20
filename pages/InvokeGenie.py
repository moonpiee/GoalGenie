import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import execjs
import streamlit.components.v1 as components #allows var height for whole graph view

st.set_page_config("Goal Genie🧞🪄",initial_sidebar_state="collapsed")

def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true, theme:'default', scale:1.5 }});
        </script>
        """,
        height=st.session_state["svg_height"] + 200,
    )

if "svg_height" not in st.session_state:
    st.session_state["svg_height"] = 500 

st.markdown(
        """
        ##### Hello Master! 👋 I'm Your **GoalGenie** 🧞🪄
        ##### Have a wish or goal? 🤔 Tell me! 📝 Be it easy or difficult, I'll weave the path and You make your move!
        ##### Let's get started! 🎉 
        """
    )
# st.write("I'm Your GoalGenie🧞. I weave a path to you to make your dreams a reality💫💫 \nWhat is that you want to achieve today?")
llm_client = ChatGroq(
        api_key = st.secrets["GROQ_API_KEY"],
        model = "llama-3.1-70b-versatile", #st.secrets["default_model"]
        temperature = 0.5
    )
user_inpt = st.text_input("What's your heart's desire? ❤️")
#     6. You can use different colors, fonts, and shapes to make the flowchart more engaging and effective.
prompt = f"""
    You are a solutions specialist and mermaid.js LR charts coder. 
    Create a flowchart that represents the user goal: {user_inpt}. 
    You must abide by the below rules:
    1. The flowchart should have realistic, creative, possible solutions in an organised, structured way.
    2. Be clear, Use good readable combination of colors for background and text and visually appealing elements for flowchart. Address sentence in 1st person (I)
    3. Use flowchart type, elements, shape, colors by analysing user goals briefly
    4. Only output the working, error-free mermaid code of flowchart, Nothing other tha this. Be careful of spaces, proper indentation etc.,
    5. Give only production ready mermaid code. Give only code from GRAPH LR. Exclude any other tags.
    Sample: 
    user goal: I want to have fun. I can play game or cook or sleep or cry and not have fun at all.
    response: graph LR;
    id1(I Want to Have Fun) --> |Yes| id2(Do I want to play?)
    id2 -->|Yes| id3(Play Game)
    id2 -->|No| id4(Do I want to read?)
    id4 -->|Yes| id5[Read Book]
    id4 -->|No| id6(Do I want to cook?)
    id6 -->|Yes| id7[Cook]
    id6 -->|No| id8(Do I want to relax?)
    id8 -->|Yes| id9[Sleep]
    id8 -->|No| id10(Do I want to do something casual?)
    id10 -->|Yes| id11[Scroll]
    id10 -->|No| id12[Sit]
    id1 -->|No| id13[Cry and not have fun]
    style id1 fill:#FFECB3,stroke:#000000,stroke-width:2px;
    style id2 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
    style id3 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id4 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
    style id5 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id6 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
    style id7 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id8 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
    style id9 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id10 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
    style id11 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id12 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
    style id13 fill:#FFCDD2,stroke:#000000,stroke-width:2px,color:#000000;
    linkStyle default stroke:#FF00FF,stroke-width:1px;
    classDef default font-family:'Arial',sans-serif,font-size:14px;
    """
    
evaluate_prompt = f"""
    Output only the corrected code, remove any syntax errors and re verify the mermaid code without including ```mermaid and ```:{user_inpt}
    """
    
    # msgs = [
    #     ("system",prompt),
    #     ("human","hi")
    # ]
template = ChatPromptTemplate( #removed from_messages
            [
            ("system","{sys_prompt}"),
            ("human","{user_inpt}") #should include "" since it needs formattii g
            ]
        )
    
if user_inpt: #by default this wont be none but empty string
    with st.spinner("Genie Thinking..."):
        chain = template | llm_client #chain the llm model and prompt template
        #invoke llm by passing user input
        resp = chain.invoke({"sys_prompt":prompt, "user_inpt":user_inpt})
        # st.markdown(resp.content)
        # print(resp.content)
        #display resp
        final_code = resp.content.split("mermaid")[-1].replace("```","")
        print(final_code)
        st.write("Here's your map 🗺️")
        #evaluate the mermaid code-> here i used evaluatiion by llm to make code error proof, didnt achieve with prompt engineering due to synatx errors issues.
        eval = chain.invoke({"sys_prompt":evaluate_prompt, "user_inpt":final_code})
        eval_code = eval.content
        print(eval_code)                   
        mermaid(eval_code)





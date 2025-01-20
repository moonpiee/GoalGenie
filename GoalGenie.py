import streamlit as st
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import execjs
import streamlit.components.v1 as components #allows var height for whole graph view

st.set_page_config(page_title="Goal Genie🧞🪄",initial_sidebar_state="collapsed", page_icon="🧞")

def mermaid(code: str) -> None:
    components.html(
        f"""
        <style>
        .mermaid {{
            max-width: 100%;
            max-height: 100%
            overflow: auto;
        }}
        .mermaid text {{
            font-size: 14px;
            font-family: Arial, sans-serif;
        }}
        </style>
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
        </script>
        """,
        height=st.session_state["svg_height"] + 20,
    )

if "svg_height" not in st.session_state:
    st.session_state["svg_height"] = 20 

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
    3. Use flowchart type(TB), elements, shape, colors by analysing user goals briefly
    4. Only output the working, error-free mermaid code of flowchart, Nothing other tha this. Be careful of spaces, proper indentation etc., Follow the sample given.
    5. Give only production ready mermaid code. Give only code from GRAPH LR. Exclude any other tags.
    Sample: 
    user goal: I want to have fun. I can play game or cook or sleep or cry and not have fun at all.
    response: graph TB;
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
        # final_code = resp.content.split("mermaid")[-1].replace("```","")
        # print(final_code)
        st.write("Here's your map 🗺️") #errors were resolved by prompt engineering(steps) and mainly few shot prompting(structure and layout!!!)
        #evaluate the mermaid code-> here i used evaluatiion by llm to make code error proof, didnt achieve with prompt engineering due to synatx errors issues.
        # eval = chain.invoke({"sys_prompt":evaluate_prompt, "user_inpt":final_code})
        # eval_code = eval.content
#         eval_code="""
# graph TB;
#     id1(I Want to Sleep) --> |Yes| id2(Am I Tired?)
#     id2 -->|Yes| id3(Go to Bed)
#     id2 -->|No| id4(Do I need to Relax?)
#     id4 -->|Yes| id5[Meditate]
#     id4 -->|No| id6(Do I want to Wind Down?)
#     id6 -->|Yes| id7[Read a Book]
#     id6 -->|No| id8(Do I want to Take a Warm Bath?)
#     id8 -->|Yes| id9[Take a Bath]
#     id8 -->|No| id10(Do I want to Listen to Soothing Music?)
#     id10 -->|Yes| id11[Listen to Music]
#     id10 -->|No| id12(Do I want to Try Progressive Muscle Relaxation?)
#     id12 -->|Yes| id13[Relax Muscles]
#     id12 -->|No| id14[Try Aromatherapy]
#     id1 -->|No| id15[Stay Awake]
#     style id1 fill:#FFECB3,stroke:#000000,stroke-width:2px;
#     style id2 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id3 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id4 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id5 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id6 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id7 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id8 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id9 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id10 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id11 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id12 fill:#C8E6C9,stroke:#000000,stroke-width:2px;
#     style id13 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id14 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id15 fill:#FFCDD2,stroke:#000000,stroke-width:2px,color:#000000;
#     linkStyle default stroke:#FF00FF,stroke-width:1px;
#     classDef default font-family:'Arial',sans-serif,font-size:14px;
#     """
        # print(eval_code)                   
        # mermaid(eval_code)
        mermaid(resp.content)





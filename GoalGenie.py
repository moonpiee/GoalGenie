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
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=st.session_state["svg_height"] + 50,
    )
st.markdown("""## Goal Genie🧞🪄: The Genie That Weaves Your Path 🌟""")
st.divider()
st.markdown(
    """
    <style>
    .left {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 40vh;
    }
    .zoom {
        transition: transform 0.2s; /* Animation */
        border: none; /* Remove default button border */
        padding: 0; /* Remove default button padding */
        background: none; /* Remove default button background */
    }
    .zoom img {
        width: 500px; /* Set width of the GIF */
        height: 300px; /* Set height of the GIF */
        object-fit: cover; /* Ensure the GIF covers the entire button area */
    }
    .zoom:hover {
        transform: scale(1.05); /* Zoom in by 5% */
        content: "Awake Your Genie"; /* Replace with your desired text */

    }
    .zoom:hover::after {
        content: "Tap to Awake Your Genie!"; /* Replace with your desired text */
        position: absolute;
        top: 70%;
        left: 80%;
        transform: translate(-50%, -50%);
        background-color: rgba(0, 0, 0, 0.7); /* Background color for the text */
        color: #ffffff; /* Text color */
        padding: 5px 10px; /* Padding around the text */
        border-radius: 5px; /* Rounded corners for the text box */
        white-space: nowrap; /* Prevent text from wrapping */
        z-index: 1; /* Ensure the text is above the image */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="center">
        <a href="InvokeGenie" target="_self">
            <button class="zoom">
                <img src="https://cdn.dribbble.com/users/1738955/screenshots/16211496/media/9d492e5cdf06019762921c57535fba7c.gif" alt="GIF Button">
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# print("hello chandana")

# row1=st.empty()
# row1col1=row1.col(width=100)
# col1, col2, col3=st.columns([3,1,1])
# with row1col1:
# lamp_clck = st.button("![Click Here](https://cdn.dribbble.com/users/1738955/screenshots/16211496/media/9d492e5cdf06019762921c57535fba7c.gif)")

# if lamp_clck:
#     st.session_state["lamp_clck"]=1

# if "svg_height" not in st.session_state:
#     st.session_state["svg_height"] = 500 

# if "lamp_clck" in st.session_state:
#     st.markdown(
#         """
#         ### Welcome
#         # Hello Master! I'm Your **GoalGenie** 🧞
#         # I weave the paths to turn your **aspirations** into **achievements**, and your **goals** into **reality** 💫💫.
#         # Make a wish, and I'll chart the course to make it happen! 🗺️
#         """
#     )
    # st.write("Hello there!I'm Your GoalGenie🧞. I weave a path to you to make your dreams a reality💫💫 \nWhat is that you want to achieve today?")

#     llm_client = ChatGroq(
#         api_key = api_key,
#         model = "llama-3.1-70b-versatile",
#         temperature = 0.5
#     )
#     user_inpt = st.text_input("What is the goal you want to achieve?")
#     prompt = f"""
# You are a solutions specialist and mermaid.js LR charts coder. 
# Create a flowchart that represents the user goal: {user_inpt}. 
# You must abide by the below rules:
# 1. The flowchart should have realistic, creative, possible solutions in an organised, structured way.
# 2. Be clear, Use good readable combination of colors for background and text and visually appealing elements for flowchart. Address sentence in 1st person (I)
# 3. Use flowchart type, elements, shape, colors by analysing user goals briefly
# 4. Only output the working, error-free mermaid code of flowchart, Nothing other tha this. Be careful of spaces, proper indentation etc.,
# 5. Give only production ready mermaid code. Give only code from GRAPH LR. Exclude any other tags.
# 6. You can use different colors, fonts, and shapes to make the flowchart more engaging and effective.
# Sample: 
# user goal: I want to have fun. I can play game or cook or sleep or cry and not have fun at all.
# response: graph LR;
#     id1(I Want to Have Fun) --> |Yes| id2(Do I want to play?)
#     id2 -->|Yes| id3(Play Game)
#     id2 -->|No| id4(Do I want to read?)
#     id4 -->|Yes| id5[Read Book]
#     id4 -->|No| id6(Do I want to cook?)
#     id6 -->|Yes| id7[Cook]
#     id6 -->|No| id8(Do I want to relax?)
#     id8 -->|Yes| id9[Sleep]
#     id8 -->|No| id10(Do I want to do something casual?)
#     id10 -->|Yes| id11[Scroll]
#     id10 -->|No| id12[Sit]
#     id1 -->|No| id13[Cry and not have fun]
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
#     style id12 fill:#B3E5FC,stroke:#000000,stroke-width:2px,color:#000000;
#     style id13 fill:#FFCDD2,stroke:#000000,stroke-width:2px,color:#000000;
#     linkStyle default stroke:#000000,stroke-width:1px;
#     classDef default font-family:'Arial',sans-serif,font-size:14px; 
# """
    
#     evaluate_prompt = f"""
#     Output only the corrected code, remove any syntax errors and re verify the mermaid code without including ```mermaid and ```:{user_inpt}
#     """
    
#     # msgs = [
#     #     ("system",prompt),
#     #     ("human","hi")
#     # ]
#     template = ChatPromptTemplate( #removed from_messages
#         [
#         ("system","{sys_prompt}"),
#         ("human","{user_inpt}") #should include "" since it needs formattii g
#         ]
#     )
    
#     if user_inpt: #by default this wont be none but empty string
#         chain = template | llm_client #chain the llm model and prompt template
#         #invoke llm by passing user input
#         resp = chain.invoke({"sys_prompt":prompt, "user_inpt":user_inpt})
#         # st.markdown(resp.content)
#         # print(resp.content)
#         #display resp
#         st.write("Flowchart:")
#         final_code = resp.content.split("mermaid")[-1].replace("```","")
#         print(final_code)

#         #evaluate the mermaid code-> here i used evaluatiion by llm to make code error proof, didnt achieve with prompt engineering due to synatx errors issues.
#         eval = chain.invoke({"sys_prompt":evaluate_prompt, "user_inpt":final_code})
#         eval_code = eval.content
#         print(eval_code)                   
#         mermaid(eval_code)





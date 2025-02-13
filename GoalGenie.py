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

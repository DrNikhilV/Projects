import streamlit as st
import g4f

# Set the page layout
st.set_page_config(page_title="ChatGPT", layout="wide")

# Custom CSS for styling the text input
st.markdown(
    """
    <style>
    /* Style the text input */
    .stTextInput {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        outline: none;
        transition: box-shadow 0.3s ease;
        resize: none; /* Prevent resizing */
        font-size: 16px; /* Adjust font size */
    }
    .stTextInput:focus {
        box-shadow: 0 0 8px rgba(0,123,255,0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    st.title("Vaathi AI")
    st.header("Explore with us")
    st.markdown("Top questions")

    st.write("### STEM (Science, Technology, Engineering, Mathematics)")
    st.write("1. Median Half Hypothesis Proof: What is the median half hypothesis and how can it be proved mathematically?")
    st.write("2. Corrected Operations for Points: What are the corrected operations for handling points in mathematical computations?")

    # Programming
    st.write("### Programming")
    st.write("1. Index Error in List: How do you resolve an index error in a list in Python?")
    st.write("2. Python Code: Find List Size: How can you find the size of a list in Python?")
    st.write("3. Single Number Using HashMap: How can you find a single number in a list using a HashMap in Python?")

    # Operating Systems (OS) and Related Topics
    st.write("### Operating Systems (OS) and Related Topics")
    st.write("1. Approximate Inference in Bayesian PR: What is approximate inference in Bayesian probabilistic reasoning and how is it applied?")

    # Focus and Study Habits
    st.write("### Focus and Study Habits")
    st.write("1. Focus Issues: Causes & Tasks: What are the common causes of focus issues and what tasks can help improve focus?")
    st.write("2. Student Distraction: Causes & Solutions: What are the primary causes of student distraction and what are the effective solutions?")
        
    st.markdown("---")
    st.button("Upgrade plan", key="upgrade_button")

# Main content
st.title("Chat with Vaathi AI")

# Initialize session state for conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Create a text area for the user's question
question = st.text_area("Enter your question:", "", key="chat_input", height=80, max_chars=500)

if question:
    # Display the user's question
    st.session_state.conversation.append(('user', question))
    
    # Stream the response
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )
    
    response_text = ""
    for message in response:
        response_text += message
    
    st.session_state.conversation.append(('bot', response_text))
    
    # Clear the input box after processing
    st.text_area("Enter your question:", "", key="empty", height=80, max_chars=500)

# Display conversation history
for role, text in reversed(st.session_state.conversation):
    if role == 'user':
        st.markdown(f"<div style='background-color: #000; color: #fff; padding: 10px; border-radius: 10px;'><strong>You:</strong> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: #333; color: #fff; padding: 10px; border-radius: 10px;'><strong>GPT-3.5-turbo:</strong> {text}</div>", unsafe_allow_html=True)
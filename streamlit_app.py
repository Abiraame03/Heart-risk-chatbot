import streamlit as st
import google.generativeai as genai

# Set up Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini 1.5 Pro with system prompt
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="""
    You are a helpful and knowledgeable AI assistant that answers questions about heart disease and related risks.
    Provide clear, accurate, and concise medical information based on current research.
    Avoid giving personal medical advice—recommend consulting a doctor when necessary.
    """
)

# Start chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("❤️ Heart Risk Q&A Chatbot")
st.write("Ask any question about heart disease, symptoms, or prevention tips.")

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat.send_message(user_input)
    response = st.session_state.chat.last.text.strip()
    st.markdown(f"**Bot:** {response}")

# Display chat history
if st.button("Show Full Chat History"):
    st.markdown("### Chat History:")
    for turn in st.session_state.chat.history:
        st.markdown(f"**You:** {turn.parts[0].text}")
        st.markdown(f"**Bot:** {turn.parts[1].text}")

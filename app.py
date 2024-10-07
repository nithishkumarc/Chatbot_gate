import streamlit as st
import google.generativeai as genai

# Configure Gemini API using the environment variable for the API key
genai.configure(api_key="AIzaSyAsWdnkcKcxjhLx1XIr3qd9WbtczJP4vak")

# Set up the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

system_instruction = '''youre a GATE exam preparation bot for ECE department of Nandha Engineering College, 
You need to Answer All the gate related questions with answers and explanation, 
if the question is irrelevant to GATE exam reply with *Sorry, It doesn't seem like a GATE question.*'''

# Create the Generative Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction,
)

# Streamlit app
def main():
    st.title("GATE Exam Preparation Bot")
    st.write("Ask me anything about GATE preparation for the ECE department!")

    # Input message from the user
    user_message = st.text_input("Your question:")

    if st.button("Send"):
        if user_message:
            # Start a new chat session
            chat_session = model.start_chat(history=[])

            # Send the user message to the Gemini API and get the response
            response = chat_session.send_message(user_message)

            # Display the response
            st.write("Response:", response.text)
        else:
            st.warning("Please enter a question.")

if __name__ == '__main__':
    main()

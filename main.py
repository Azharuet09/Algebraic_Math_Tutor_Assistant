import openai
from dotenv import load_dotenv
import os
import streamlit as st
from constants import GPT_MODEL,SYSTEM_MESSAGE

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def solve_algebra_problem(prompt):
    """
    Function to solve algebra-related problems using Prompt Engineering.
    """
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_MESSAGE
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=500
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {e}"


st.title("Algebraic Math Tutor Assistant")
st.write("Enter your algebra problem below, and click 'Solve' to get step-by-step solutions.")

user_input = st.text_input("Enter your algebra problem:", "")

if st.button("Solve"):
    if user_input.strip():
        st.write("**Solving your problem...**")
        solution = solve_algebra_problem(user_input)
        st.write("### Solution and Explanation:")
        st.write(solution)
    else:
        st.error("Please enter a valid algebra problem.")

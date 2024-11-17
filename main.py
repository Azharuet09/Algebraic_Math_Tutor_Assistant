import openai
from dotenv import load_dotenv
import os
import streamlit as st
from constants import GPT_MODEL 

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
                    "content": (
                        "You are a highly specialized algebra tutor. Your task is to solve only algebra-related problems, such as equations, expressions, and related mathematical queries. "
                        "If the question is not algebra-related, politely respond with: 'I can only assist with algebra-related problems. Please ask an algebra question.' "
                        "Provide detailed step-by-step explanations for algebra problems."
                    )
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

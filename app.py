import streamlit as st
from openai import OpenAI

# Read API key from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Teacher's Lesson Plan Architect")

grade = st.selectbox("Select Grade", ["3", "5", "8", "10"])
subject = st.text_input("Enter Subject")
topic = st.text_input("Enter Topic")

if st.button("Generate Lesson Plan"):

    prompt = f"""
    Generate a structured 40-minute lesson plan for:
    Grade: {grade}
    Subject: {subject}
    Topic: {topic}

    Include:
    1. Learning Objectives
    2. 5-minute Introduction
    3. 15-minute Explanation
    4. 10-minute Activity
    5. 5 Quiz Questions with Answers
    6. Homework
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)

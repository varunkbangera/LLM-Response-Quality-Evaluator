import streamlit as st
from evaluator import evaluate

st.title("AI Output Quality Evaluator")

question = st.text_input("Enter the Question")
answer = st.text_area("Enter the AI Answer")

if st.button("Evaluate"):
    if not question.strip() or not answer.strip():
        st.error("Please enter both a question and an answer before evaluation.")
    else:
        result = evaluate(question, answer)
        st.subheader("Evaluation Result")
        st.json(result)

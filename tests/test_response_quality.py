import os
import sys
import pytest
import streamlit as st  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import utils
import rag
from rag import CONFIG


# Config Langsmith
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "test_response_quality"


def load_questions_from_file(filename="tests/user_question_list.txt"):
    with open(filename, "r") as file:
        questions = [line.strip() for line in file if line.strip()]
    return questions

questions = load_questions_from_file()

@pytest.mark.parametrize("question", questions)
def test_rag_pipeline_responses(question):

    response, enriched_question = rag.rag(question)
    print({question})
    print({response['answer']['answer']})
    # Assert the response is not empty
    assert response, f"Response for question '{question}' is empty."



# Run this test file with `pytest -s tests/test_response_quality.py` 

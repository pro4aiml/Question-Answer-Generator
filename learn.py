import json
import openai
from openai import OpenAI
from pydantic import BaseModel


class AnswerSchema(BaseModel):
    answer: str

class QuestionSchema(BaseModel):
    questions: list[str]


client = OpenAI()

prompt_template = """
You are a helpful assistant. Generate a question based on the following document content.
The question will be either a short factual question and a long complex reasoning question.

Document:
{text}

Answer only with a valid JSON object using the following format:
{{
    "questions": [
        "Generated question 1.",
        "Generated question 2.",
        "Generated question 3.",
    ]
}}
"""

Query = ""
model="gpt-4o-2024-08-06"
"""
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function.",
        },
        {
            "role": "user",
            "content": "look up all my orders in may of last year that were fulfilled but not delivered on time",
        },
    ],
    tools=[
        openai.pydantic_function_tool(Query),
    ],
)

print(completion.choices[0].message.tool_calls[0].function.parsed_arguments)
"""

def generate_questions(text):
    prompt = prompt_template.format(text)

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt }],
        temperature=1,
        top_p=0.9,
        max_tokens=4096,
        response_format=QuestionSchema
    )

    result = completion.choices[0].message.parsed
    return result.questions


def generate_answers(text, questions, model="llama3.2"):
    qa_generated = []

    prompt_template = """
        You are a helpful assistant. Provide a clearly articulated and phrased answer to the following question based on the following document content.
        The answer should include step-by-step reasoning followed by the final answer.

        Document:
        {text}

        Question:
        {question}

        Answer only with a valid JSON object in the following format:
        {{
            "answer": "Step by step reasoning followed by the answer."
        }}
    """


def disk_output(data, dir_out):
    def convert_to_jsonl(data, dir_out):
        with open("output.json", 'w') as f:
            for row in data:
                messages = [
                    {"role": "user", "content": row['question']},
                    {"role": "assistant", "content": row['answer']}
                ]
                json_schema = {"messages": messages}
                f.write(json.dumps(json_schema) + "\n")

    convert_to_jsonl(data, dir_out)
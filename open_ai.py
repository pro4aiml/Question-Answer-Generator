import os, json
from openai import OpenAI
from pydantic import BaseModel
from rich import print


client = OpenAI()
model="gpt-4o-2024-08-06"

class GenerateQA(BaseModel):
    question: str
    answer: str



def get_response(text):
  pass


def generate_questions(text):
    qnum = 3
    questions = []

    prompt_template = """
      You are a helpful assistant. Generate a list of 3 questions based on the following document content.
      The list should contain a mix of short factual questions and long complex reasoning questions.

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

    prompt = prompt_template.format(text=text)

    completion = client.beta.chat.completions.parse(
          model=model,
          messages=[{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt }],
          temperature=1,
          top_p=0.9,
          max_tokens=4096,
          response_format=GenerateQA
      )
    
    #r = completion.choices[0].message.content     
    r = completion.choices[0].message.parsed

    # for i in range(qnum):
    #   print(r.question)
    return r



def main():
  doctxt = "The sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating energy mainly as visible light and infrared radiation. The sun is by far the most important source of energy for life on Earth."

  resp = generate_questions(doctxt)

  print(resp.question)
  print(resp.answer)


if __name__ == "__main__":
    main()
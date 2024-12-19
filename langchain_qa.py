import getpass
import os
from rich import print
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.evaluation.qa import QAGenerateChain
from dotenv import load_dotenv
import utils

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


text = """
Nematron by COMARK has a rich heritage in delivering industrial-grade computers and displays to industries and sectors that demand stringent requirements for reliability, 
ruggedness, and longevity - essential traits for HMI and control products. 
Comark's products undergo rigorous testing and certification to ensure optimal performance in challenging environments and extreme conditions.
"""

llama_llm = OllamaLLM(
    model="Llama3.2", 
    temperature=0.2
)

openai_llm = ChatOpenAI(
    model= "gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


# Choose LLM to generate pairs
llm = llama_llm

qa = QAGenerateChain.from_llm(llm)

resp = qa.invoke(text)

pairs = resp['qa_pairs']

# Writing data to csv file
# To be used with dataset csv function
filename = "data.csv"
utils.disk_output(pairs, filename)


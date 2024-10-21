from transformers import pipeline


# Load pre-trained model for text generation
generator = pipeline('text-generation', model='gpt-3.5-turbo')

# Define input context
context = """
The sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating energy mainly as visible light and infrared radiation. The sun is by far the most important source of energy for life on Earth.
"""

# Generate question-answer pair
prompt = f"Generate a question and answer based on this context: {context}"
result = generator(prompt, max_length=100, num_return_sequences=1)
question_answer = result[0]['generated_text']

# Display the generated question and answer
print(question_answer)


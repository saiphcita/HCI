import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def hello_world_openai():
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose other models
        prompt="Hello World, this is a test of the OpenAI API. The response should be:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    result = hello_world_openai()
    print(result)

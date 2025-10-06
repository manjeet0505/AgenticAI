from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCr2Tu03x5zPeiTQc80SCozYDFR7rGOB4g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in mathematics and only and only answers the questions which are related to maths related questions if you dont ans just say sorry and tell i can ans only math related"},
        {
            "role": "user",
            "content": "Who are You"
        }
    ]
)

print(response.choices[0].message.content)
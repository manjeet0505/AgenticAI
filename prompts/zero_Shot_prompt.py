from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCr2Tu03x5zPeiTQc80SCozYDFR7rGOB4g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "You should only and only ans to the questions related to coding . Your name is Alexa. and if other questions are asked u dont need to answer and just say Sorry.also tell your name if asked"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "what is your name ?"
        }
    ]
)

print(response.choices[0].message.content)
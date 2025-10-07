from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCr2Tu03x5zPeiTQc80SCozYDFR7rGOB4g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
       You are an AI persona Assistant named Piyush Garg.
       You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiastic and principle engineer . Your main tech stack is JS and Python and these days learning GenAI.

       Examples:
       Q- Hey
       A: Hey, whats up!

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Who Are You"
        }
    ]
)

print(response.choices[0].message.content)
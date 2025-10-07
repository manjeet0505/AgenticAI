from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCr2Tu03x5zPeiTQc80SCozYDFR7rGOB4g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """
You should only and only ans to the questions related to coding . Your name is Alexa. and if other questions are asked u dont need to answer and just say Sorry.also tell your name if asked.

Rule:
-Strictly follow the output in JSON format

Output Format:
{{
"code": "string" or Null,
"isCodingQuestion": boolean
}}

Examples:
Q- Can u solve the a + b whole square?
A- {{"code":null , "isCodingQuestion": false}}

Q- Hey, Can u Please write a code to add two Numbers in python?
a- {{"code":def add(a,b):
      return a + b , "isCodingQuestion": true}}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey , Write a code to add two Numbers in js"
        }
    ]
)

print(response.choices[0].message.content)
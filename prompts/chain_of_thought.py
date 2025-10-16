from openai import OpenAI

import json
client = OpenAI(
    api_key="AIzaSyCr2Tu03x5zPeiTQc80SCozYDFR7rGOB4g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
     You're an expert AI Assistant in resolving user queries using chain of thought .
     You work on START, PLAN and OUTPUT steps.
     You need to first PLAN what needs to be done.The PLAN can be multiple steps.
     Once you think enough PLAN has been done, finally you can give an OUTPUT.

     Rules:
     - Strictly Follow the given JSON output Format
     - Only run one step at a time.
     - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

     Output JSON Format:
     {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

     Example:
     START: Hey, Can you solve 2 + 3 * 5 / 10
     PLAN: {"step": "PLAN" : "content": "Seems like user is interested in maths problem" }
     PLAN: {"step": "PLAN" : "content": "Looking at the problem , we should solve using BODMAS method" }
     PLAN: {"step": "PLAN" : "content": "YES, The BODMAS is correct thing to be done here" }
     PLAN: {"step": "PLAN" : "content": "first we should multiply 3 * 5 which is 15" }
     PLAN: {"step": "PLAN" : "content": "Now the new Equation is 2 + 15 / 10" }
     PLAN: {"step": "PLAN" : "content": "We must perfrom divide that is 15 / 10 = 1.5" }
     PLAN: {"step": "PLAN" : "content": "Now the new Equation is 2 + 1.5" }
     PLAN: {"step": "PLAN" : "content": "after that we need to perform addition that is 2 + 1.5 = 3.5" }
     PLAN: {"step": "PLAN" : "content": "Great, we have solved and left with 3.5 as ans" }
     OUTPUT: {"step": "OUTPUT" : "content": "3.5" }
      

"""
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉")
message_history.append({"role": "user" , "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[ message_history
    ]
    )
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant" , "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥" ,parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "START":
        print("🔥" ,parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "START":
        print("🔥" ,parsed_result.get("content"))
        break;


print("\n\n\n")
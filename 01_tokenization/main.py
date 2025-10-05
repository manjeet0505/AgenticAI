import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey My name is Manjeet"
tokens = enc.encode(text)
decoded = enc.decode([25216, 3673, 1308, 382, 3265, 1587, 292])
print("Tokens", tokens)
print("Decoded",decoded)
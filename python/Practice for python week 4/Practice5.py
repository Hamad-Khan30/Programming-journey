from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role":"system", "content":"we are friendly tutor for beginners."},
                {"role":"user", "content": "Explian the variable in one sentence."}]
)
print(response.choices[0].message.content)
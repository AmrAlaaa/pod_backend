import os

from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)




# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Write a short podcast intro script about the importance of fast language models",
#         },
#         {
#             "role": "system",
#             "content": "Format the script as follows: Host's lines should be in normal text, and Guest's lines should be surrounded by asterisks (**) like this: *Guest's line*.",
#         }
#     ],
#     model="llama-3.1-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)


def createPodcastScript(userPrompt, systemPrompt):

    messages=[
        {"role": "assistant", "content": ""},{
            "role": "user",
            "content": userPrompt,
        },
        {
            "role": "system",
            "content": systemPrompt,
        }
    ]   

    chat_completion = client.chat.completions.create(
    messages=messages,
    model="llama-3.1-70b-versatile",
    )
    return chat_completion.choices[0].message.content
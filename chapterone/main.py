import cohere
import os
from dotenv import load_dotenv

load_dotenv()


co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

response = co.chat(
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "Hello what are you capable off"}],
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Hello! I'm a large language model, and I'm capable of a wide range of tasks. Here are some of the things I can do:\n\n1. **Answering Questions**: I can provide thorough and informative responses to a wide range of questions on various topics, including science, history, technology, arts, and more.\n\n2. **Generating Text**: I can generate coherent and contextually relevant text, such as essays, stories, articles, emails, and social media posts.\n\n3. **Language Translation**: I can translate text between many languages, although my proficiency may vary depending on the language pair.\n\n4. **Summarization**: I can summarize long pieces of text, articles, or documents into shorter, more concise versions while retaining the main points.\n\n5. **Conversation**: I can engage in conversational dialogue, answering questions, providing information, and maintaining context throughout the conversation.\n\n6. **Creative Writing**: I can assist with creative writing tasks, such as generating plot ideas, character descriptions, and dialogue for stories or scripts.\n\n7. **Data Analysis**: While I don't have direct access to external data sources, I can help analyze and interpret data provided to me, identify patterns, and provide insights.\n\n8. **Problem Solving**: I can assist with problem-solving tasks, providing step-by-step guidance, explanations, and potential solutions.\n\n9. **Personalization**: I can adapt my responses to suit different tones, styles, and contexts, making my output more personalized and engaging.\n\n10. **Learning and Adaptation**: I can learn from user feedback and interactions, improving my responses over time and adapting to new information and contexts.\n\nKeep in mind that my capabilities are based on the data I was trained on, and I may have limitations or biases. If you have a specific task or question in mind, feel free to ask, and I'll do my best to assist you!",
                }
            ],
        },
    ],  # type: ignore
    temperature=0.3,
    model="command-a-03-2025",
)

print(response)

from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat = client.chats.create(model="gemini-3.5-flash")


def generate_ideas(topic, scraped_data):
    context = "\n".join([
        f"- [{item['score']} points] {item['title']}: {item['content']}"
        for item in scraped_data[:10]
    ])

    prompt = f"""
    You are an entrepreneur and product strategist analyzing market trends.
   
    Topic/Industry: {topic}
   
    Here are trending discussions and pain points from Hacker News:
    {context}
   
    Based on these real pain points and trends, generate 5 specific app or tool ideas.
   
    For each idea provide:
    1. App/Tool Name
    2. Problem it solves (based on the pain points above)
    3. Core features (3-4 bullet points)
    4. Target audience
    5. Suggested tech stack to build it
    6. Market opportunity (why now?)
   
    Format each idea clearly and be specific. Focus on ideas that could realistically
    be built by a small team or solo developer.
    """

    response = chat.send_message(prompt)
    return response.text


def refine_idea(idea, question):
    prompt = f"""
   Dive deeper into the idea for the user:
    {idea}
   
    The entrepreneur asks: {question}
   
    Provide specific, actionable advice to help them think through this further.
    """

    refine_response = client.send_message(prompt)
    return refine_response.text


if __name__ == "__main__":
    from scraper import scrape_hacker_news
    data = scrape_hacker_news("project management")
    ideas = generate_ideas("project management", data)
    print(ideas)

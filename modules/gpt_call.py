from dotenv import load_dotenv
from openai import OpenAI
from .scraper import scrape_posts_content
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

posts_list = scrape_posts_content()

def summarize_post(post):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Summarize the following post, keep the most important content of it: {post}"
            }
        ]
    )
    return completion.choices[0].message.content

def get_summary_messages():
    summary_messages = []
    for post in posts_list:
        post_content = f"{post.get('title', '')}\n{post.get('body', '')}"
        summary_messages.append(summarize_post(post_content))
    return summary_messages


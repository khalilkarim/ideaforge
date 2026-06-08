import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_hacker_news(topic, limit=20):
    results = []

    url = "https://hn.algolia.com/api/v1/search"
    params = {
        "query": topic,
        "tags": "story",
        "hitsPerPage": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    for hit in data["hits"]:
        results.append({
            "source": "Hacker News",
            "title": hit.get("title", ""),
            "content": hit.get("story_text", "") [:500] if hit.get("story_text") else "",
            "score": hit.get("points", 0),
            "url": hit.get("url", f"https://news.ycombinator.com/item?id={hit.get('objectID')}")
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


if __name__ == "__main__":
    results = scrape_hacker_news("project management tools")
    for r in results:
        print(f"[{r['score']} {r['title']}")
        print(f"URL: {r['url']}")
        print("---")

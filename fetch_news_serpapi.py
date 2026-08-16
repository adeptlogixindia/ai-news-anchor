import requests
serpapi_api_key = "Enter key"

def fetch_news_from_serpapi(topic, serpapi_api_key):
    url = "https://serpapi.com/search.json"
    params = {
        "q": topic,
        "tbm": "nws",  # news results
        "api_key": serpapi_api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        news_results = data.get("news_results", [])
        summaries = []

        print(f"\n📰 Top {len(news_results)} News Headlines:\n")
        for news in news_results:
            title = news.get("title", "No Title")
            snippet = news.get("snippet", "No Snippet")
            print(f"🗞️ {title}\n   {snippet}\n")
            summaries.append(f"{title}: {snippet}")

        return summaries
    else:
        print("❌ Failed to fetch news:", response.status_code)
        return []

# ==============================
if __name__ == "__main__":
   
    topic = input("📢 Enter topic to search news about: ")
    fetch_news_from_serpapi(topic, serpapi_api_key)

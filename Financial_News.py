import streamlit as st
import requests
import os
from dotenv import load_dotenv

def show():
    """Display the Indian Financial News on the Streamlit app."""
    st.title("📰 Indian Financial News")

    news_articles = fetch_news()

    if news_articles:
        for article in news_articles[:5]:  # Show only top 5 news
            title = article.get("title", "No Title Available")
            description = article.get("summary", "No Description Available")
            url = article.get("url", "#")
            image_url = article.get("banner_image")

            st.subheader(title)
            if image_url:
                st.image(image_url, use_column_width=True)
            st.write(description)
            st.markdown(f"[Read More]({url})", unsafe_allow_html=True)
    else:
        st.warning("No news articles available at the moment.")

def fetch_news():
    """Fetch Indian financial news using Alpha Vantage API."""
    load_dotenv()  # Load environment variables from .env file
    API_KEY = os.getenv("NEWS_API_KEY")

    if not API_KEY:
        st.error("⚠ API Key is missing! Please set NEWS_API_KEY in the .env file.")
        return []

    # Correct URL for Alpha Vantage news API
    URL = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey={API_KEY}"

    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # DEBUG: Print the full response for analysis
        st.write("🔍 Debugging API Response:", data)

        # If 'feed' doesn't exist or is empty, show error
        if "feed" not in data or not data["feed"]:
            st.error("⚠ No news articles found. Try again later.")
            return []

        return data["feed"]

    except requests.exceptions.RequestException as e:
        st.error(f"⚠ Failed to fetch news: {e}")
        return []

if __name__ == "__main__":
    show()

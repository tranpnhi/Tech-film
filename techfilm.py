import requests

requests.post("https://api.ai21.com/studio/v1/experimental/rewrite",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "text": "Good writing is about finding the best words to convey your message",
        "intent": "general"
        #there are 5 intents (tones): general, long,short,formal,casual
    }
)

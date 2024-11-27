from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


@app.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')
    max_results = int(request.args.get('maxResults', 10))

    youtube_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": f"{query} full movie",
        "type": "video",
        "videoDuration": "long",
        "videoCategoryId": "24",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(youtube_url, params=params)
    
    if response.status_code == 200:
        data = response.json()

        movies = []
        for item in data.get('items', []):
            thumbnails = item['snippet']['thumbnails']
            thumbnail_url = thumbnails.get('maxres', thumbnails.get('high', thumbnails.get('medium', thumbnails.get('default'))))['url']
            
            movie = {
                "title": item['snippet']['title'],
                "description": item['snippet']['description'],
                "thumbnail": thumbnail_url,
                "video_url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            movies.append(movie)

        return jsonify({"movies": movies})
    else:
        return jsonify({"error": response.json()}), response.status_code


@app.route('/trending', methods=['GET'])
def trending_videos():
    country = request.args.get('country', 'IN')

    youtube_url = "https://www.googleapis.com/youtube/v3/videos"
    
    params = {
        "part": "snippet,contentDetails,statistics",
        "chart": "mostPopular",
        "regionCode": country,
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(youtube_url, params=params)
    
    if response.status_code == 200:
        data = response.json()

        trending = []
        for item in data.get('items', []):
            thumbnails = item['snippet']['thumbnails']
            thumbnail_url = thumbnails.get('maxres', thumbnails.get('high', thumbnails.get('medium', thumbnails.get('default'))))['url']
            
            video = {
                "title": item['snippet']['title'],
                "description": item['snippet']['description'],
                "thumbnail": thumbnail_url,
                "video_url": f"https://www.youtube.com/watch?v={item['id']}",
                "views": item['statistics']['viewCount']
            }
            trending.append(video)

        return jsonify({"trending": trending})
    else:
        return jsonify({"error": response.json()}), response.status_code


@app.route('/latest', methods=['GET'])
def latest_videos():
    lang = request.args.get('lang', 'en')
    
    lang_region_mapping = {
        'en': 'US',
        'hi': 'IN',
        'es': 'ES',
        'fr': 'FR',
        'de': 'DE'
    }

    region_code = lang_region_mapping.get(lang, 'US')
    
    youtube_url = "https://www.googleapis.com/youtube/v3/videos"
    
    params = {
        "part": "snippet,contentDetails,statistics",
        "chart": "mostPopular",
        "regionCode": region_code,
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(youtube_url, params=params)
    
    if response.status_code == 200:
        data = response.json()

        latest = []
        for item in data.get('items', []):
            thumbnails = item['snippet']['thumbnails']
            thumbnail_url = thumbnails.get('maxres', thumbnails.get('high', thumbnails.get('medium', thumbnails.get('default'))))['url']
            
            video = {
                "title": item['snippet']['title'],
                "description": item['snippet']['description'],
                "thumbnail": thumbnail_url,
                "video_url": f"https://www.youtube.com/watch?v={item['id']}",
                "views": item['statistics']['viewCount']
            }
            latest.append(video)

        return jsonify({"latest": latest})
    else:
        return jsonify({"error": response.json()}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)

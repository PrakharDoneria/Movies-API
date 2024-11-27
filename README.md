# YouTube Trending & Search API

This project provides a Flask-based API that interfaces with the YouTube Data API to retrieve trending videos and perform searches for full-length movies. It includes three main endpoints:

1. `/search`: Search for movies on YouTube.
2. `/trending`: Get the top trending videos in a specific country.
3. `/latest`: Get the top trending videos based on language code.

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace the `YOUTUBE_API_KEY` variable in the code with your own YouTube Data API key. You can obtain it from the [Google Developers Console](https://console.developers.google.com/).

## Usage

1. Run the Flask application:

   ```bash
   python main.py
   ```

2. The API will be accessible at `http://localhost:5000`.

## Endpoints

### `/search`

**Method:** `GET`

**Parameters:**
- `query`: (Optional) Search query to find movies (default: empty string).
- `maxResults`: (Optional) Number of results to return (default: 10).

**Example:**

```bash
GET /search?query=action&maxResults=5
```

This will search for 5 action movies on YouTube.

**Response:**

Returns a JSON response containing a list of movies with their title, description, thumbnail URL, and video URL.

---

### `/trending`

**Method:** `GET`

**Parameters:**
- `country`: (Optional) Country code to filter trending videos by region (default: 'IN' for India).

**Example:**

```bash
GET /trending?country=US
```

This will fetch the top 10 trending videos in the United States.

**Response:**

Returns a JSON response containing a list of the top trending videos with their title, description, thumbnail URL, video URL, and view count.

---

### `/latest`

**Method:** `GET`

**Parameters:**
- `lang`: (Optional) Language code to filter trending videos by language (default: 'en' for English).

**Example:**

```bash
GET /latest?lang=fr
```

This will fetch the top 10 trending videos for the French language.

**Response:**

Returns a JSON response containing the top 10 trending videos for the specified language, with the title, description, thumbnail URL, video URL, and view count.

---

## Example Responses

### `/search` Example Response:

```json
{
  "movies": [
    {
      "title": "Movie Title 1",
      "description": "Description of movie 1",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_1"
    },
    {
      "title": "Movie Title 2",
      "description": "Description of movie 2",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_2"
    }
  ]
}
```

### `/trending` Example Response:

```json
{
  "trending": [
    {
      "title": "Trending Video 1",
      "description": "Description of video 1",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_1",
      "views": "1000000"
    },
    {
      "title": "Trending Video 2",
      "description": "Description of video 2",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_2",
      "views": "500000"
    }
  ]
}
```

### `/latest` Example Response:

```json
{
  "latest": [
    {
      "title": "Latest Trending Video 1",
      "description": "Description of video 1",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_1",
      "views": "2000000"
    },
    {
      "title": "Latest Trending Video 2",
      "description": "Description of video 2",
      "thumbnail": "https://example.com/thumbnail.jpg",
      "video_url": "https://www.youtube.com/watch?v=video_id_2",
      "views": "1000000"
    }
  ]
}

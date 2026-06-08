# IdeaForge

IdeaForge offers an accelerated way to find app or business ideas. By offering AI infused recommendations through deep level research tailored specifically to solving pain points throughout an array of industries.

Real pain points from Hacker News are passed to Google Gemini for a tailored analysis that accelerates and validates possible solutions — then refined further through continuous follow up queries until the idea is fully fleshed out.

---

## Features

- **Market Research** — scrapes Hacker News to identify real unresolved pain points across industries
- **AI Idea Generation** — Google Gemini analyzes pain points and generates 5 specific app or tool ideas with problem, solution, target audience and tech stack
- **Idea Refinement** — dig deeper into any idea with continuous follow up questions and queries
- **Save Ideas** — save promising ideas to a local database for later review
- **Clean Interface** — simple web UI to search, refine, save and manage ideas

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| Web Framework | Flask |
| AI | Google Gemini API |
| Data Source | Hacker News API |
| Database | SQLite |
| HTML Parsing | BeautifulSoup4 |

---

## Getting Started

### Prerequisites
- Python 3.x installed
- Google Gemini API key (free at aistudio.google.com)

### Setup

```bash
# clone the repo
git clone https://github.com/YOUR_USERNAME/ideaforge.git
cd ideaforge

# create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root folder:

```
GEMINI_API_KEY=your_gemini_api_key
```

### Run

```bash
python3 app.py
```

Open your browser and go to:

```
http://localhost:5000
```

---

## How It Works

```
1. Enter an industry or problem space
2. IdeaForge scrapes Hacker News for trending pain points
3. Real pain points are sent to Google Gemini
4. Gemini generates 5 specific app or tool ideas
5. Dig deeper into any idea with follow up questions
6. Save promising ideas for later review
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Web interface |
| POST | /search | Scrape HN + generate ideas |
| POST | /refine | Dig deeper into a specific idea |
| GET | /ideas | Get all saved ideas |
| POST | /ideas | Save an idea |
| DELETE | /ideas/{id} | Delete a saved idea |

---

## Project Structure

```
ideaforge/
├── app.py              →  Flask web server and API endpoints
├── scraper.py          →  Hacker News scraping
├── gemini_service.py   →  Google Gemini AI integration
├── database.py         →  SQLite operations
├── requirements.txt    →  Python dependencies
├── .env                →  secrets (not committed)
├── templates/
│   └── index.html      →  web interface
└── static/
    └── style.css       →  styling
```

---

## Environment Variables Reference

| Variable | Description |
|----------|-------------|
| GEMINI_API_KEY | Google Gemini API key from aistudio.google.com |

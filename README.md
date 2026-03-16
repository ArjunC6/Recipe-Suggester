# Mise en Place — Recipe Suggester

A beautiful Flask web app that suggests recipes based on ingredients you have at home, powered by Claude AI.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```
Get your API key at: https://console.anthropic.com/

### 3. Run the app
```bash
python app.py
```

Then open http://localhost:5000 in your browser.

## Features
- **Tag-based ingredient input** — type an ingredient and press Enter to add it
- **Dietary filters** — Vegetarian, Vegan, Gluten-Free, Dairy-Free, Keto, Low Carb
- **Cuisine filters** — Italian, Asian, Mexican, Mediterranean, Indian, French, American
- **3 AI-generated recipes** per search with:
  - Prep time & difficulty
  - Which ingredients you already have vs. what you still need
  - Step-by-step instructions (expandable)

## Project Structure
```
recipe-suggester/
├── app.py              # Flask routes + Anthropic API calls
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Full frontend (HTML + CSS + JS)
└── README.md
```

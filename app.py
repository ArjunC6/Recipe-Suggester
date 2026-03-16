from flask import Flask, render_template, request, jsonify
from groq import Groq
import json

app = Flask(__name__)
client = Groq()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.get_json()
    ingredients = data.get("ingredients", [])
    dietary = data.get("dietary", "")
    cuisine = data.get("cuisine", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    ingredient_list = ", ".join(ingredients)
    filters = []
    if dietary:
        filters.append(f"dietary preference: {dietary}")
    if cuisine:
        filters.append(f"cuisine style: {cuisine}")
    filter_text = (" with " + " and ".join(filters)) if filters else ""

    prompt = f"""I have these ingredients: {ingredient_list}{filter_text}.

Suggest 3 creative recipes I can make. For each recipe, write detailed, thorough cooking steps (at least 6-8 steps) with specific quantities, temperatures, and timing. Respond with JSON only (no markdown, no preamble, no backticks) in this exact format:
{{
  "recipes": [
    {{
      "name": "Recipe Name",
      "emoji": "🍝",
      "time": "30 mins",
      "difficulty": "Easy",
      "description": "A short enticing description (1-2 sentences)",
      "ingredients_used": ["ingredient1", "ingredient2"],
      "missing_ingredients": ["ingredient3"],
      "steps": ["Detailed step 1", "Detailed step 2", "Detailed step 3"]
    }}
  ]
}}"""

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=3000,
    )

    raw = chat_completion.choices[0].message.content.strip()

    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        raw = raw.rsplit("```", 1)[0]

    result = json.loads(raw)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
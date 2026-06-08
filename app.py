from flask import Flask, request, jsonify, render_template
from scraper import scrape_hacker_news
from gemini_service import generate_ideas, refine_idea
from database import init_db, save_idea, get_all_ideas, delete_idea

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "Topic is required"}), 404

    scraped = scrape_hacker_news(topic)

    if not scraped:
        return jsonify({"error": "There is no data for this topic"}), 404

    ideas = generate_ideas(topic, scraped)

    return jsonify({
        "topic": topic,
        "ideas": ideas,
        "sources": scraped[:5]
    })

@app.route("/refine", methods=["POST"])
def refine():
    data = request.json
    idea = data.get("idea")
    question = data.get("question")

    if not idea or not question:
        return jsonify({"error": "idea and question are required"}), 400

    refined = refine_idea(idea, question)

    return jsonify({"response": refined})

@app.route("/ideas", methods=["GET"])
def get_ideas():
    ideas = get_all_ideas()
    return jsonify([{
        "id": idea[0],
        "topic": idea[1],
        "ideas": idea[2],
        "created_at": idea[3],}
        for idea in ideas]
    )

@app.route("/ideas", methods=["POST"])
def save():
    data = request.json()
    idea = data.get("idea")
    topic =data.get("topic")

    if not topic or idea:
        return jsonify({"error": "topic and idea required to save"})

    save_idea(topic, idea)

    return jsonify({"message": "Idea saved successfully"})

@app.route("/ideas/<int:idea_id>", methods=["DELETE"])
def delete(idea_id):
    delete_idea(idea_id)

    return jsonify({"message": "idea deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)



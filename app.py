from flask import Flask, render_template, jsonify

app = Flask(__name__)

player = {
    "name": "hiccu",
    "rank": "IMMORTAL 2",
    "rr": 154,
    "rank_image": "Immortal_1_Rank.png"
}

@app.route("/")
def overlay():
    return render_template(
        "index.html",
        player=player
    )

@app.route("/riot.txt")
def riot_verification():
    return "c8d4fc31-d2d2-4e34-9731-de50a56b6007", 200, {
        "Content-Type": "text/plain"
    }

@app.route("/api/player")
def get_player():
    return jsonify(player)

if __name__ == "__main__":
    app.run(debug=True)

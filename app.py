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


@app.route("/api/player")
def get_player():
    return jsonify(player)


if __name__ == "__main__":
    app.run(debug=True)

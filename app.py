from flask import Flask, render_template, request, jsonify
import os
from ice_breaker import ice_break

app = Flask(__name__)

app.route("/process", methods=["POST"])


def process():
    name = request.form["name"]
    person_info, image_url = ice_break(name=name)
    return jsonify(
        {
            "summary": person_info.summary,
            "facts": person_info.facts,
            "topics": person_info.topics,
            "hobbies": person_info.hobbies,
            "image_url": image_url,
        }
    )


if __name__ == "__main__":
    port = os.environ.get('PORT', 8000)
    app.run(debug=True, host='0.0.0.0', port=int(port))

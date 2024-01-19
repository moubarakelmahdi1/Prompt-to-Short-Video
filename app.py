from flask import Flask, request, jsonify, render_template, url_for
import main
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_video', methods=['POST'])
def generate_video_endpoint():
    title = request.form.get('title', 'default_title')
    script_text = request.form.get('script', '')

    if not script_text:
        return jsonify({"error": "Script is required"}), 400

    try:
        # Convertir le script en format JSON en objet Python
        script = json.loads(script_text)

        video_path = main.generate_video(title, script)
        video_url = url_for(
            'static', filename=video_path.replace('static/', ''))
        return jsonify({"message": "Video generated successfully", "video_url": video_url}), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid script format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

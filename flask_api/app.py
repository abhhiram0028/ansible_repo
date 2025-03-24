from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "up", "healthy": True})

@app.route('/redirect', methods=['GET'])
def url_redirect():
    target_url = request.args.get('url')

    if not target_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    corrected_url = target_url.replace("_", ".")
    return redirect(f"https://{corrected_url}")

if __name__ == '__main__':
    app.run(debug=True)

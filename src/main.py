from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎬 Simple Movie Site</h1>
    <p>Welcome to my movie list!</p>

    <h2>Top Movies</h2>
    <ul>
        <li>The Shawshank Redemption</li>
        <li>Inception</li>
        <li>Interstellar</li>
        <li>The Dark Knight</li>
        <li>Avengers: Endgame</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)

import logging
from flask import Flask, request, render_template
from scrapper import youtube_scrap

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('log.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scrapper", methods=["POST"])
def scrapper():
    try:
        question = request.form.get("question")
        link = request.form.get("link")
        csv = request.form.get("csv")
        result = youtube_scrap(question, link, csv)
        logger.info(f"Scraped {question} for {link}")
        return render_template("index.html", result=result)
    except Exception as e:
        logger.exception(e)
        return "Error: " + str(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

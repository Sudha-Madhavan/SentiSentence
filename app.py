from flask import *
import language_tool_python
from textblob import TextBlob

app = Flask(__name__)


@app.route("/")
def upload():
    return render_template("input.html")


@app.route("/success", methods=["POST"])
def success():
    global st
    st = str(request.form['inp'])
    return render_template("success.html", start=st)


@app.route("/spellcheck")
def check():
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(st)
    res = ' '.join(map(str, matches))
    result = "Spellcheck Results : "
    if (res == ""):
        sample = "No errors"
        return render_template("result.html", result=result, sample=sample)
    else:
        sample = res
        return render_template("result.html", result=result, sample=sample)


@app.route("/senti")
def senti():
    text = TextBlob(st)
    if text.sentiment[0] > 0:
        output = "Postitive Emotion"
    elif text.sentiment[0] < 0:
        output = "Negative Emotion"
    elif text.sentiment[0] == 0.0:
        output = "No Emotion"
    if text.sentiment[1] > 0.5:
        output1= "It is a personal belief"
        return render_template("result.html", output=output,output1=output1)
    elif text.sentiment[1] <= 0.5:
        output1 = "It is general truth, not a personal belief"
        return render_template("result.html", output=output,output1=output1)



if __name__ == "__main__":
    app.run(debug=True)

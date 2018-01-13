import flask
app = flask(__name__)

@app.route("/")
def main():
    return "Welcome!"
if __name__ == "__main__":
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡API actualizada y funcionando correctamente en Azure App Service! 😄"

if __name__ == "__main__":
    app.run()
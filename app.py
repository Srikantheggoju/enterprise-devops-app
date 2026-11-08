from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Enterprise DevOps Pipeline Working Successfully!"

@app.route('/health')
def health():
    return {
        "status": "UP",
        "application": "enterprise-devops-app"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

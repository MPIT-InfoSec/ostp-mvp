from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from markdown2 import markdown
from app.agent.generator import generate_jd_from_prompt

# -------------------------------------------------------
# Jinja2 Template Configuration
# -------------------------------------------------------

# Tell FastAPI where to find your HTML templates
templates = Jinja2Templates(directory="app/web/templates")

# Create a new router for all web-based (HTML UI) routes
router = APIRouter()


# -------------------------------------------------------
# GET / → Serve the Main UI Form
# -------------------------------------------------------

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Renders the home page with a prompt input form.

    - Method: GET
    - Route: /
    - Template: index.html
    """
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------------------------------------------
# POST /generate → Process Prompt + Render Result
# -------------------------------------------------------

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, prompt: str = Form(...)):
    """
    Accepts a natural language job prompt, sends it to the backend LLM,
    and renders the result as HTML (converted from Markdown).

    - Method: POST
    - Route: /generate
    - Form Field: prompt (str)
    - Returns: Rendered HTML version of JD + hidden Markdown for download
    """
    # Run the LangChain agent to generate JD as Markdown
    jd_markdown = generate_jd_from_prompt(prompt)

    # Convert Markdown to HTML for display in the browser
    jd_html = markdown(jd_markdown)

    # Render the result on the same page
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prompt": prompt,
        "jd_markdown": jd_markdown,
        "jd_html": jd_html,
    })


# -------------------------------------------------------
# POST /download → Download JD as .md File
# -------------------------------------------------------

@router.post("/download")
async def download_markdown(markdown: str = Form(...)):
    """
    Returns a downloadable `.md` file containing the generated JD.

    - Method: POST
    - Route: /download
    - Form Field: markdown (str)
    - Content-Type: text/markdown
    - Header: Content-Disposition (forces file download)
    """
    headers = {
        "Content-Disposition": "attachment; filename=job_description.md"
    }
    return Response(content=markdown, media_type="text/markdown", headers=headers)

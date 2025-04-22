from fastapi import APIRouter, status
from app.models.prompt import PromptRequest
from app.models.response import PromptResponse
from app.agent.generator import generate_jd_from_prompt

# Create a router instance for job description-related endpoints
router = APIRouter()


@router.post(
    "/generate-jd",
    status_code=status.HTTP_200_OK,
    response_model=PromptResponse,
    tags=["JD Generation"],
    summary="Generate Job Description from Text Prompt",
    description="""
    Generate a structured job description (JD) using AI from a natural language prompt.
    ### Example Prompt
    Looking for a frontend engineer with React, TypeScript, and Tailwind CSS experience.
    """
)
async def generate_jd(data: PromptRequest) -> PromptResponse:
    """
    Accepts a natural language prompt and returns a job description in Markdown format.

    Args:
        data (PromptRequest): Input model containing the prompt string.

    Returns:
        PromptResponse: Structured response with input and generated JD in Markdown.
    """
    jd_text = generate_jd_from_prompt(data.prompt)

    return PromptResponse(
        input=data.prompt,
        jd_markdown=jd_text
    )

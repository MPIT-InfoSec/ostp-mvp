from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    """
    Request model for submitting a prompt to generate a job description.

    Fields:
    - prompt (str): The main natural language input (text prompt) from the user.

    In the future, this model can be extended to support:
    - audio_prompt (bytes or file upload): For speech-to-text support
    - attachments (List[UploadFile]): For supporting PDFs or images
    """
    prompt: str = Field(
        ...,
        title="Text Prompt",
        description="The natural language description of the job role (e.g., 'Looking for a senior Python backend developer with AWS experience.')"
    )

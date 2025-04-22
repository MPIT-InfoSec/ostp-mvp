from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from app.core.config import settings

# -----------------------------
# Initialize the Language Model
# -----------------------------

# Load configuration from .env or config module
MODEL_NAME = settings.OPENAI_MODEL or "gpt-3.5-turbo"
TEMPERATURE = float(settings.OPENAI_TEMPERATURE or 0.5)

# Initialize the LLM using LangChain's OpenAI wrapper
llm = ChatOpenAI(
    temperature=TEMPERATURE,
    model=MODEL_NAME,
    openai_api_key=settings.OPENAI_API_KEY
)

# -----------------------------
# Prompt Generation Logic
# -----------------------------

def generate_jd_from_prompt(prompt: str) -> str:
    """
    Generate a job description using a natural language prompt.

    Args:
        prompt (str): Freeform text like 'Looking for a React engineer with AWS experience.'

    Returns:
        str: AI-generated JD in plain text or Markdown format.
    """
    # Define the system template for how the AI should behave
    template = ChatPromptTemplate.from_template(
        """You are an HR assistant helping to draft structured, concise, and professional job descriptions.

        Generate a job description suitable for posting on Naukri.com using the following structure:

        1. **Job Title / Designation**: [Insert Title]  
        2. **SEO-Friendly Short Description (Max 150 words)**:  
        3. **Employment Type**: [Full Time / Part Time / Contract]  
        4. **Key Skills**: [minimum 3 primary skills and 3 relevant ones e.g., Java, SpringBoot, Postgres, ReactJs]  
        5. **Job Location**: [e.g., Pune]  
        6. **Work Experience**: [e.g., 5 years]  
        7. **Annual Salary Range**: [e.g., 25 Lakhs INR per annum]  
        8. **Educational Qualification**: [e.g., B.E./B.Tech in Computer Science, MCA, BCA, or BSc in Computer Science]  
        9. **Roles and Responsibilities**:  [minimum 5 bulleted points]
        10. **Desired Candidate Profile**:  [minimum 5 bulleted points]

        Use a clear, recruiter-friendly tone suitable for job portals like Naukri.com.  
        Return the job description as a **Markdown-formatted block** with bold section headings and bullet points where appropriate.

        Prompt: {raw_prompt}

        Please return only the Markdown content without wrapping it in triple backticks.
        """
    )

    # Format the template with user input
    formatted_prompt = template.format_messages(raw_prompt=prompt)

    # Get AI-generated content
    response = llm(formatted_prompt)

    return response.content.strip()

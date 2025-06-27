import json
import google.generativeai as genai

def generate(resume, github_repos, job_description):
    
    system_instruction = f"""
    You are an expert cover letter writer. Your task is to generate a professional, personalized cover letter tailored specifically to the job description using the user’s resume and GitHub project details.

    Use the following data:
    Resume:
    {resume}

    GitHub Projects:
    {github_repos}

    Job Description:
    {job_description}
    """

    response = model.generate_content(
        contents=system_instruction,
        generation_config={
            "temperature": 0.8,
            "max_output_tokens": 2000,
            "top_p": 0.9,
            "top_k": 10,
        },
    )
    return response.text.strip()

if __name__ == "__main__":
    genai.configure(api_key="API KEY HERE JOTO")
    model = genai.GenerativeModel("gemini-2.0-flash")
    # Generate response
    # Load json metadata
    with open("user/combined_data.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)
    resume = user_data["resume"]
    github_repos = user_data["github_repos"]

    job_description = """
    About Bestie
    Bestie is a concierge-style, membership-based pet sitting service for busy pet parents in downtown Manhattan. Instead of self-serve booking, our members text us and we coordinate personalized pet care with our vetted network of sitters. We’re now looking to build a smart, backend-powered scheduling tool to help automate the sitter-matching process behind the scenes—without losing the white-glove experience our members love.

    What We’re Building
    We’re creating an internal booking process where members can enter their requests in free text (e.g., “30-minute walk Friday at 9pm”). The system will:
    * Ingest free text from member
    * Prompt for any missing info (e.g., location, timing, booking type, etc.)
    * Check sitter availability and preferences
    * Match the request to the best-fit sitters
    * Notify sitters to confirm or decline
    * Confirm back to the member once a sitter is booked
    This tool will be used internally to streamline operations—not as a public-facing product.

    What You’ll Do
    * Design and build a backend that can handle:
    * Sitter and member profiles, preferences, locations, and availability
    * A matching engine to recommend sitters based on past history, proximity, and open schedules
    * A messaging flow (via text or interface) to confirm bookings
    * Suggest and implement tools (e.g., calendar integrations, SMS APIs like Twilio, etc.)
    * Explore and integrate AI tools (e.g., natural language processing, prompt engineering, scheduling intelligence) to improve matching logic and user input interpretation
    * Collaborate with the founder (Lauren) to iterate and improve the product based on real usage

    You Might Be a Fit If You:
    * Are a current college student or recent graduate looking for hands-on experience with a real-world product to add to your resume and portfolio
    * Want experience using AI tools and integrations in a practical, applied setting
    * Are curious about natural language processing, recommendation systems, and smart automation
    * Have experience with scheduling or logistics tools, matching algorithms, or marketplace apps
    * Enjoy designing systems that replace spreadsheets, texts, and manual processes
    * Are comfortable asking questions, offering suggestions, and working independently

    Tech Stack (Flexible):
    * Python
    * PostgreSQL or MongoDB
    * Integrations: Zapier, Twilio, Google Calendar, Auth0/Firebase
    * We currently use OpenPhone so any experience using this tool is a plus, and integrations need to be compatible with OpenPhone

    Estimated Time Commitment:
    8 to 10 hours/week for 6 to 8 weeks, with potential for ongoing iterations or maintenance work after MVP launch.
    """

    reply = generate(resume, github_repos, job_description)
    print("\nGemini says:\n", reply)

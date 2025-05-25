import google.generativeai as genai

class GeminiLLM:
    def __init__(self, config):
        self.api_key = config.GEMINI_API_KEY
        self.model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        self.logger = config.logger
    
    def generate(self, system_instruction):
        return "Hello"
        
    def generate_test(self, resume, github_repos, job_description):
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
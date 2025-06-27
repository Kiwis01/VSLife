import google.generativeai as genai

class GeminiLLM:
    def __init__(self, config):
        self.api_key = config.GEMINI_API_KEY
        self.logger = config.logger
    
    def generate(self, query):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(
            contents=query,
            generation_config={
                "temperature": 0.8,
                "max_output_tokens": 2000,
                "top_p": 0.9,
                "top_k": 10,
            },
        )
        return response.text.strip()

    def generate_relative_query(self, query):
        system_instruction = f"""
        You are only going to provide a relative query to make a vector search.
        You want to make queries for cover letters.
        The pdf file contains guidelines and tips for cover letters and CVs.
        The relative query should be a 5 word sentence or less.
        Use this initial query to make the relative query:
        {query}
        """
        response = self.generate(system_instruction)
        return response
        
    def generate_cover_letter(self, resume, github_repos, job_description, harvard_tips, final_query):
        # system_instruction = f"""
        # You are an expert cover letter writer. Your task is to generate a professional, personalized cover letter tailored specifically to the job description using the user’s resume and GitHub project details.
        # Use the following data:
        # Cover Letter Guidelines:
        # {harvard_tips}

        # User Resume:
        # {resume}

        # User GitHub Projects:
        # {github_repos}

        # Job Description:
        # {job_description}
        # """

        system_instruction = f"""
        # You are an expert cover letter writer. Your task is to generate a professional, personalized cover letter tailored specifically to the job description.
        # You will utilize three responses from the vector search to generate the cover letter, this text should give me guidelines on how to write a cover letter.
        # Use the following Guidelines and tips:
        {final_query}

        # Job Description that user wants to apply for:
        {job_description}

        # Use the following Resume to fill out the cover letter:
        {resume}
        """
        response = self.generate(system_instruction)
        return response

    def generate_resume(self, resume, github_repos, job_description, harvard_tips):
        system_instruction = f"""
        You are an expert resume writer. Your task is to generate a professional, personalized resume tailored specifically to the job description using the user’s resume and GitHub project details.
        Use the following data:
        Resume Guidelines:
        {harvard_tips}

        User Resume:
        {resume}

        User GitHub Projects:
        {github_repos}

        Job Description:
        {job_description}
        """

        response = self.generate(system_instruction)
        return response
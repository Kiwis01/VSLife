from config.config import Config
from llm.gemini import GeminiLLM
from rag.embedding import Embedding
import json

def main():
    config = Config()
    gemini = GeminiLLM(config)
    embedding = Embedding(config)

    # Load User processed Data
    with open("user/combined_data.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)
    resume = user_data["resume"]
    # github_repos = user_data["github_repos"]

    # with open("user/combined_data.txt", "r", encoding="utf-8") as f:
    #     user_data = f.read()
    # resume = user_data.split("GITHUB REPOS:")[0]
    # github_repos = user_data.split("GITHUB REPOS:")[1]

    # Load Desired job description
    job_description = ""
    with open("user/job_description.txt", "r", encoding="utf-8") as f:
        job_description = f.read()

    # Embedding
    embedding.embed("database/harvard_booklet.pdf")

    # Vector search
    # option = input("Choose one of the folllowing options by entering the number:\n1. Cover Letter\n2. Resume\n")
    # vector_search = ""
    # if option == "1":
    #     query = f"What are some cover letter tips for a {job_description}?"
    #     query += " Focus on structure, tone, and how to mention GitHub projects."
    # elif option == "2":
    #     query = f"What are CV best practices for a {job_description}?"
    #     query += " Include action verbs and formatting structure."
    # else:
    #     query = "Career writing tips"

    # Generate relative query
    queries = []
    for i in range(3):
        if i != 0:
            query = gemini.generate_relative_query(queries[i-1])
        else:
            query = gemini.generate_relative_query(job_description)
        queries.append(query)

    final_query = ""
    for query in queries:
        print("\nQuery:\n", query, "\nEND of Query\n")
        vector_search = embedding.search(query)
        print("\nVector Search:\n", vector_search, "\nEND of Vector Search\n")
        final_query += vector_search

    github_repos = ""
    harvard_tips = ""
    reply = gemini.generate_cover_letter(resume, github_repos, job_description, harvard_tips, final_query)
    print("\nGemini says:\n", reply)

    # query = "Cover Letter"
    # vector_search = embedding.search(query)
    # print("\nVector Search:\n", vector_search, "\nEND of Vector Search\n")

    # Gemini
    # if option == "1":
    #     reply = gemini.generate_cover_letter(resume, github_repos, job_description, vector_search)
    # elif option == "2":
    #     reply = gemini.generate_resume(resume, github_repos, job_description, vector_search)
    # else:
    #     self.logger.warning("Invalid option selected. Please choose 1 or 2.")


    # print("\nGemini says:\n", reply)

if __name__ == "__main__":
    main()
    
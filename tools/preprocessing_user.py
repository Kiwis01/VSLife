import json
import fitz 

def get_resume_text(resume_path):
    doc = fitz.open(resume_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def get_github_repo_info(repo_path):
    with open(repo_path, "r") as f:
        return json.load(f)

def save_as_json(resume_text, github_repos, out_path="combined_data.json"):
    combined = {
        "resume": resume_text,
        "github_repos": github_repos
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=4)

def save_as_text(resume_text, github_repos, out_path="combined_data.txt"):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("RESUME:\n")
        f.write(resume_text + "\n\n")

        f.write("GITHUB REPOS:\n")
        for i, repo in enumerate(github_repos, 1):
            f.write(f"{i}. {repo['name']}\n")
            f.write(f"   Description: {repo['description']}\n")
            f.write(f"   Stars: {repo['stargazers_count']}\n")
            f.write(f"   URL: {repo['url']}\n\n")

resume = get_resume_text("user/resume.pdf")
repos = get_github_repo_info("user/github_repos.json")
save_as_json(resume, repos)
save_as_text(resume, repos)
print("Saved both JSON and plain text files.")

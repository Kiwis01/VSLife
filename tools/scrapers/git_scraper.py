import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
load_dotenv()
 
def get_readme(url, driver):
    readme_url = f"{url}/blob/main/README.md"
    driver.get(readme_url)
    readme = driver.find_element(By.CLASS_NAME, "Box-sc-g0xbh4-0").text

    if "Raw" in readme:
        clean_readme = readme.split("Raw", 1)[1].strip()
    else:
        clean_readme = readme.strip()  
        
    return clean_readme

def get_github_info(username,token,driver):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get GitHub info")

    repos = response.json()
    sorted_repos = sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)

    repo_data=[]
    #get top 5 repos, change this to use all repos
    for repo in sorted_repos:
        private = repo["private"]
        if not private:
            readme = get_readme(repo["html_url"], driver)
        repo_info = {
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "readme": readme if readme else "None",
            "url": repo["html_url"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "pushed_at": repo["pushed_at"],
            "stargazers_count": repo["stargazers_count"],
            "forks_count": repo["forks_count"],
        }
        repo_data.append(repo_info)
    
    # Save to JSON file
    with open("user/github_repos.json", "w", encoding="utf-8") as f:
        json.dump(repo_data, f, indent=4)
    print("saved github data")


if __name__ == "__main__":
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    username = "Kiwis01"
    token = os.getenv("GITHUB_TOKEN")
    get_github_info(username,token,driver)
    driver.quit()
 
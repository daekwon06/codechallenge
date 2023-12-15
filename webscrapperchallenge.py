import requests 
from bs4 import BeautifulSoup


keywords = [
  "flutter",
  "python",
  "golang"
]

r = requests.get(f"https://remoteok.com/remote-{keywords[0]}-jobs", headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})

soup = BeautifulSoup(r.content, "html.parser")

jobs = soup.find("table", id="jobsboard").find_all("td", class_="company position company_and_position")

all_jobs = []


for job in jobs:
  title = job.find("h2")
  company = job.find("h3")
  region = job.find("div", class_="location")
  print(region)
  url = job.find("a")["href"]

  job_data = {"title": title.text,
              "company": company.text,
              "region": region,
              "url": f"https://remoteok.com{url}",
             }
  
  all_jobs.append(job_data)

print(all_jobs)



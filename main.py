from bs4 import BeautifulSoup 
from datetime import datetime
import requests
import time


def find_jobs(unfimiliar_skills):
    # store html information from website 
    html_texts = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_texts, 'lxml')
    # find all jobs on website and store in variable 
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # get current time
    now = datetime.now()
    # convert to hours:minutes:seconds format 
    current_time = now.strftime("%H:%M:%S")
    for job in jobs:
        skills = job.find('span', class_ = 'srp-skills').text.strip().lower()
        # only if skills dont include unfimiliar skills 
        state = True
        for uf_skill in unfimiliar_skills:
            if uf_skill in skills:
                state = False 
        if state == True:
            job_title = job.header.h2.a.text.strip()
            company = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            link = job.header.h2.a['href'].strip()
            # write to text file with current time as title 
            with open(f"{current_time}.txt", 'a') as fout:
                fout.write(f"Job Title: {job_title}\n")
                fout.write(f"Company: {company}\n")
                fout.write(f"Skills: {skills}\n")
                fout.write(f"Link: {link}\n")
                fout.write("\n")

if __name__ == '__main__': 
    print("What are skills you are unfimiliar with? (type 'x' when done)")
    # list of unfimiliar skills based on inputs 
    unfimiliar_skills = []
    skill = input("> ")
    while skill != 'x':
        unfimiliar_skills.append(skill.lower().strip())
        skill = input("> ")
    print(f"Filtering out jobs with {unfimiliar_skills} as a key skill")
    # look for jobs every 12 hours 
    while True:
        find_jobs(unfimiliar_skills)
        wait_in_hours = 12 
        print(f"Waiting {wait_in_hours} hours...")
        time.sleep(wait_in_hours * 60 * 60)
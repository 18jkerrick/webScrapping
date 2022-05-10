# webScrapping
This program web scrapes from https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=.
It takes Python developer jobs from the website every 12 hours and pastes the job title, company, skills, and link for each job onto a seperate text file 
in the same directory that it is ran in. The name of the text file will be the time that the program is ran at. The program asks the user for a list of 
unfimiliar skills, so that it can filter out jobs that have those skills in the description. The input for the list is terminated by a 'x'. 
The skills are transformed into lowercase chars and stripped so that capitolization does not matter. 

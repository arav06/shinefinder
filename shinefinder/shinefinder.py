#!/usr/bin/python3
from bs4 import BeautifulSoup
from requests import get
from argparse import ArgumentParser,SUPPRESS
from datetime import datetime
from time import sleep

banner = """
 ██████╗██╗  ██╗██╗███╗  ██╗███████╗███████╗██╗███╗  ██╗██████╗ ███████╗██████╗ 
██╔════╝██║  ██║██║████╗ ██║██╔════╝██╔════╝██║████╗ ██║██╔══██╗██╔════╝██╔══██╗
╚█████╗ ███████║██║██╔██╗██║█████╗  █████╗  ██║██╔██╗██║██║  ██║█████╗  ██████╔╝
 ╚═══██╗██╔══██║██║██║╚████║██╔══╝  ██╔══╝  ██║██║╚████║██║  ██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║██║ ╚███║███████╗██║     ██║██║ ╚███║██████╔╝███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚══╝╚══════╝╚═╝     ╚═╝╚═╝  ╚══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
> Created by Arav Budhiraja(https://github.com/arav06)
"""

parser = ArgumentParser(add_help = False)
parser.add_argument('--job','-j', type=str, required=True,help="Job you are looking for")
parser.add_argument('--location','-l',type=str, required=True,help="Your location preference")
parser.add_argument('--pages','-p', type=str, required=True,help="Number of pages you wish to check")
parser.add_argument('-h', '--help', action='help', default=SUPPRESS,help='Shows the help message')
args = parser.parse_args()

myjob = args.job.replace(' ', "-").rstrip("-")
location = args.location.replace(' ', "-").rstrip("-")
pages = args.pages

try:
      pages = int(pages)
except:
      print("[+]Number of pages must be an integer")
      exit()

if pages < 1:
      print("[+]Number of pages must be greater than 1 and not null\n[+]Taking number of pages as 1")
      pages = 1

print(banner)

now = datetime.now()
dt = now.strftime("%d.%m.%Y %H-%M-%S")
tempJob = myjob.replace('-',' ')

f = open(f"report-{dt}.txt",'w')
f.write(f"Report for {dt}\n\n")
f.write(f"Job: {tempJob}\n")
f.write(f"Location: {location}\n\n------------------------------------------------------\n\n")
f.close()

for page in range(1,pages+1):

      url = f"https://www.shine.com/job-search/{myjob}-jobs-in-{location}-{page}"
      r = get(url)
      content = r.content

      soup = BeautifulSoup(content,'lxml')

      alljobs = soup.find_all('div', class_ = "w-90 ml-25")

      print("\n\n")

      for job in alljobs:

            title = job.find('h2', class_ = "result-display__profile__job-tittle").text
            exp = job.find('li', class_ = "w-30 mr-10 result-display__profile__years").text.replace("to","-").strip().replace("Yrs", " years")
            company = job.find('span', class_ = "result-display__profile__company-name").text.strip()
            link = job.find('a', class_ = "job_title_anchor")["href"]
            moreinfo = f"https://shine.com{link}".rstrip("/")
            posted = job.find('li', class_ = "w-30 mr-10 result-display__profile__date").text.strip()
            
            data = f"Job Title: {title}\nCompany: {company}\nPosted: {posted}\nExperience Required: {exp}\nMore Info: {moreinfo}\n\n------------------------------------------------------\n\n"
            print(data)
            sleep(1)
            f2 = open(f"report-{dt}.txt",'a')
            f2.write(data)

f2.write("---------------------------------------------------------------------------------------------------------------")
f2.close()

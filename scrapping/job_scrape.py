import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://ng.indeed.com/jobs?q=software+developer&l=Nigeria'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')
links = results.find_all(
    'div', class_='jobsearch-SerpJobCard')


def sorted_jobs_by_title(jobs):
    return sorted(jobs, key=lambda k: k['title'], reverse=True)


def create_custom_job(links):
    jobs = []
    for item in links:
        title = item.find('a', class_='jobtitle')
        company = item.find('span', class_='company')
        location = item.find(
            'span', class_='location accessible-contrast-color-location')
        if None in (title, company, location):
            continue

        jobs.append(
            {'title': title.text.strip(), 'location': location.text.strip(), 'company': company.text.strip()})
    return jobs


pprint.pprint(create_custom_job(links))

# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='')
#     location_elem = job_elem.find(
#         'span', class_='location accessible-contrast-color-location')
#     print(title_elem.text)
#     print(location_elem.text)
#     print()

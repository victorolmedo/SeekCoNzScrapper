import requests
from bs4 import BeautifulSoup
url ="https://www.seek.co.nz/php-developer-jobs?salaryrange=30000-100000&salarytype=annual&where=Work%20from%20home"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    def has_data_search(tag):
        return tag.has_attr("data-search-sol-meta")
    results = soup.find_all(has_data_search)

    for job in results:
        try:
            title =job.find("a", attrs={ "data-automation": "jobTitle"}).get_text()
            company =job.find("a", attrs={"data-automation":"jobCompany"}).get_text()
            joblink ="https://www.seek.co.nz" + job.find("a", attrs={"data-automation":"jobCompany"})["href"]
            salary = job.find("span", attrs={"data-automation":"jobSalary"})
            salary = salary.get_text()  if salary else 'n/a'
            job="Titulo:{}\nEmpresa:{}\nSalario:{}\nLink:{}\n"
            job = job.format(title,company,salary,joblink)
            print(job)
        except Exception as e:
            print("Exception: {}" .format(e))
            pass




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

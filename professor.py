from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

BASE = 'http://www.ratemyprofessors.com/'

# returns html of url passed
def search(url):
    req = Request(url,headers={'User-Agent' : "test"})
    con = urlopen(req)
    soup = BeautifulSoup(con, 'lxml')
    return soup

# returns link to ratemyprofessor page
def find_professor(professor):

    professor = professor.replace(" ","+")

    links = search('http://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=University+of+Texas+at+Austin&schoolID=1255&query={})'.format(professor))

    for link in links.find_all('a'):
        link = link.get('href')
        if link != None and '/ShowRatings' in link:
            return link

# Returns overall rating
def get_rating(link):
    url= BASE + link[1:]
    links = search(url)
    return(links.find("div", {"class": "grade"}).text.strip())

# Gets most recent reviews
def get_reviews(link):
    links = search(BASE + link[1:])
    comments = links.find_all('p',"commentsParagraph")
    comments = [comment.text.strip() for comment in comments]
    return (comments)

# returns difficulty ranking
def get_difficulty(link):
    url= BASE + link[1:]
    links = search(url)
    difficult = links.find_all("div", {"class": "grade"})[2].text
    return(difficult.strip())

# Example try: print(get_difficulty(find_professor('Jesse Miller')))


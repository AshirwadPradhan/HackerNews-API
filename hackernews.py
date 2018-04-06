import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/'


def get_source():
    global URL
    try:
# getting the source code
        sc = requests.get(URL)
        if sc.status_code == 200:
            print('Retrieved Webpage')
            return sc.text
    except Exception:
        print('Cannot retrieve webpage {}'.format(URL))


def parse_source(number_of_links=10):
    sc = get_source()

# encoding the source
    sc = sc.encode('ascii', 'ignore')
    soup = BeautifulSoup(sc, 'html.parser')

# collecting all the news links
    a_links = soup.find_all('a', {'class' : 'storylink'})


    
# collecting top 10 links from a_links
    a_links_text = []
    for i,a_tags in enumerate(a_links):
        if i < number_of_links:
            a_links_text.append(a_tags.get_text())


# collecting the links of top 10 news
    a_links_link = []
    for i,a_tags in enumerate(a_links):
        if i < number_of_links:
            a_links_link.append(a_tags['href'])
        else:
            break


# collecting the score of top 10 news
    a_scores = soup.find_all('span', {'class': 'score'})
    a_links_score = []
    for i,score in enumerate(a_scores):
        if i < number_of_links:
            a_links_score.append(score.get_text())
        else:
            break
    

# collecting the time of addition of top 10 news
    a_span_time = soup.find_all('span', {'class': 'age'})
    a_link_time = []
    for i,ast in enumerate(a_span_time):
        if i < number_of_links:
            for child in ast.children:
                a_link_time.append(child.get_text())
        else:
            break
    print(a_link_time)



if __name__ == '__main__':
    parse_source()
import requests
from operator import itemgetter


def get_top_article_ids(num=20):
    """this function will return a list, containing id for top article"""
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    top_article_ids = r.json()
    return top_article_ids[:num + 1]


def get_article_detail(id):
    """return a dictionary that contains the details of an article
            the id passed in is article's id, which will be used to generate url
    """
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json'
    r = requests.get(url)
    return r.json()


def get_top_articles_detail():
    """returns a list of dictionaries of top articles"""
    top_article_ids = get_top_article_ids()
    articles_detail = []
    for article_id in top_article_ids:
        articles_detail.append(get_article_detail(article_id))

    return articles_detail


articles = get_top_articles_detail()

# sort articles by title
articles = sorted(articles, key=itemgetter('title'))
for article in articles:
    print(article['title'])

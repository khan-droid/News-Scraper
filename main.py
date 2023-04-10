#import what we need
from requests_html import HTMLSession
session = HTMLSession()

#use session to get the pagex

def get_data(topics):
    data = []
    for i in topics:
        r = session.get('https://news.google.com/search?q='+i+'&hl=en-GB&gl=GB&ceid=GB%3Aen')
        r.html.arender(timeout=20, sleep=1, scrolldown=0)
        articles = r.html.find('article')
        newslist = []
        for item in articles:
            # try:
                article = item.find('.MQsxIb', first=True)
                newsitem = article.find('h3', first=True)
                image = article.find('img', first=True).attrs['srcset'].split(',')[1]
                time = article.find('time',first=True).text
                title = newsitem.text
                link = newsitem.absolute_links
                newsarticle = {
                    'title': title,
                    'link': link,
                    'image': image,
                    'time' : time,
                }
                newslist.append(newsarticle)
            # except:
                
                # pass
        data.append(newslist)
    return data
def main():
    topics = ['rahul','upsc']
    news = get_data(topics)
    return news

if __name__ == '__main__':
    data = main()
    print(data)


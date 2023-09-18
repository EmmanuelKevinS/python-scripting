import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ea2131626e4849b585e82695e24d6a12')

content = r.json()
articles = content['articles']

#i=1

'''for article  in articles:
    print(f'Title {i}: ' , article['title'])
    i=i+1'''
'''for article in articles:
    source = article.get('source', {})  # Get the 'source' dictionary for each article
    name = source.get('name', 'Name not available')  # Get the 'name' value from 'source' if it exists
    print('name:', name)'''
   
   
#API key: ea2131626e4849b585e82695e24d6a12 
#https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ea2131626e4849b585e82695e24d6a12


def get_news(topic,from_date,to_date,api_key,language):
    api_key = 'ea2131626e4849b585e82695e24d6a12'
    website = (f'https://newsapi.org/v2/everything?q=Apple&from={from_date}&sortBy=popularity&apiKey={api_key}')
    r = requests.get(website)
    content = r.json()
    return content

news = get_news('c', '2023-09-17','c','ea2131626e4849b585e82695e24d6a12','c')
print(news)
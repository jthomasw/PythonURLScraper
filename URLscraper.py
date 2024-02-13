
from bs4 import BeautifulSoup                                               #libraries
import requests


def download_content(url):                                                   #downloads articles as individual files
    response = requests.get(url)
    if response.status_code == 200:                                         #checks connection to site
        soup = BeautifulSoup(response.content, 'html.parser')
        article_text = get_title(soup) + '\n' + get_author(soup) + '\n' + get_mainbody(soup)
        return article_text

    else:
        return "failed to scrape"

#title  
def get_title(soup):
    title_content = soup.title

    if title_content: #Extract text from the title content
            
            article_text =title_content.get_text()
            return article_text
    
    else:
        return "could not find title content"

#author
def get_author(soup):
    author_content = soup.find('div', class_='author-byline')

    if author_content: #Extract text from the author content
            
            article_text =author_content.get_text()
            return article_text
    
    else:
        return "could not find author content"
    
#mainbody
def get_mainbody(soup):                                     
    main_content = soup.find('div', class_='article-body')  #fox news format
    
    if main_content: #Extract text from the main content
            
            article_text = main_content.get_text()
            return article_text
    
    #main_content = soup.find('body', class_='page-prism-story')  abc news format

    #if main_content:
    #    article_text = main_content.get_text()
    #    return article_text
    #couldn't get abc news to work because their classes are random characters

    else:
            return "could not find main content"

def download_articles(file_path):
    with open(file_path, 'r') as file:                                      #downloads articles as individual files
        urls = file.readlines()
        for index, url in enumerate(urls):                                  #goes down the list of urls 1 at a time
            url = url.strip()
            content = download_content(url)                                 #takes content from url
            if content:                                                     #bool=t
                with open(f'article_{index+1}.txt', 'w') as article_file:
                    article_file.write(content)                             #writes content to n file, then loops n+1 to next article to write
                print(f"Article {index+1} download successful")
            else:                                                           #bool=f
                print(f"failed to download Article {index+1}")

if __name__ == "__main__":
    file_path = "url.txt"
    download_articles(file_path)


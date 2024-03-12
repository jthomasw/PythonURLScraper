"""
Module: Article Scrapper
"""

from bs4 import BeautifulSoup
import requests

def download_content(url):
    """
    Function to download article content from a URL.
    Args:
        str url : URL of the article.
    Returns:
        str: Content of the article.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_text =  get_mainbody(soup)
        return article_text
    else:
        return ""
    
##def get_title(soup):
##   title_content = soup.title
##    return title_content.get_text() if title_content else ""

##def get_author(soup):
##    author_content = soup.find('div', class_='author-byline')
##    return author_content.get_text() if author_content else ""

def get_mainbody(soup):
    """
    Function to extract the main body of the article.
    Args:
        BeautifulSoup soup : Parsed HTML content.
    Returns:
        str: Main body of the article.
    """
    main_content = soup.find('div', class_='article-body')
    return main_content.get_text() if main_content else ""

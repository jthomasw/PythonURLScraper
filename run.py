"""

Module: run

"""


from module_1 import file_handler
from module_2 import article_scraper

def download_articles(file_path):
    """
    This function downloads and stores atricles from URLs in the
    file
        Arguments:
        str file_path: string of the url 

    """
    urls = file_handler.read_urls(file_path)
    for index, url in enumerate(urls, start=1):
        content = article_scraper.download_content(url)
        if content:
            file_handler.write_article(index, content)
            print(f"Article {index} downloaded successfully")
        else:
            print(f"Failed to download Article {index}")

if __name__ == "__main__":
    file_path = "Data/raw/url.txt"
    download_articles(file_path)


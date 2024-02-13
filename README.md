Hello user,
URLscraper.py is a python script that takes in a file named url.txt, which has any amount of news article urls pasted into it.

Then the script scrapes the websites html code taking the title, author, and text from the site and writes it to a new file.

Libraries used-
requests
beautifulsoup4

Defining functions-

get_title(soup):
    Takes in soup argument which is using the beautiful soup function to pass in the content from the html.
    This function looks in the html code for the title tag then either returns the title string or "could not find title content"

get_author(soup):
    Takes in soup argument which is using the beautiful soup function to pass in the content from the html.
    This function looks in the html code for the div tag, then the class 'author-byline' and either returns the author string or "could not find author content"

get_mainbody(soup):
    Takes in soup argument which is using the beautiful soup function to pass in the content from the html.
    This function looks in the html code for the div tag, then the class 'article-body' and either returns the author string or "could not find article body content"

download_content(url):
    Takes in url argument which connects to website.
    Attempts to make connection to host, if successful in the article_text variable the contents of get_title(soup), get_author(soup), get_mainbody(soup). Then returns article_text. If unsucessful returns "failed to scrape"

download_articles(file_path):
    Takes in a file_path argument which is the file holding the urls. Opens the files and reads the urls. Next, it attempts to index through the urls getting their content using the download_content(url) function and places the data in the content variable. If succesful, it will create a new file called "article_{index}.txt" (with index being a numerical value), then for the corresponding url (the first url in url.txt is first article scraped) will print "Article {index} download successful". If unsuccessful then it will print "failed to download Article {index}"

Warning: As of this version, this code only works with articles from FOX news. 

"""
Module: File Handler
SOLID Principle: Single Responsibility Principle (SRP)
Benefit: This module is responsible only for handling 
         file-related operations, adhering to the SRP.
"""

def read_urls(file_path):
    """
    Function to read URLs from a file and return a list.
    Args:
        str file_path : Path to the file containing URLs.
    Returns:
        list: List of URLs.
    """
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def write_article(index, content):
    """
    Function to write article content to a file.
    Args:
        int index : Index of the article.
        str content: Content of the article.
    """
    with open(f"processed/article_{index}.txt", 'w') as article_file:
        article_file.write(content)
import os
from urllib.parse import urlparse

def get_file_extension(url):
    parsed_url = urlparse(url)
    url = parsed_url.path
    filename, file_extension = os.path.splitext(url)
    return file_extension

url = "https://example.com/txt/hello%20world.txt?v=9#python"

#print(get_file_extension(url))

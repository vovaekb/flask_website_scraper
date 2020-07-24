import os
import time
from bs4 import BeautifulSoup
import requests
import urllib.request
from app import app


def scrape_website(url):
    errors = []
    
    try:
        resp = urllib.request.urlopen(url)
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
        return {"error": errors}
    
    parser = 'html.parser'
    soap = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

    links = []
    for link in soap.find_all('a', href=True):
        links.append(link['href'])

    filename = 'links.txt'
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename), 'w') as f:
        for link in links:
            f.write(link + '\n')

    return filename

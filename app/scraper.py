import os
from bs4 import BeautifulSoup
import urllib.request
from app import app


def scrape_website(url):
    """Parses links from website and save to file
    
    Keyword arguments:
    url -- url of website to scrape
    Return: path to result file
    """
    errors = []
    
    try:
        resp = urllib.request.urlopen(url)
    except:
        errors.append(
            'Unable to get URL. Please make sure it's valid and try again.''
        )
        return {'error': errors}
    
    parser = 'html.parser'
    soap = BeautifulSoup(
        resp, 
        parser, 
        from_encoding=resp.info().get_param('charset')
    )

    links = []
    for link in soap.find_all('a', href=True):
        links.append(link['href'])

    # save links to file
    filename = 'links.txt'
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(
        basedir,
        app.config['UPLOAD_FOLDER'], filename
    )
    with open(file_path, 'w') as f:
        for link in links:
            f.write(link + '\n')

    return filename

import argparse
import requests
from datetime import datetime, timedelta
import os

def is_valid_pdf(url):
    if not url:
        print("URL is empty")
        return False
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type', '').lower()
        if response.status_code == 200 and 'application/pdf' in content_type:
            print(f"URL {url} is a valid PDF")
            return True
        else:
            print(f"URL {url} is not a valid PDF. Status code: {response.status_code}, Content-Type: {content_type}")
            return False
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False

def get_current_date():
    today = datetime.today()
    return today.strftime('%Y.%m.%d')

def get_date(year: int, month: int, day: int) -> str:
    try:
        return datetime(year, month, day).strftime('%Y.%m.%d')
    except ValueError as e:
        print(f"Error: {e}")
        return None

def genereate_rage_of_links(end_date: str):
    starting_date = get_current_date()
    date_str = starting_date
    list_of_links = []
    while date_str != end_date:
        base_pdf_url = f'https://apps.ioepa.com.br/Parauapebas/Busca/Arquivos/{date_str}.EDOMP.pdf'
        date_obj = datetime.strptime(date_str, '%Y.%m.%d')
        date_obj -= timedelta(days=1)
        date_str = date_obj.strftime('%Y.%m.%d')
        list_of_links.append(base_pdf_url)
    return list_of_links

def download_file(url, destination_folder='./downloaded_pdf_files'):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = url.split('/')[-1]
        filepath = f"{destination_folder}/{filename}"
        if os.path.exists(filepath):
            print(f"File already exists: {filepath}")
            return
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file: {filepath}")
    except requests.RequestException as e:
        print(f"Error downloading file from {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Download PDFs from a range of dates.')
    parser.add_argument('end_date', type=str, help='The end date in YYYY.MM.DD format')
    args = parser.parse_args()
    year, month, day = map(int, args.end_date.split('.'))
    end_date = get_date(year, month, day)

    links = genereate_rage_of_links(end_date)
    for link in links:
        if is_valid_pdf(link):
            download_file(link)

if __name__ == '__main__':
    main()
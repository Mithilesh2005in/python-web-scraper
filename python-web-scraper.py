# web_scraper.py
import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch and parse the webpage
def fetch_webpage(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract data from the parsed webpage
def extract_data(soup):
    data = []
    table = soup.find('table')  # Adjust based on the structure of the target webpage
    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')[1:]
    for row in rows:
        cells = row.find_all('td')
        data.append([cell.text for cell in cells])
    return headers, data

# Function to save data to a CSV file
def save_to_csv(headers, data, filename='data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    url = 'https://example.com/data'  # Replace with the actual URL
    soup = fetch_webpage(url)
    headers, data = extract_data(soup)
    save_to_csv(headers, data)

if __name__ == '__main__':
    main()

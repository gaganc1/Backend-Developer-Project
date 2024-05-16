import csv
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
   
    response = requests.get(url)
    
    if response.status_code == 200:
      
        soup = BeautifulSoup(response.text, 'html.parser')
       
        headings = soup.find_all('h1')
        
        # Create a list to hold the scraped data
        scraped_data = []
        
       
        for heading in headings:
            scraped_data.append(heading.text.strip())
        
        return scraped_data
    else:
        print("Failed to fetch the webpage")
        return None

def write_to_csv(data, filename):
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Heading'])
        writer.writerows(zip(data))

if __name__ == "__main__":
    
    url = input("Enter the URL to scrape: ")
    
    scraped_data = scrape_website(url)
    
    if scraped_data:
        write_to_csv(scraped_data, 'scraped_data.csv')
        print("Scraped data has been saved to 'scraped_data.csv'")

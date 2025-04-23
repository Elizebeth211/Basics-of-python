import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("https://books.toscrape.com/")
print(response)
print(response.content)
print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)
print(soup.prettify)

# Find all book containers on the page
books = soup.find_all('article', class_='product_pod')

# Loop through each book and extract the title and price
for book in books:
    # Extract the title (stored in the 'title' attribute of the <a> tag inside <h3>)
    title = book.find('h3').find('a')['title']
    
    # Extract the price (stored in the <p> tag with class 'price_color')
    price = book.find('p', class_='price_color').text
    
    # Print the title and price
    print(f"Title: {title}, Price: {price}")



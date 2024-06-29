import requests
from bs4 import BeautifulSoup
import time
import random
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "specialoffer.settings")
django.setup()

from website.models import Product

# Headers and URL
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

# Initialize variables
proceed = True
current_page = 0

while proceed:
    # Construct the URL dynamically based on the current page
    url = f"https://www.rossmann.de/de/angebote/m/angebote?q=angebote%3A&page={current_page}&pageSize=60#"
    
    # Send GET request
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'

    # Check if the request was successful
    if r.status_code != 200:
        print(f"Failed to retrieve page {current_page}. Status code: {r.status_code}")
        break

    # Parse the HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # Select the grid content items
    items = soup.select('div.rm-grid__content div.rm-tile-product')

    # Check if no items are found, then stop the loop
    if not items:
        proceed = False
        break

    for item in items:
        product_name = item.get('data-product-name', 'N/A')
        product_number = item.get('data-product-id', 'N/A')
        product_number_2 = item.get('data-product-id2', 'N/A')
        currency = item.get('data-product-currency', 'N/A')
        price = item.get('data-product-price', 'N/A')
        brand_name = item.get('data-product-brand', 'N/A')

        # Extract the product webpage URL
        a_tag = item.find('a', href=True)
        product_url = f"https://www.rossmann.de{a_tag['href']}" if a_tag else 'N/A'

        # Extract the image URL
        img_tag = item.find('img', class_='rm-tile-product__image')
        img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else 'N/A'

        # Save product info to the database
        Product.objects.create(
            product_name=product_name,
            product_number=product_number,
            product_number_2=product_number_2,
            currency=currency,
            price=price,
            brand_name=brand_name,
            product_url=product_url,
            product_picture_url=img_url
        )

    # Random sleep to avoid detection
    time.sleep(1 + random.random() * 2)

    # Increment the current page to fetch the next page
    current_page += 1

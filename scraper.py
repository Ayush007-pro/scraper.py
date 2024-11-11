import requests
from bs4 import BeautifulSoup
import sys

url = input("Enter the url: ")

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/58.0.3029.110 Safari/537.3'
    )
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    sys.exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

page_title = soup.title
print("Page Title:", page_title.get_text() if page_title else "No title found.")

first_p_tag = soup.find('p')
if first_p_tag:
    print("\nFirst <p> Tag:")
    print(first_p_tag)
    print("\nPrettified <p> Tag:")
    print(first_p_tag.prettify())
    print("\nClasses of <p> Tag:", first_p_tag.get('class', 'No class attribute.'))
    print("\nText within <p> Tag:")
    print(first_p_tag.get_text())
else:
    print("\nNo <p> tag found.")

first_div_tag = soup.find('div')
if first_div_tag:
    print("\nFirst <div> Tag:")
    print(first_div_tag)
    print("\nPrettified <div> Tag:")
    print(first_div_tag.prettify())
    print("\nClasses of <div> Tag:", first_div_tag.get('class', 'No class attribute.'))
    print("\nText within <div> Tag:")
    print(first_div_tag.get_text())
else:
    print("\nNo <div> tag found.")

if first_div_tag:
    cleaned_text = ''
    text_list = list(first_div_tag.get_text())
    i = 0
    while i < len(text_list) - 1:
        if text_list[i] == '\n':
            if text_list[i + 1] != '\n':
                cleaned_text += text_list[i]
            i += 1
        else:
            cleaned_text += text_list[i]
        i += 1
    print("\nCleaned Text from <div> Tag:")
    print(cleaned_text)
else:
    print("\nNo <div> tag to clean text from.")

all_p_tags = soup.find_all('p')
print(f"\nTotal <p> Tags Found: {len(all_p_tags)}")
for index, p in enumerate(all_p_tags, start=1):
    print(f"\n<p> Tag {index}:")
    print(p)

all_a_tags = soup.find_all('a')
print(f"\nTotal <a> Tags Found: {len(all_a_tags)}")
for index, a in enumerate(all_a_tags, start=1):
    href = a.get('href', 'No href attribute.')
    print(f"\n<a> Tag {index}:")
    print(f"Href: {href}")
    print(f"Link Text: {a.get_text()}")

description_p_tags = soup.find_all('p', class_='description')
print(f"\nTotal <p> Tags with class 'description': {len(description_p_tags)}")
for index, p in enumerate(description_p_tags, start=1):
    print(f"\n<p> Tag {index} with class 'description':")
    print(p.get_text())

multi_class_elements = soup.find_all(class_='form-select-lg form-select eduvibe-search-popup-select')
print(f"\nTotal Elements with specified classes: {len(multi_class_elements)}")
for index, element in enumerate(multi_class_elements, start=1):
    print(f"\nElement {index}:")
    print(element)

option_values = [91, 380]
for value in option_values:
    option_tags = soup.find_all('option', value=value)
    print(f"\n<option> Tags with value='{value}': {len(option_tags)}")
    for idx, option in enumerate(option_tags, start=1):
        print(f"Option {idx}: {option.get_text()}")

anchors = soup.find_all('a')
unique_links = set()

for link in anchors:
    href = link.get('href')
    if href and href != '#':
        if href.startswith('http'):
            unique_links.add(href)
        else:
            full_url = requests.compat.urljoin(url, href)
            unique_links.add(full_url)

print(f"\nTotal Unique Links Found: {len(unique_links)}")
for link in unique_links:
    print(link)

images = soup.find_all('img')
image_urls = set()

for img in images:
    src = img.get('src')
    if src:
        if src.startswith('http'):
            image_urls.add(src)
        else:
            full_url = requests.compat.urljoin(url, src)
            image_urls.add(full_url)

print(f"\nTotal Images Found: {len(image_urls)}")
for img_url in image_urls:
    print(img_url)

from bs4 import BeautifulSoup

with open('element.txt', 'r', encoding='utf-8') as r:
    html_content = r.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Open a file to write the mapping of names to image links with UTF-8 encoding
with open('output.txt', 'w', encoding='utf-8') as file:
    # Find all grid items
    grid_items = soup.find_all('div', class_='grid-item--rJBK1')

    for item in grid_items:
        # Extract name and image link
        name = item.find('div', class_='name--QRAI9').text.strip()
        image_link = item.find('img')['src'].strip()

        # Write to the file
        file.write(f"{name}: {image_link}\n")

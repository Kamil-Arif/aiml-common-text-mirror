import requests
from bs4 import BeautifulSoup
import hashlib
from urllib.parse import urlparse
import os 
visited = []

def get_unique_file_name(url: str):
    path = url.split("//")[1].split('/')
    if ':' in path[-1]:
        return url[7:] #intentionally cause an error
    if '.' not in path[-1]:
        hashed_url = hashlib.sha256(url.encode()).hexdigest()
        path.append(f"index_{hashed_url}.html")
    path = '/'.join(path[:-1])
    if len(path) == 0:
        if os.path.exists(os.path.join("pantelis.github.io", "index.html")):
            return os.path.join("pantelis.github.io", "index.html")
        else:
            hashed_url = hashlib.sha256(url.encode()).hexdigest()
            return os.path.join("pantelis.github.io", f"misc_page_{hashed_url}.html")
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    return url.split("//")[1]

def get_links(url, depth, base_url):
    if 'pantelis.github.io' not in url or len(url) == 0:
        return []
    if url in visited:
        return [url]

    # Send a GET request to the URL, allow up to 10 redirects
    try:
        response = requests.get(url)
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
    except:
        return []
    
    visited.append(url)

    file_path = get_unique_file_name(url)
    try:
        if os.path.exists(file_path):
            print(f"File for {url} already exists.")
        else:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(response.text)
    except Exception as e:
        print(f"Failed to write file {file_path} for {url}. This might not be a bad thing.")

    # Find all anchor tags and extract the href attribute
    links = [link.get('href') for link in soup.find_all('a')]

    # Combine all links into a single list
    all_links = links #+ scripts + stylesheets + forms

    for i, link in enumerate(all_links):
        if link == None or len(link) == 0 or link[0] == '#' or link[0] == '.':
            all_links[i] = None
            continue
        elif link[0] == '/':
            #relative URL
            all_links[i] = base_url + link
        elif link.startswith(base_url):
            all_links[i] = link
        else:              
            all_links[i] = base_url + "/" + link
    
    all_links.append(url)
    all_links = list(set(all_links))
    all_links = [link for link in all_links if link is not None]

    print(depth, len(all_links), url)

    if depth == 0:
        return all_links
    else:
        final_links = all_links.copy()
        for i, link in enumerate(all_links):
            if link == None:
                continue
            if 'pantelis.github.io' not in link:
                continue
            final_links.append(link)
            final_links += get_links(link, depth-1, base_url)
            print(f" - {depth} // {i} : {len(final_links)}")
        return list(set(final_links))

all_links = get_links('https://pantelis.github.io/data-mining/intro.html', 2, 'https://pantelis.github.io')
all_links = get_links('https://pantelis.github.io', 2, 'https://pantelis.github.io')
all_links = list(set(all_links))
# Print the links
print(all_links)
print(len(all_links))

with open('links.txt', 'w', encoding='utf-8') as f:
    for item in all_links:
        f.write("%s\n" % item)
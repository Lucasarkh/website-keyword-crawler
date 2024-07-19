import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd
from colors import color, green

page_counter = 0

def crawl_page(url, results, key_words, visited_pages):
    global page_counter
    try:
        page_counter += 1
        print(f"page number: {page_counter} --- {url}")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        def find_key_word(element, tag):
            for key_word in key_words:
                if key_word.lower() in element.get_text().lower():
                    results[key_word].append((url, tag, element.get_text(strip=True)))
                    print(green(f"keyword found: {key_word} em {url} (Tag: {tag})"))

        for tag in ['title', 'h1', 'h2', 'h3', 'p', 'span', 'li']: #YOU CAN ADD A TAG HERE
            for element in soup.find_all(tag):
                find_key_word(element, tag)

        links = soup.find_all('a', href=True)
        links = [urljoin(url, link['href']) for link in links]

        links = [link for link in links if urlparse(link).netloc == urlparse(url).netloc and "?" not in link and "upload" not in link.lower() and "#" not in link and "http://" not in link ] #URL VARIABLES TO NOT CONSIDER

        for link in links:
            if link not in visited_pages:
                visited_pages.add(link)
                crawl_page(link, results, key_words, visited_pages)

    except requests.exceptions.RequestException as e:
        print(f"HTTP request error at: {url}: {e}")

    except Exception as e:
        print(f"Error {url}: {e}")

def find_keywords_in_site(first_url, key_words):
    results = {key_word: [] for key_word in key_words}
    visited_pages = set()

    def wrapper_crawl_page(url):
        crawl_page(url, results, key_words, visited_pages)

    crawl_page(first_url, results, key_words, visited_pages)

    return results, visited_pages

def export_to_excel(results, visited_pages):
    data = []
    for key_word, occurrences in results.items():
        for url, tag, context in occurrences:
            data.append({'keyword': key_word, 'URL': url, 'Tag': tag, 'Context': context})

    df_results = pd.DataFrame(data)
    df_visited_pages = pd.DataFrame({'All pages': list(visited_pages)})

    with pd.ExcelWriter('results.xlsx') as writer:
        df_results.to_excel(writer, sheet_name='Pages with keywords', index=False)
        df_visited_pages.to_excel(writer, sheet_name='All pages', index=False)

if __name__ == "__main__":
    site_url = "https://" # INSERT URL HERE
    wanted_key_words = ["example_1", "example_2"] #ARRAY OF KEYWORDS

    results, visited_pages = find_keywords_in_site(site_url, wanted_key_words)

    if any(results.values()):
        print("\nresults:")
        for key_word, occurrences in results.items():
            print(f"\nPages with requested keywords '{key_word}':")
            for url, tag, context in occurrences:
                print(f"URL: {url}, Tag: {tag}, Context: {context}")

        export_to_excel(results, visited_pages)
        print("\nExported to 'results.xlsx'")
    else:
        print("\nThe search was stopped or none of the keywords were found on any of the analyzed pages.")

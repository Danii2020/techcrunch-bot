from bs4 import BeautifulSoup
import requests
BASE_URL = 'https://www.techcrunch.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
def load_bs_object(url):
    response = requests.get(url, headers=HEADERS)
    return BeautifulSoup(response.text, 'html.parser')
def scrape_posts_links():
    soup = load_bs_object(BASE_URL)
    posts_headers = soup.find_all('h3', attrs={"class": "loop-card__title"})
    return [element.find('a')['href'] for element in posts_headers][:10]
def scrape_posts_content():
    posts_list = []
    posts_links = scrape_posts_links()
    for link in posts_links:
        try:
            post_soup = load_bs_object(link)
            post_title = post_soup.find('h1', attrs={"class": "wp-block-post-title"}).text.strip()
            post_content_container = post_soup.find('div', attrs={"class": "wp-block-post-content"})
            post_paragraphs = post_content_container.find_all('p', attrs={"class": "wp-block-paragraph"})
            post_content = ' '.join(paragraph.text for paragraph in post_paragraphs)
            posts_list.append({
                "title" : post_title,
                "content": post_content
            })
        except Exception as e:
            print(f"Error: {e}")
            continue
    return posts_list

from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n") # Extract text
    return text.strip()

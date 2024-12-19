from network import fetch_page
from parser import parse_html

class Navigator:
    def __init__(self):
        self.history = [] # Each entry: { 'url': str, 'content': str }
        self.current_index = -1

    def load_page(self, url):
        html = fetch_page(url)
        if html is not None:
            text = parse_html(html)
            self.history = self.history[:self.current_index+1] # if we load a new page, discard any forward history
            self.history.append({'url': url, 'content': text})
            self.current_index += 1

    def go_back(self):
        if self.current_index > 0:
            self.current_index -= 1

    def go_forward(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1

    def get_current_page_content(self):
        if self.current_index == -1 or self.current_index >= len(self.history):
            return None
        return self.history[self.current_index]['content']

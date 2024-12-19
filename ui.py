import textwrap
from bs4 import BeautifulSoup

class UI:
    def get_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_help(self):
        # Provide a cleaner, more aligned help message
        help_text = (
            "Available commands:\n"
            "  open <url>    - Open a webpage\n"
            "  back          - Go back in history\n"
            "  forward       - Go forward in history\n"
            "  help          - Show this help message\n"
            "  quit          - Exit shello\n"
        )
        print(help_text)
    
    def display_page(self, content):
        if content is None:
            print("No page loaded.")
            return

        soup = BeautifulSoup(content, "html.parser")

        header = soup.find('header')
        if header:
            header.decompose()

        footer = soup.find('footer')
        if footer:
            footer.decompose()

        text = soup.get_text(separator="\n").strip()

        print("----- PAGE CONTENT START -----")

        wrapper = textwrap.TextWrapper(width=80)
        wrapped_lines = wrapper.wrap(text)

        for line in wrapped_lines:
            print("  " + line)

        print("----- PAGE CONTENT END -----")

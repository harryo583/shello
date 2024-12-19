class UI:
    def get_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_help(self):
        help_text = """
                    Available commands:
                    open <url>    - Open a webpage
                    back          - Go back in history
                    forward       - Go forward in history
                    help          - Show this help message
                    quit          - Exit the browser
                    """
        print(help_text)

    def display_page(self, content):
        if content is None:
            print("No page loaded.")
        else:
            print("----- PAGE CONTENT START -----")
            print(content)
            print("----- PAGE CONTENT END -----")

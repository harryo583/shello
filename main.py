from ui import UI
from navigator import Navigator

def main():
    navigator = Navigator()
    ui = UI()

    ui.display_message("Welcome to shello! Type 'help' for commands.")

    # main loop
    while True:
        command = ui.get_input("shello> ")

        if command.startswith("open "):
            url = command.split(" ", 1)[1]
            navigator.load_page(url) # load page using navigator
            page_content = navigator.get_current_page_content()
            ui.display_page(page_content)

        elif command == "back":
            navigator.go_back()
            ui.display_page(navigator.get_current_page_content())

        elif command == "forward":
            navigator.go_forward()
            ui.display_page(navigator.get_current_page_content())

        elif command == "help":
            ui.display_help()

        elif command == "quit":
            ui.display_message("Goodbye!")
            break

        else:
            ui.display_message("Unknown command. Type 'help' for assistance.")

if __name__ == "__main__":
    main()

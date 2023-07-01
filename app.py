import commands


def print_options(options: dict):
    """Prints out the options to the user
    """
    for shortcut, option in options.items():
        print(f'({shortcut})', option)
    print()


def get_option_choice(options: dict):
    """Gets the option from user
    """
    while True:
        choice = input('Plase select an option: ').upper()

        if choice not in options.keys():
            print('Invalid choice!')
            print_options(options)

        else:
            break

    choice = options.get(choice)
    choice()


def get_user_input(label: str, required=True):
    """Gets inputs from user
    """
    value = input(f'{label}: ') or None

    while required and not value:
        value = input(f'{label}: ') or None

    return value


def get_new_bookmark_data():
    """Gets data from new bookmarks
    """
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False)
    }


def get_bookmark_id_for_deletion():
    """Gets id for bookmark's delete
    """
    return get_user_input('Enter a bookmark ID to delete')


class Option:
    """These class holds the logic to be executed when a user choose an option.
    """

    def __init__(self, name_to_display: str, command, preparation_step=None) -> None:
        self.name_to_display = name_to_display
        self.command = command
        self.preparation_step = preparation_step

    def __call__(self):
        data = self.preparation_step() if self.preparation_step else None

        if data:
            message = self.command.execute(data)

        else:
            message = self.command.execute()

        print(message)

    def __str__(self) -> str:
        return self.name_to_display


if __name__ == "__main__":
    commands.CreateBookmarksTableCommand().execute()

    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(), get_new_bookmark_data),
        'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand(), get_bookmark_id_for_deletion),
        'Q': Option('Quit', commands.QuitCommand())
    }

    print_options(options=options)
    get_option_choice(options=options)

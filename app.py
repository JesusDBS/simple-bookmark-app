import commands


def print_options(options: dict):
    """Prints out the options to the user
    """
    for key, val in options.items():
        print(f'({key})', val)


class Options:
    """These class holds the logic to be executed when a user choose an option.
    """

    def __init__(self, name_to_display: str, command, preparation_step=None) -> None:
        self.name_to_display = name_to_display
        self.command = command
        self.preparation_step = preparation_step

    # def get_preparation_step_data(self):
    #     """Takes data from user
    #     """
    #     keys = ['title', 'url', 'notes', 'date_added']

    #     message = """Please provide the info in the following order:
    #         1) bookmark's title
    #         2) bookmark's URL
    #         3) bookmark's notes
    #         4) bookmark's creation date\n
    #     """
    #     print(message)

    #     user_input = input(
    #         "Please give the bookmark info separated by one space: ")

    #     values = [value.strip() for value in user_input.split(' ') if value]

    #     self.data = dict(zip(keys, values))

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
        'A': 'Add a bookmark',
        'B': 'List bookmarks by date',
        'T': 'List bookmarks by title',
        'D': 'Delete a bookmark',
        'Q': 'Quit'
    }

    print_options(options=options)

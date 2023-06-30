from database import DatabaseManager

db = DatabaseManager(db_filename='bookmark.db')

class CreateBookmarksTableCommand:
    """This class creates the bookmarks table
    """
    table_name = 'bookmarks'
    columns = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'title': 'TEXT NOT NULL',
        'url': 'TEXT NOT NULL',
        'notes': 'TEXT',
        'date_added': 'TEXT NOT NULL'
    }

    @classmethod
    def execute(cls):
        """Creates bookmarks table
        """
        table_name = cls.table_name
        columns = cls.columns

        db.create_table(
            table_name=table_name,
            columns=columns
        )
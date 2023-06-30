from datetime import datetime
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


class AddBookmarkCommand:
    """This class adds new bookmarks into the database
    """
    date_added = datetime.utcnow().isoformat()
    table_name = 'bookmarks'

    @classmethod
    def execute(cls, data: dict) -> str:
        """Creates bookmarks records
        """
        assert isinstance(data, dict), f'data: {data} must be a dictionary!'

        if 'date_added' in data.keys():
            data['date_added'] = cls.date_added

        else:
            data.update(
                {'date_added': cls.date_added}
            )

        db.create_record(
            table_name=cls.table_name,
            columns_values=data
        )

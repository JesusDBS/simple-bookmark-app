import os
import sqlite3


class DatabaseManager:
    """This class manages the operations of the database.
    """

    def __init__(self, db_filename) -> None:

        if os.path.isfile(db_filename):
            self.__connection = sqlite3.connect(db_filename)

    def __del__(self):
        self.__connection.close()

    def _execute(self, statement: str, values=None):
        with self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name: str, columns: dict):
        """Creates a table in database.
        """
        columns_with_type = []
        for column_name, column_type in columns.items():
            columns_with_type.append(
                f'{column_name} {column_type}'
            )

        SQL_CREATE_STATEMENT = f'''
                        CREATE TABLE IF NOT EXISTS {table_name}
                        ({', '.join(columns_with_type)});
                        '''

        self._execute(SQL_CREATE_STATEMENT)

    def create_record(self, table_name: str, columns_values: dict):
        """Creates records in the database
        """
        placeholders = ', '.join('?'*len(columns_values))
        columns_names = ', '.join(columns_values.keys())
        columns_values = tuple(columns_values.values())

        SQL_INSERT_STATEMENT = f'''
                            INSERT INTO {table_name}
                            ({columns_names})
                            VALUES ({placeholders});
                            '''
        self._execute(SQL_INSERT_STATEMENT, values=columns_values)

    def delete_records(self, table_name:str, columns_values: dict, criteria: str):
        """Deletes records from the database
        """
        placeholders = [f'{column_name} = ?' for column_name in columns_values.keys()]
        delete_criteria = f' {criteria} '.join(placeholders)
        values = tuple(columns_values.values(()))

        SQL_DELETE_STATEMENT = f'''
                            DELETE FROM {table_name}
                            WHERE {delete_criteria};
                                '''
        self._execute(SQL_DELETE_STATEMENT, values=values)

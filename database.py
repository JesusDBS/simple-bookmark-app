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
        columns_with_type =[]
        for column_name, column_type in columns.items():
            columns_with_type.append(
                f'{column_name} {column_type}'
            )
        
        SQL_STATEMENT = f'''
                        CREATE TABLE IF NOT EXISTS {table_name}
                        ({', '.join(columns_with_type)});
                        '''
        
        self._execute(SQL_STATEMENT)

        
#########################################################################################
# Caution: Decompressing a chat's .db will result in a .db approximately thrice as heavy.
#########################################################################################


import sqlite3
import zlib


def decompress_db(compressed_db_path, decompressed_db_path):
    compressed_connection = sqlite3.connect(compressed_db_path)
    decompressed_connection = sqlite3.connect(decompressed_db_path)
    compressed_cursor = compressed_connection.cursor()
    decompressed_cursor = decompressed_connection.cursor()
    compressed_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = compressed_cursor.fetchall()
    for table in tables:
        table_name = table[0]
        compressed_cursor.execute(f"PRAGMA table_info({table_name})")
        columns = compressed_cursor.fetchall()
        column_defs = [f"{col[1]} {col[2]}" for col in columns]
        create_table_query = f"CREATE TABLE {table_name} ({', '.join(column_defs)})"
        decompressed_cursor.execute(create_table_query)
        compressed_cursor.execute(f"SELECT * FROM {table_name}")
        rows = compressed_cursor.fetchall()
        placeholders = ", ".join(["?" for _ in columns])
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        for row in rows:
            new_row = list(row)
            for i, col in enumerate(columns):
                col_name = col[1]
                if (table_name == "details" and col_name in ["chat", "chat_full"]) or \
                        (table_name == "messages" and col_name == "message") or \
                        (table_name == "participants" and col_name == "user"):
                    if new_row[i] is not None:
                        try:
                            new_row[i] = zlib.decompress(new_row[i]).decode()
                        except zlib.error:
                            pass
            decompressed_cursor.execute(insert_query, new_row)
    decompressed_connection.commit()
    compressed_connection.close()
    decompressed_connection.close()

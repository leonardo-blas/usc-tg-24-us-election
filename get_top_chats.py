"""
Using chats.db to determine the top N chats based on unique incoming edges (an influence proxy metric).
By default, N = 500. If desired, change N on top_n_chats.
Note that not all chats in chats.db have been scraped, and that the list may change as the scraping continues.
Will output N "chat: unique incoming edge count" lines in a .txt.
Sample:
channel_1179270258: 2910
channel_2066575222: 1963
channel_1956613416: 1924
"""


import sqlite3
from collections import defaultdict


top_n_chats = 500
chats_path = "chats.db"
with sqlite3.connect(chats_path) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT parent, type_and_id FROM chats")
    rows = cursor.fetchall()

incoming_edges_dictionary = defaultdict(set)
for row in rows:
    parent, type_and_id = row[0], row[1]
    if type_and_id:
        incoming_edges_dictionary[type_and_id].add(parent)

incoming_edges_dictionary = {node: list(edges) for node, edges in incoming_edges_dictionary.items()}
incoming_edge_counts = [(node, len(edges)) for node, edges in incoming_edges_dictionary.items()]
incoming_edge_counts.sort(key=lambda x: x[1], reverse=True)
top_chats = incoming_edge_counts[:top_n_chats]
with open("top_chats.txt", "w") as f:
    f.writelines(f"{chat[0]}: {chat[1]}\n" for chat in top_chats)

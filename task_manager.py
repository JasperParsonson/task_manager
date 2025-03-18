import sqlite3 # imports the sqlite3 module.

conn = sqlite3.connect("tasks.db") # connects to the SQLite database.
cursor = conn.cursor() # creates a cursor object.

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        category TEXT,
        status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending'
    )
""")
# Save and close connection
conn.commit()
conn.close()

print("Database setup complete!")
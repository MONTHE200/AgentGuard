import sqlite3


connection = sqlite3.connect("resources/database.sqlite")


cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS systems (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    environment TEXT NOT NULL,
    status TEXT NOT NULL
)
""")


cursor.execute("""
INSERT INTO systems (name, environment, status)
VALUES
    ('CRM', 'production', 'active'),
    ('HR-Portal', 'production', 'active'),
    ('Monitoring', 'production', 'active')
""")


connection.commit()


connection.close()


print("Database created successfully.")
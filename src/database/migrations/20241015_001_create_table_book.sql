CREATE TABLE Book 
( 
    id TEXT PRIMARY KEY NOT NULL, 
    title TEXT UNIQUE NOT NULL,
    author TEXT,
    gender TEXT,
    indicate_rating INTEGER NOT NULL,
    number_of_pages INTEGER NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);
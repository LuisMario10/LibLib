CREATE TABLE BookLoan 
(
    id TEXT PRIMARY KEY NOT NULL,
    book TEXT NOT NULL,
    client TEXT NOT NULL,
    loan_date TEXT DEFAULT (datetime('now')),
    return_date TEXT,
    FOREIGN KEY (book) REFERENCES Book(id),
    FOREIGN KEY (client) REFERENCES Client(id)
);
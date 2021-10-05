CREATE TABLE ownership(
  id INTEGER PRIMARY KEY NOT NULL,
  user_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  symbol TEXT NOT NULL,
  shares INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id)
);
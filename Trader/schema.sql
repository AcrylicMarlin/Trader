CREATE TABLE IF NOT EXISTS user_data (
    user INTEGER PRIMARY KEY,
    user_name TEXT UNIQUE
    infrastructure INTEGER NOT NULL,
    artifact_name TEXT NOT NULL UNIQUE,
    artifact_value FLOAT NOT NULL,
    currency FLOAT NOT NULL
);
CREATE TABLE IF NOT EXISTS infrastructure (
    user INTEGER,
    coal_mines INTEGER,
    FOREIGN KEY (user) REFERENCES user_data(user)
);
CREATE TABLE IF NOT EXISTS materials (
    user INTEGER,
    coal FLOAT,
    FOREIGN KEY (user) REFERENCES user_data(user)
);
SELECT {1}
FROM user_data
WHERE user=={2};
INSERT INTO user_data
WHERE user=={1}
VALUES (
    user={1},
    infrastructure={2},
    artifact_name={3},
    artifact_value={4},
    currency={5}
)



CREATE_USER_TABLE:
CREATE TABLE IF NOT EXISTS user_data (user INTEGER PRIMARY KEY, user_name TEXT UNIQUE, artifact_name TEXT NOT NULL UNIQUE, artifact_value FLOAT NOT NULL, currency FLOAT NOT NULL);
CREATE_INFRASTRUCTURE_TABLE:
CREATE TABLE IF NOT EXISTS infrastructure (user INTEGER, coal_mines INTEGER, FOREIGN KEY (user) REFERENCES user_data(user));
CREATE_MATERIALS_TABLE:
CREATE TABLE IF NOT EXISTS materials (user INTEGER, coal FLOAT, FOREIGN KEY (user) REFERENCES user_data(user));
SELECT_USER:
SELECT {1} FROM user_data WHERE user=={2};
SELECT_INFRASTRUCTURE:
SELECT {1} FROM infrastructure WHERE user=={2};
SELECT_MATERIALS:
SELECT {1} FROM materials WHERE user=={2};
INSERT_USER:
INSERT INTO user_data VALUES (user={1}, user_name={2}, artifact_name={3}, artifact_value={4}, currency={5});
INSERT_INFRASTRUCTURE:
INSERT INTO infrastructure 
VALUES (user={1}, coal_plants={2});
INSERT_MATERIALS:
INSERT INTO materials 
VALUES (user={1}, coal={2});
MODIFY_INFRASTRUCTURE:
UPDATE TABLE infrastructure WHERE user=={1} VALUES (user={2}, coal_plants={3});
MODIFY_MATERIALS:
UPDATE TABLE materials WHERE user=={1} VALUES (user={2}, coal={3});
MODIFY_USER:
UPDATE TABLE user_data WHERE user=={1} VALUES (artifact_value={2}, currency={3})
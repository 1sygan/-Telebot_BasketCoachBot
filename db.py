import sqlite3
import time


class Database:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

# TODO регистрация пользователя в БД
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

# TODO Проверка наличия пользователя в БД
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

# TODO ник нейм пользователя в БД
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?",(nickname, user_id,))

# TODO проверка стадии регистрации пользователя
    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

# TODO изменение стадии регистрации пользователя
    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?",(signup, user_id,))

# TODO получить пользователя
    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT nickname FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                nickname = str(row[0])
            return nickname

# TODO изменить переменную в БД
    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE users SET time_sub = ? WHERE user_id = ?", (time_sub, user_id,))

# TODO получить переменной из БД
    def get_time_sub(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            return time_sub

# TODO получить статус подписки пользователя
    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub > int(time.time()):
                return True
            else:
                return False

# TODO получение списка команд и ссылок
    def get_teams(self):
        with self.connection:
            result = self.cursor.execute("SELECT id, teams FROM teams_nba", ()).fetchall()
            data = {}
            for row in result:
                teams = tuple(row[1].split())
                data[row[0]] = teams
            return data

# TODO возрат значения с изпользованием id
    def get_teams_link(self, teams_link_id):
        with self.connection:
            return self.cursor.execute("SELECT teams_link FROM teams_nba WHERE id = ?", (teams_link_id,)).fetchone()[0]


import sqlite3


class SQL:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_questions(self, answered=True):
        # Возвращает список из вопросов, на которые есть ответы/нет ответа(True/False)
        with self.connection:
            return self.cursor.execute("SELECT * FROM `faq` WHERE `answered` = ?", (answered,)).fetchall()

    def add_question(self, question, answered=False):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `faq` (`question`, `answered`) VALUES(?,?)",
                (question, answered))

    def set_answer(self, question, answer, answered=True):
        with self.connection:
            return self.cursor.execute("UPDATE `faq` SET `answer` = ?, `answered` = ? WHERE `question` = ?",
                                       (answer, answered, question))

    def set_keywords(self, question, keywords):
        with self.connection:
            return self.cursor.execute("UPDATE `faq` SET `key_words` = ? WHERE `question` = ?", (keywords, question))

    def close(self):
        self.connection.close()

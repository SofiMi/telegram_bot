import sqlite3

class SQL:
    """Класс, отвечающий за коммуникацию с БД"""
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_question(self, question, answered, key_words, answer):
        """Функция, которая добавляет новый вопрос"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `faq` (`question`, `answered`, `key_words`, `answer`) VALUES(?,?,?,?)",
                (question, answered, key_words, answer))

    def update_answer(self, question, answer, answered=True):
        """Функция, которая изменяет ответ на вопрос"""
        with self.connection:
            return self.cursor.execute("UPDATE `faq` SET `answer` = ?, `answered` = ? WHERE `question` = ?",
                                       (answer, answered, question))

    def update_question(self, question, answer):
        """Функция, которая изменяет вопрос"""
        with self.connection:
            return self.cursor.execute("UPDATE `faq` SET `question` = ? WHERE `answer` = ?",
                                       (question, answer))

    def set_keywords(self, question, keywords):
        """Изменяет ключевые слова"""
        with self.connection:
            return self.cursor.execute("UPDATE `faq` SET `key_words` = ? WHERE `question` = ?", (keywords, question))

    def dict_factory(self):
        """Возвращает массив, состоящий из ключевых слов"""
        self.connection.row_factory = sqlite3.Row
        self.cursor.execute("SELECT key_words, question, answer  FROM faq")

        list_word = []
        for res in self.cursor:
           list_word.append(list(res))
        return list_word

    def close(self):
        """Закрывает базу данных"""
        self.connection.close()



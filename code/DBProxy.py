import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        # Inicializa a conexão com o banco de dados
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        # Insere um novo registro na tabela 'dados'
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        # Faz o commit para salvar no banco de dados
        self.connection.commit()

    def retrieve_top10(self) -> list:
        # Retorna os 10 melhores registros (maior pontuação) da tabela 'dados'
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        # Fecha a conexão com o banco de dados
        return self.connection.close()

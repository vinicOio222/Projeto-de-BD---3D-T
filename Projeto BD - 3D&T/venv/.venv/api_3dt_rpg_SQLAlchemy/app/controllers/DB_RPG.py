import sqlite3 as sql

class DataBase:
    def __init__(self, db_name = "3D&T.db"):
        self.conn = sql.connect("api_3dt_rpg\\app\\database\\" + db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        tabela_usuario = '''
            CREATE TABLE IF NOT EXISTS "Usuario" (
                "Email" TEXT PRIMARY KEY,
                "Username" TEXT NOT NULL UNIQUE,
                "Nome" TEXT NOT NULL UNIQUE,
                "Senha" TEXT NOT NULL UNIQUE
            );'''

        tabela_mesa = '''
            CREATE TABLE IF NOT EXISTS "Mesa"(
                "Nome_Mesa" TEXT NOT NULL,
                "ID_Mesa" INTEGER PRIMARY KEY AUTOINCREMENT,
                "Mestre" TEXT NOT NULL,
                FOREIGN KEY ("Mestre") REFERENCES "Usuario"("Email") ON DELETE CASCADE ON UPDATE CASCADE

            );'''

        tabela_ficha = '''
            CREATE TABLE IF NOT EXISTS "Ficha" (
                "ID_Ficha" INTEGER PRIMARY KEY,
	            "Nome" TEXT NOT NULL,
	            "Arquetipo"	TEXT,
	            "XP" INTEGER NOT NULL,
	            "Poder"	INTEGER NOT NULL,
	            "Habilidade" INTEGER NOT NULL,
                "Resistencia" INTEGER NOT NULL,
	            "Tipo_Ficha" TEXT CHECK(Tipo_Ficha IN ("Player", "Veiculo")) NOT NULL,
	            "Email_Usuario" TEXT NOT NULL,
                "ID_Mesa" INTEGER,
                "ID_Veiculo" INTEGER,
	            FOREIGN KEY ("Email_Usuario") REFERENCES "Usuario"("Email") ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY ("ID_Mesa") REFERENCES "Mesa"("ID_Mesa") ON DELETE SET NULL ON UPDATE CASCADE,
                FOREIGN KEY ("ID_Veiculo") REFERENCES "Ficha"("ID_Ficha")
            );'''

        tabela_desvantagem = '''
            CREATE TABLE IF NOT EXISTS "Desvantagem" (
	            "nome_Desv"	TEXT NOT NULL,
	            "ID_Ficha"	INTEGER NOT NULL,
	            FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_vantagem = '''
            CREATE TABLE IF NOT EXISTS "Vantagem" (
	            "Nome_Vant"	TEXT NOT NULL,
	            "ID_Ficha"	INTEGER NOT NULL,
	            FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_pericia = '''
            CREATE TABLE IF NOT EXISTS "Pericia" (
                "Nome_Pericia" TEXT PRIMARY KEY,
                "ID_Ficha" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_item  = '''
            CREATE TABLE IF NOT EXISTS "Item" (
                "ID_Item" INTEGER PRIMARY KEY,
                "Nome_Item" TEXT NOT NULL,
                "Raridade" TEXT NOT NULL,
                "Efeito" TEXT NOT NULL,
                "ID_Ficha" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_artefato = '''
            CREATE TABLE IF NOT EXISTS "Artefato"(
                "ID_Item" INTEGER PRIMARY KEY AUTOINCREMENT,
                "XP" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_tecnica = '''
            CREATE TABLE IF NOT EXISTS "Tecnica" (
                "ID_Item" INTEGER PRIMARY KEY AUTOINCREMENT,
                "XP" INTEGER NOT NULL,
                "Custo" INTEGER NOT NULL,
                "Alcance" TEXT NOT NULL,
                "Duracao" TEXT NOT NULL,
                FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item") ON DELETE CASCADE ON UPDATE CASCADE
             );'''

        tabela_qualidade = '''
            CREATE TABLE IF NOT EXISTS "Qualidade"(
                "Nome" TEXT NOT NULL UNIQUE,
                "ID_Artefato" INTEGER,
                FOREIGN KEY ("ID_Artefato") REFERENCES "Artefato"("ID_Item") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        tabela_requisito = '''
            CREATE TABLE IF NOT EXISTS "Requisito"(
                "ID_Requisito" INTEGER,
                "Nome" TEXT NOT NULL UNIQUE,
                FOREIGN KEY ("ID_Requisito") REFERENCES "Tecnica"("ID_Item") ON DELETE CASCADE ON UPDATE CASCADE
            );'''

        self.cursor.execute(tabela_usuario)
        self.cursor.execute(tabela_ficha)
        self.cursor.execute(tabela_mesa)
        self.cursor.execute(tabela_desvantagem)
        self.cursor.execute(tabela_vantagem)
        self.cursor.execute(tabela_pericia)
        self.cursor.execute(tabela_item)
        self.cursor.execute(tabela_artefato)
        self.cursor.execute(tabela_tecnica)
        self.cursor.execute(tabela_qualidade)
        self.cursor.execute(tabela_requisito)

        self.conn.commit()

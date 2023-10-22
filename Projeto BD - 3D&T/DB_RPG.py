import sqlite3 as sql3

class DataBase:
    def __init__(self, db_name = "3D&T.db"):
        self.conn = sql3.connect("Projeto BD - 3D&T\\database\\database.db")
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        tabela_usuario = '''
            CREATE TABLE "Usuario" (
                "Email" TEXT PRIMARY KEY,
                "Nome" TEXT NOT NULL UNIQUE,
                "Senha" TEXT NOT NULL UNIQUE
            );'''

        tabela_mesa = '''
            CREATE TABLE "Mesa"(
                "Nome_Mesa" TEXT NOT NULL,
                "ID_Mesa" INTEGER PRIMARY KEY,
                "Email_Usuario" INTEGER NOT NULL,
                FOREIGN KEY ("Email_Usuario") REFERENCES "Usuario"("Email")

            );'''

        tabela_ficha = '''
            CREATE TABLE "Ficha" (
                "ID_Ficha" INTEGER PRIMARY KEY,
	            "Nome" TEXT NOT NULL,
	            "Arquetipo"	TEXT NOT NULL,
	            "XP" INTEGER DEFAULT 100 NOT NULL,
	            "Poder"	INTEGER NOT NULL,
	            "Habilidade" INTEGER NOT NULL,
                "Resistencia" INTEGER NOT NULL,
	            "Tipo_Ficha" TEXT CHECK(Tipo_Ficha IN ("Player", "Veiculo")) NOT NULL,
	            "Email_Usuario" TEXT NOT NULL,
                "ID_Mesa" INTEGER NOT NULL,
	            FOREIGN KEY ("Email_Usuario") REFERENCES "Usuario"("Email"),
                FOREIGN KEY ("ID_Mesa") REFERENCES "Mesa"("ID_Mesa")
            );'''

        tabela_desvantagem = '''
            CREATE TABLE "Desvantagem" (
	            "nome_Desv"	TEXT NOT NULL,
	            "ID_Ficha"	INTEGER NOT NULL,
	            FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
            );'''

        tabela_vantagem = '''
            CREATE TABLE "Vantagem" (
	            "Nome_Vant"	TEXT NOT NULL,
	            "ID_Ficha"	INTEGER NOT NULL,
	            FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
            );'''

        tabela_pericia = '''
            CREATE TABLE "Pericia" (
                "Nome_Pericia" TEXT PRIMARY KEY,
                "ID_Ficha" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
            );'''

        tabela_item  = '''
            CREATE TABLE "Item" (
                "ID_Item" INTEGER PRIMARY KEY,
                "Nome_Item" TEXT NOT NULL,
                "Raridade" TEXT NOT NULL,
                "Efeito" TEXT NOT NULL,
                "ID_Ficha" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
            );'''

        tabela_artefato = '''
            CREATE TABLE "Artefato"(
                "ID_Item" INTEGER PRIMARY KEY,
                "XP" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item")
            );'''

        tabela_tecnica = '''
            CREATE TABLE "Tecnica" (
                "ID_Item" INTEGER PRIMARY KEY,
                "XP" INTEGER NOT NULL,
                "Custo" INTEGER NOT NULL,
                "Alcance" INTEGER NOT NULL,
                "Duracao" INTEGER NOT NULL,
                FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item")
             );'''

        tabela_qualidade = '''
            CREATE TABLE "Qualidade"(
                "ID_Qualidade" INTEGER PRIMARY KEY,
                "Nome" TEXT NOT NULL UNIQUE,
                "ID_Artefato" INTEGER,
                FOREIGN KEY ("ID_Artefato") REFERENCES "Artefato"("ID_Item")
            );'''

        tabela_requisito = '''
            CREATE TABLE "Requisito"(
                "ID_Requisito" INTEGER PRIMARY KEY,
                "Nome" TEXT NOT NULL UNIQUE,
                FOREIGN KEY ("ID_Requisito") REFERENCES "Tecnica"("ID_Item")
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

    def cadastrar_usuario(self, email, nome, senha):
        query = "INSERT INTO Usuario (Email, Nome, Senha) VALUES (?, ?, ?)"
        values = (email, nome, senha)
        self.cursor.execute(query,values)
        self.conn.commit()

    def cadastrar_ficha(self, ID_Ficha, Nome, Arquetipo, Poder, Habilidade, Resistencia, Tipo_Ficha, Email_Usuario, ID_Mesa):
        query = "INSERT INTO Ficha (ID_Ficha, Nome, Arquetipo, Poder, Habilidade, Resistencia, Tipo_Ficha, Email_Usuario, ID_Mesa) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (ID_Ficha, Nome, Arquetipo, Poder, Habilidade, Resistencia, Tipo_Ficha, Email_Usuario, ID_Mesa)
        self.cursor.execute(query, values)
        self.conn.commit()


    def cadastrar_mesa(self, nome_mesa, id_mesa, email_usuario):
        query = "INSERT INTO Mesa (Nome_Mesa, ID_Mesa, Email_Usuario) VALUES (?, ?, ?)"
        values = (nome_mesa, id_mesa, email_usuario)
        self.cursor.execute(query,values)
        self.conn.commit()

    def cadastrar_vantagem(self, nome, id_ficha):
        query = "INSERT INTO Vantagem (Nome_Vant, ID_Ficha) VALUES (?, ?)"
        values = (nome, id_ficha)
        self.cursor.execute(query, values)
        self.conn.commit()

    def cadastrar_desvantagem(self, nome, id_ficha):
        query = "INSERT INTO Desvantagem (nome_Desv, ID_Ficha) VALUES (?, ?)"
        values = (nome, id_ficha)
        self.cursor.execute(query, values)
        self.conn.commit()

    def cadastrar_pericia(self, nome_pericia, id_ficha):
        query = "INSERT INTO Pericia (Nome_Pericia, ID_Ficha) VALUES (?,?)"
        values = (nome_pericia, id_ficha)
        self.cursor.execute(query, values)
        self.conn.commit()

    def cadastrar_item_artefato(self, ID_Item, Nome_Item, Raridade, XP, Efeito, ID_Ficha, Nome_Qualidade):
        query_a = "INSERT INTO Item(ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha) VALUES (?, ?, ?, ?, ?)"
        query_b = "INSERT INTO Artefato(ID_Item, XP) VALUES (?, ?)"
        query_c = "INSERT INTO Qualidade(Nome, ID_Artefato) VALUES (?, ?)"
        values_a = (ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha)
        values_b = (ID_Item, XP)
        values_c = (Nome_Qualidade, ID_Item)
        self.cursor.execute(query_a, values_a)
        self.cursor.execute(query_b, values_b)
        self.cursor.execute(query_c, values_c)
        self.conn.commit()

    def cadastrar_item_tecnica(self, ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha, XP, Custo, Alcance, Duracao, Nome_Requisito, ):
        query_a = "INSERT INTO Item(ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha) VALUES (?, ?, ?, ?, ?)"
        query_b = "INSERT INTO Tecnica(ID_Item, XP, Custo, Alcance, Duracao) VALUES (?, ?, ?, ?, ?)"
        query_c = "INSERT INTO Requisito(Nome, ID_Requisito) VALUES (?, ?)"
        values_a = (ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha)
        values_b = (ID_Item, XP, Custo, Alcance, Duracao)
        values_c = (Nome_Requisito, ID_Item)
        self.cursor.execute(query_a, values_a)
        self.cursor.execute(query_b, values_b)
        self.cursor.execute(query_c, values_c)
        self.conn.commit()

Db = DataBase()
Db.criar_tabelas()
Db.cadastrar_mesa("Ragnarok", 122, "mtafg567@gmail.com")
Db.cadastrar_usuario("mtafg567@gmail.com", "Vinicoios", "coio290903.")
Db.cadastrar_ficha(1, "Cecilus Sigurd", "Humano", 11, 15, 19, "Player", "mtafg567@gmail.com",122)
Db.cadastrar_vantagem("Ágil", 1)
Db.cadastrar_vantagem("Anulação", 1)
Db.cadastrar_desvantagem("Antipático",1)
Db.cadastrar_desvantagem("Frágil",1)
Db.cadastrar_item_artefato(233, "Wasameru", "Mítico", 190, "Arma", 1, "Sagrado")
Db.cadastrar_item_tecnica(444, "Expurgar", "Lendária", "Truque Lendário", 1, 800, 9, 300, 2, "Magia, Mística")
Db.cadastrar_pericia("Arte", 1)


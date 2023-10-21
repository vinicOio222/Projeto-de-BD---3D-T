CREATE TABLE "Usuario" (
   "Email" TEXT PRIMARY KEY,
   "Nome" TEXT NOT NULL UNIQUE,
   "Senha" TEXT NOT NULL UNIQUE
 );
 
CREATE TABLE "Ficha" (
    "ID_Ficha"INTEGER PRIMARY KEY,
	"Nome"	TEXT NOT NULL UNIQUE,
	"Mesa"	TEXT NOT NULL,
	"Arquétipo"	TEXT NOT NULL,
	"XP"	INTEGER NOT NULL,
	"Poder"	TEXT NOT NULL,
	"Habilidade"	TEXT NOT NULL,
	"Tipo_Ficha"	TEXT NOT NULL,
	"Resistencia"	TEXT NOT NULL,
	"ID_Usuario"	INTEGER not NULL,
	FOREIGN KEY("ID_Usuario") REFERENCES "Usuario"("ID")
);

CREATE TABLE "Desvantagem" (
	"nome_Desv"	TEXT PRIMARY KEY,
	"ID_Ficha"	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
);

CREATE TABLE "Vantagem" (
	"Nome_Vant"	TEXT PRIMARY KEY,
	"ID_Ficha"	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
);

CREATE TABLE "Pericia" (
  "Nome_Pericia" TEXT PRIMARY KEY,
  "ID_Ficha" INTEGER NOT NULL UNIQUE,
  FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
 );
 
 CREATE TABLE "Item" (
   "ID_Item" INTEGER PRIMARY KEY,
   "Nome_Item" TEXT NOT NULL,
   "Raridade" TEXT NOT NULL,
   "Efeito" TEXT NOT NULL,
   "XP" INTEGER NOT NULL,
   "ID_Ficha" INTEGER NOT NULL UNIQUE,
   FOREIGN KEY ("ID_Ficha") REFERENCES "Ficha"("ID_Ficha")
 );
 
 CREATE TABLE "Artefato"(
   "ID_Item" INTEGER PRIMARY KEY,
   "Nome" TEXT NOT NULL,
   FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item")
 );
 
 CREATE TABLE "Tecnica" (
   "ID_Item" INTEGER PRIMARY KEY,
   "Nome" TEXT NOT NULL,
   FOREIGN KEY ("ID_Item") REFERENCES "Item"("ID_Item")
 );
 
 CREATE TABLE "Qualidade"(
   "ID_Qualidade" INTEGER PRIMARY KEY,
   "Nome" TEXT NOT NULL UNIQUE, 
   "ID_Artefato" INTEGER,
   FOREIGN KEY ("ID_Artefato") REFERENCES "Artefato"("ID_Item")
 );
 
 CREATE TABLE "Requisito"(
   "ID_Requisito" INTEGER PRIMARY KEY,
   "Nome" TEXT NOT NULL UNIQUE, 
   "ID_Tecnica" INTEGER,
   FOREIGN KEY ("ID_Requisito") REFERENCES "Tecnica"("ID_Item")
 );
 
 
 
 
 
 
# -*- encoding: utf-8 -*-

import codecs
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

metadata = 'type|lang|creationdate|modifdate|dataseed|scriptname'
class BDdatos():

    def conectar(self):
        """
            conectarme a la bd
        """
        db = None
        try:
            db=mysql.connector.connect(host="localhost",user="root",password="andres1601",database="sbc_proyecto",charset='utf8mb4',use_unicode=True)
            #cursor=db.cursor()
        except mysql.connector.Error as error:
            print("error de conexión")
        return db
    
    def closeDB(self, db):
        """
            closeDB la base de datos
        """
        db.close()
    
    def saveDB(self, db):
        """
            closeDB la base de datos
        """
        db.commit()


    def DBCSubconceptsVR(db, self, date, s, c1, c2, c3, l, table):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + table + """ values (%s, %s, %s, %s, %s, %s)""", (date, s, c1, c2, c3, l))
        db.saveDB(con)
        db.closeDB(con)


    def DBCGetUniqueConcepts(db, self, stable, otable, ftable):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""CREATE TABLE """ + otable +
            """ SELECT DISTINCT `level`, c1 FROM """ + stable + """ WHERE c1 is not NULL"""
            """ UNION SELECT DISTINCT `level`, c2 FROM """ + stable + """ WHERE c2 is not NULL"""
            """ UNION SELECT DISTINCT `level`, c3 FROM """ + stable + " WHERE c3 is not NULL;")

        cursor.execute(u"""CREATE TABLE """ + ftable + """ (id INT AUTO_INCREMENT PRIMARY KEY)"""
            """ SELECT DISTINCT c1 AS c FROM """ + otable + """ WHERE length(c1) > 0;""")

        db.saveDB(con)
        db.closeDB(con)

    def DBSubconcepts_WikiPages(db, self, date, c, r, p, d, l, table):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        
        # Insert data
        cursor.execute(u"""INSERT INTO """ + table + """ values (%s, %s, %s, %s, %s, %s)""", (date, c, r, p, d, l))
        db.saveDB(con)
        db.closeDB(con)


    def WikiPagesRedirects(db, self, date, idp, dbpediaUrl, returnedUrl, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s)""", (date, idp, dbpediaUrl, returnedUrl))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageMetadata(db, self, date, page, title, pageid, revid, lastUpdate, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s)""", (date, page, title, pageid, revid, lastUpdate))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageLanglinks(db, self, date, page, lang, url, langname, autonym, pageLang, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s, %s)""", (date, page, lang, url, langname, autonym, pageLang))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageCategories(db, self, date, page, category, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s)""", (date, page, category))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageLinks(db, self, date, page, ns, link, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s)""", (date, page, ns, link))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageTemplates(db, self, date, page, ns, link, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s)""", (date, page, ns, link))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageExternalLinks(db, self, date, page, link, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s)""", (date, page, link))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageWikiProjects(db, self, date, page, prefix, url, nameproj,tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s)""", (date, page, prefix, url, nameproj))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageTOC(db, self, date, page, toclevel, levels, line, number, indexs, fromtitle, anchor, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (date, page, toclevel, levels, line, number, indexs, fromtitle, anchor))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageError(db, self, date, page, error, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s)""", (date, page, error))
        db.saveDB(con)
        db.closeDB(con)


    def WikiPageMetadataLib(db, self, date, page, summary, revisionID, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s)""", (date, page, summary, revisionID))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageSections(db, self, date, page, section, sectionID, textS, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s)""", (date, page, section, sectionID, textS))
        db.saveDB(con)
        db.closeDB(con)

    def WikiPageSectionLinks(db, self, date, page, section, sectionID, textLink, link, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s)""", (date, page, section, sectionID, textLink, link))
        db.saveDB(con)
        db.closeDB(con)

    def WikiAnnotationMetadata(db, self, date, page, url, title, pageid, revisionID, lastUpdate, summary, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s, %s, %s)""", (date, page, url, title, pageid, revisionID, lastUpdate, summary))
        db.saveDB(con)
        db.closeDB(con)

    def WikidataRV3(db, self, date, idn, page, p, o, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s)""", (date, idn, page, p, o))
        db.saveDB(con)
        db.closeDB(con)


    def WikiPageSectionRV(db, self, date, page, section, idSection, idWikidata, pstart, pend, text, tabla):
        """
            Insertar en la base de datos
        """
        con = db.conectar()  
        #if db2 is not None: 
        cursor=con.cursor()
        cursor.execute(u"""INSERT INTO """ + tabla + """ values (%s, %s, %s, %s, %s, %s, %s, %s)""", (date, page, section, idSection, idWikidata, pstart, pend, text))
        db.saveDB(con)
        db.closeDB(con)


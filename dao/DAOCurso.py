import pymysql

class DAOCurso:
    def connect(self):
        return pymysql.connect(host='localhost', password='',user='root',db='db_poo')

    def read(self, id):
        con = DAOCurso.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM curso order by nombre_curso")

            else:
                cursor.execute("SELECT * FROM curso where id = %s order by nombre_curso", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


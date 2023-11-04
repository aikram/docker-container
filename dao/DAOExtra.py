import pymysql

class DAOExtra:
    def connect(self):
        return pymysql.connect(host='localhost', password='',user='root',db='db_poo')

    def read(self, id):
        con = DAOExtra.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM extra order by id")

            else:
                cursor.execute("SELECT * FROM extra where codigo = %s order by id", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    
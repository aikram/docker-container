import pymysql

class DAOEmpleado:
    def connect(self):
        return pymysql.connect(host='db', password='',user='root',db='db_poo')

    def read(self, id):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM empleado order by nombre")

            else:
                cursor.execute("SELECT * FROM empleado where codigo = %s order by nombre", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = self.connect()
        cursor = con.cursor()

        try:
            insert_query = "INSERT INTO empleado (nombre, apellido, area, sueldo, profesion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (data['nombre'], data['apellido'], data['area'], data['sueldo'], data['profesion']))
            con.commit()
            return True
        except pymysql.Error as e:
            print("Error al insertar empleado:", e)
            con.rollback()
            return False
        finally:
            con.close()
    
    def update(self, id, data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE empleado SET nombre = %s, apellido = %s, area = %s, sueldo = %s, profesion = %s WHERE codigo = %s", (data['nombre'],data['apellido'],data['area'],data['sueldo'],data['profesion'],id,))
            con.commit()
            return True
        except pymysql.Error as e:
            print("Error al actualizar empleado:", e)
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleado where codigo = %s", (id,))
            con.commit()
            return True
        except pymysql.Error as e:
            print("Error al borrar empleado:", e)
            con.rollback()
            return False
        finally:
            con.close()


import sqlite3


class Data:
    def __init__(self):
        self._cConnect = sqlite3.connect("ESTUDIO")
        self._cCursorSql = self._cConnect.cursor()
        self._sentencia=""
    #end _init

    def seek(self):
        #table 1
        self._sentencia = '''CREATE TABLE IF NOT EXISTS ESTUDIANTE (ID_ESTUDIANTE INTEGER PRIMARY KEY AUTOINCREMENT, MATRICULA INT NOT NULL, 
        NOMBRE VARCHAR(30), SEXO NCHAR(1), APELLIDO VARCHAR(30), LUGAR_NACIMEINTO VARCHAR(30), CARRERA VARCHAR(50), CEDULA VARCHAR(11), FOTO VARCHAR(200))'''
        self._cCursorSql.execute(self._sentencia)
        #table 2
        self._sentencia = "CREATE TABLE IF NOT EXISTS MATERIA (CODIGO VARCHAR(6), NOMBRE_MATERIA VARCHAR(15))"
        self._cCursorSql.execute(self._sentencia)
        #table 3
        self._sentencia = '''CREATE TABLE IF NOT EXISTS CALIFICACIONES (ID_CALIFICACION INTEGER PRIMARY KEY AUTOINCREMENT, ID_ESTUDIANTE INTEGER, 
        ID_MATERIA VARCHAR(6), PRACTICA1 INT, PRACTICA2 INT, FORO1 INT, FORO2 INT, PRIMER_PARCIAL INT, SEGUNDO_PARCIAL INT, EXAMEN_FINAL INT,
        FOREIGN KEY(ID_ESTUDIANTE) REFERENCES ESTUDIANTE(ID_ESTUDIANTE),
        FOREIGN KEY(ID_MATERIA) REFERENCES MATERIA(CODIGO))'''
        self._cCursorSql.execute(self._sentencia)
    #end method

    def insert(self, varios, tabla, n):
        if self.exist(varios[0][0], tabla):
            return self.update(varios, tabla) #ready
        else:
            try:
                self._sentencia=f"INSERT INTO {tabla} VALUES ({self.limit(n)})"
                self._cCursorSql.executemany(self._sentencia, varios)
                self._cConnect.commit()
                return 'insertado'
            except:
                return 'Error'
        #end condition
    #end methhod

    def update(self, varios, tabla):
        if tabla =="ESTUDIANTE":
            self._sentencia=f'''UPDATE {tabla}
                    SET MATRICULA = {varios[0][0]} ,
                        NOMBRE = '{varios[0][2]}' ,
                        SEXO = '{varios[0][3]}'
                    WHERE ID_ESTUDIANTE = {varios[0][0]}'''
        elif tabla=="MATERIA":
            self._sentencia=f'''UPDATE {tabla}
                    SET  NOMBRE_MATERIA = '{varios[0][1]}'
                    WHERE CODIGO = "{varios[0][0]}"'''
        elif tabla=="CALIFICACIONES":
            self._sentencia=f'''UPDATE {tabla}
                    SET ID_ESTUDIANTE ={varios[0][1]},
                        ID_MATERIA = '{varios[0][2]}' ,
                        PRACTICA1 = {varios[0][3]} ,
                        PRACTICA2 = {varios[0][4]} ,
                        FORO1 = {varios[0][5]} ,
                        FORO2 = {varios[0][6]} ,
                        PRIMER_PARCIAL = {varios[0][7]} ,
                        SEGUNDO_PARCIAL = {varios[0][8]} ,
                        EXAMEN_FINAL = {varios[0][9]}
                    WHERE ID_CALIFICACION = {varios[0][0]}'''
        #end condition
        try:
            self._cCursorSql.execute(self._sentencia)
            self._cConnect.commit()
            return "editado"
        except:
            return "error"
        #end try
    #end method

    def calificacionByEstudiante(self, idestudiante):
        self._sentencia = f"select * from 'CALIFICACIONES' WHERE ID_ESTUDIANTE ={idestudiante}"
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def consultar(self, tabla):
        self._sentencia = f"select * from '{tabla}'"
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def consultarById(self, tabla, field, id):
        self._sentencia = f"select * from '{tabla}' where {field}={id}" if(tabla!='MATERIA') else f"select * FROM {tabla} WHERE {field}='{id}'"
        return self._cCursorSql.execute(self._sentencia).fetchone()
    #end method

    def delete(self,_id, tabla, field):
        if _id!="":
            try:
                self._sentencia=f"DELETE FROM {tabla} WHERE {field}={_id}" if(tabla!='MATERIA') else f"DELETE FROM {tabla} WHERE {field}='{_id}'"
                print(self._sentencia)
                self._cCursorSql.execute(self._sentencia)
                self._cConnect.commit()
                return 'eliminado'
            except:
                return 'Error'
        else:
            return 'No valido'
    #end method

    def limit(self, n):
        texto=''
        for i in range(0,n):
            texto=texto=texto+'?,' if(i<(n-1)) else texto+'?'
        return texto
    #end method

    def infotabla(self,tabla):
        self._sentencia = """PRAGMA table_info({});""".format(tabla)
        return self._cCursorSql.execute(self._sentencia)
    #end method

    def exist(self, value, tabla):
        if tabla =="ESTUDIANTE":
            self._sentencia= f"select * from '{tabla}' where ID_ESTUDIANTE={value}"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="MATERIA":
            self._sentencia= f"select * from '{tabla}' where CODIGO='{value}'"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="CALIFICACIONES":
            self._sentencia= f"select * from '{tabla}' where ID_CALIFICACION={value}"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
#end method
#end class
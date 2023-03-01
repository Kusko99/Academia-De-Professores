from mysql.connector import connection
import Formatting

host ='localhost'
user ='root'
password = 'portuguesa1'
database = 'DB_AcademiaDosProfessores'

def conexaoDB_TB_Curso(nome_curso,data_curso,horas,tipo,aplicador):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    sql = "INSERT INTO TB_Curso (Data_Curso,Horas,NomeCurso,Tipo,Aplicador) values (%s, %s, %s,%s,%s)"
    values = (data_curso,horas,nome_curso,tipo,aplicador)
    cursor.execute(sql,values)

    cursor.close()
    db_connection.commit()
    db_connection.close()

def conexaoDB_TB_Professor(Nome,Email):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Email FROM TB_Professor WHERE Nome = (%s)"
    values = (Nome,)
    cursor.execute(query,values)
    resultados = cursor.fetchall()
    if not resultados:
        try:
            sql = "INSERT INTO TB_Professor(Nome, Email) VALUES (%s, %s)"
            values = (Nome,Email)
            cursor.execute(sql,values)
        except:
            pass
    else:
        pass
    
    cursor.close()
    db_connection.commit()
    db_connection.close()


def conexaoDB_TB_Presenca(Nome,Email,NomeCurso):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    

    ID_Curso = Get_Curso_ID(NomeCurso)
    
    conexaoDB_TB_Professor(Nome,Email)
    
    sql = "INSERT INTO TB_Presenca (Email,ID_Curso) VALUES (%s,%s)"
    values = (Email,ID_Curso) 
    cursor.execute(sql,values)

    
    cursor.close()
    db_connection.commit()
    db_connection.close()

def Get_Curso_ID(NomeCurso):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT ID FROM TB_Curso WHERE NomeCurso = (%s)"
    values = (NomeCurso,)
    cursor.execute(query,values)
    resultados = cursor.fetchall()
    
    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultados[0][0]

def Get_Curso_Date(past_date,future_date):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT NomeCurso,Data_Curso from TB_Curso WHERE Data_Curso BETWEEN (%s) AND (%s) ORDER BY Data_Curso"
    values = (past_date,future_date)
    cursor.execute(query,values)
    resultados = cursor.fetchall()

    # print(past_date)
    # print(future_date)
    # print(resultados)
    
    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultados



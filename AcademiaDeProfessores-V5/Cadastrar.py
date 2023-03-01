import csv
import ConexaoDataBase
import Formatting


def CadastraCursoCSV(filename):
    arquivo = open(filename, encoding='utf-8')
    cursos = csv.DictReader(arquivo,delimiter=";")
    for curso in cursos:
        print(curso)
        data = Formatting.DateToSQLDate(curso['Data'])
        nome_curso = curso['\ufeffNome']
        horas = curso['Horas']
        tipo = curso['Tipo']
        aplicador = curso['Aplicador']
        ConexaoDataBase.conexaoDB_TB_Curso(nome_curso,data,horas,tipo,aplicador)

def CadastrarPresencaCSV(filename):
    arquivo = open(filename,encoding='utf-8')
    presentes = csv.DictReader(arquivo,delimiter=";")
    for presente in presentes:
        Nome_Professor = presente['\ufeffNome']
        email = presente['Email']
        NomeCurso = presente['Atividade']
        ConexaoDataBase.conexaoDB_TB_Presenca(Nome_Professor,email,NomeCurso)


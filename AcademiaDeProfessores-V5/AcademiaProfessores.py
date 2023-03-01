import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import urllib.request
import pandas as pd
import Cadastrar
import ConexaoDataBase
import Formatting

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


@app.route("/")
def home():
  return render_template("Home.html")

@app.route("/home")
def home2():
  #CHANGE THIS LATER
  return render_template("home.html")

@app.route("/registros")
def registros():
  return render_template("Registros.html")

@app.route("/criarRegistro")
def criarRegistro():
  return render_template("CriarRegistro.html")

@app.route("/cadastrarPresencaCSV", methods=['GET','POST'])
def cadastrarPresenaCSV():
  if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        new_filename = filename.split('.')[0] + ".csv"
        file.save(os.path.join('data',new_filename))
        Cadastrar.CadastrarPresencaCSV(new_filename)
        delete_path = "data/" + new_filename
        os.remove(delete_path)
      return 'uploaded'
  return render_template("CadastrarPresencaCSV.html")

@app.route("/cadastrarCursoCSV", methods=['GET','POST'])
def cadastrarCursoCSV():
    if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        new_filename = filename.split('.')[0] + ".csv"
        file.save(os.path.join('data',new_filename))
        Cadastrar.CadastraCursoCSV(new_filename)
        delete_path = "data/" + new_filename
        os.remove(delete_path)
      return 'uploaded'
    
    return render_template("CadastrarCursoCSV.html")

@app.route("/relatorios")
def relatorios():
  return render_template("Relatorios.html")

@app.route("/relatorioCurso",methods = ['GET','POST'])
def relatorioCurso():
  if request.method == 'POST':
    past_date = request.form['date-past']
    future_date = request.form['date-future']
    resultados = ConexaoDataBase.Get_Curso_Date(past_date,future_date)
    past_date = Formatting.DateSQLToDate_STR(past_date)
    future_date = Formatting.DateSQLToDate_STR(future_date)
    columns = ['Nome do Curso: ','Data: ','Dados do Curso: ']
    rows = []
    for resultado in resultados:
      nome_curso = resultado[0]
      data_curso = Formatting.DateSQLToDate(resultado[1])
      row = [nome_curso,data_curso,"Ver mais"]
      rows.append(row)
    return render_template("InfoCursosPeriodo.html",columns=columns,rows=rows,past_date=past_date,future_date=future_date)
  return render_template("RelatorioCurso.html")

@app.route("/download", methods=['POST',])
def download():
  if request.method == 'POST':
    pagina = urllib.request.urlopen("http://127.0.0.1:5000/relatorioCurso?")
    html_da_pagina = pagina.read()
    print(html_da_pagina)
    return 'Success!'

@app.route("/relatorioProfessor",methods = ['GET','POST'])
def relatorioProfessor():
  if request.method == 'POST':
    past_date = request.form['date-past']
    future_date = request.form['date-future']

    return 'Success!'
  return render_template("RelatorioProfessor.html")

@app.route("/relatorioPresenca", methods = ['GET','POST'])
def relatorioPresenca():
  if request.method == 'POST':
    past_date = request.form['date-past']
    future_date = request.form['date-future']
    
    return 'Success!'
  return render_template("RelatorioPresenca.html")

@app.route("/certificados")
def certificados():
    # return render_template("PLACEHOLDER")
    return "YET TO BE BUILD"

app.run(debug=True)
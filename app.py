from flask import Flask, render_template
from datetime import date
import calendar

app = Flask(__name__)

@app.template_filter('month_name')
def month_name_filter(mes):
    nombres = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return nombres[mes]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/portal')
def portal():
    # Obtener el mes y año actual
    hoy = date.today()
    año = hoy.year
    mes = hoy.month
    calendario_mes = calendar.monthcalendar(año, mes)
    #data notas por semestre
    data = {
        "Séptimo Semestre": {
            "descripcion": "En séptimo semestre de Ingeniería de Software se ven...",
            "fecha": "20 Mar 2025",
            "materias": [
                {"nombre": "Bases de Datos II", "nota": 4.5},
                {"nombre": "Gestión de Proyectos", "nota": 4.3},
                {"nombre": "Sistemas de Información", "nota": 4.8},
                {"nombre": "Programación IV", "nota": 4.6},
                {"nombre": "Redes II", "nota": 4.7},
                {"nombre": "Ética Profesional II", "nota": 4.5}
            ]
        },
        "Sexto Semestre": {
            "descripcion": "En sexto semestre se ven fundamentos de redes...",
            "fecha": "20 Dic 2024",
            "materias": [
                {"nombre": "Redes I", "nota": 4.0},
                {"nombre": "Sistemas Operativos", "nota": 3.9},
                {"nombre": "Ingeniería de Software", "nota": 4.1},
                {"nombre": "Programación III", "nota": 4.4},
                {"nombre": "Matemáticas II", "nota": 4.2},  
                {"nombre": "Ética Profesional", "nota": 4.0}
            ]
        },

        "Quinto Semestre": {
            "descripcion": "En quinto semestre se ven fundamentos de bases de datos...",
            "fecha": "20 Sep 2024",
            "materias": [
                {"nombre": "Bases de Datos I", "nota": 4.2},
                {"nombre": "Programación II", "nota": 4.1},
                {"nombre": "Matemáticas III", "nota": 4.3},
                {"nombre": "Física II", "nota": 4.0},
                {"nombre": "Ética Profesional I", "nota": 4.5}
            ]
        },
        
        "Cuarto Semestre": {
            "descripcion": "En cuarto semestre se ven fundamentos de programación...",
            "fecha": "20 Jun 2024",
            "materias": [
                {"nombre": "Programación I", "nota": 4.0},
                {"nombre": "Matemáticas Discretas", "nota": 3.8},
                {"nombre": "Física I", "nota": 4.1},
                {"nombre": "Química", "nota": 4.2},
                {"nombre": "Ética Profesional", "nota": 4.0},
                {"nombre": "Inglés I", "nota": 4.3}
            ]
        },
        
        "Tercer Semestre": {
            "descripcion": "En tercer semestre se ven fundamentos de matemáticas...",
            "fecha": "20 Mar 2024",
            "materias": [
                {"nombre": "Matemáticas I", "nota": 4.5},
                {"nombre": "Física I", "nota": 4.3},
                {"nombre": "Química", "nota": 4.2},
                {"nombre": "Inglés I", "nota": 4.1},
                {"nombre": "Ética Profesional", "nota": 4.0},
                {"nombre": "Fundamentos de Programación", "nota": 4.4}
            ]
        },
        }

    return render_template("portal.html",
                           calendario_mes=calendario_mes,
                           año=año,
                           mes=mes,
                           hoy=hoy,
                           semestres=data)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/ingresar')
def ingresar():
    return render_template("login_ll.html")

if __name__ == "__main__":
    app.run(debug=True)


import tarjetas
import time
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

i = []
j = []

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home')
def principal():
    return render_template("home.html")

@app.route('/se', methods=["POST", "GET"])
def se():
    if request.method == "POST":
        res = request.form["res"] 
        j.append(tarjetas.tarjetas_español())
        if len(j) <= 1:
            return redirect(url_for("respuesta", espanol=j[0]))
        elif len(j) >= 2:
            comp = tarjetas.spanish_to_english(res, j[-2]) 
            return redirect(url_for("respuesta", espanol=j[-2], comprobacion=comp))
    else:
        if (len(j) == 0):
            j.append(tarjetas.tarjetas_español())
        return render_template("se.html", español=j[-1])

@app.route('/respuesta/<espanol>/<comprobacion>')
def respuesta(espanol, comprobacion):
    return render_template("respuesta.html", español=espanol, traduction=comprobacion)

@app.route('/es', methods=["POST", "GET"])
def es():
    if request.method == "POST":
        res = request.form["res"] 
        i.append(tarjetas.tarjetas_ingles())
        if len(i) <= 1:
            return redirect(url_for("response", ingles=i[0]))
        elif len(i) >= 2:
            ans = tarjetas.english_to_spanish(res, i[-2]) 
            return redirect(url_for("response", ingles=i[-2], answer=ans))
    else:
        if (len(i) == 0):
            i.append(tarjetas.tarjetas_ingles())
        return render_template("es.html", ingles=i[-1])

@app.route('/response/<ingles>/<answer>')
def response(ingles, answer):
    return render_template("response.html", ingles=ingles, traduccion=answer)


if __name__ == "__main__":
    app.run(debug=True)
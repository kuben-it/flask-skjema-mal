from flask import Flask, render_template, request

app = Flask(__name__)

# Svar lagres her mens programmet kjører (tømmes ved omstart)
svar_liste = []


@app.route("/skjema", methods=["GET", "POST"])
def skjema():
    if request.method == "POST":
        svar = {
            "question1": request.form.get("question1"),
            "question2": request.form.get("question2"),
            "question3": request.form.get("question3"),
        }
        svar_liste.append(svar)
        return render_template("resultat.html", svar_liste=svar_liste)

    return render_template("skjema.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

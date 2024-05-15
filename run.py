from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        nx = float(request.form.get('nx'))
        ny = float(request.form.get('ny'))
        na = float(request.form.get('na'))
        nb = float(request.form.get('nb'))

        resultado_x = round(nx / na)
        resultado_y = ny / nb
        
        resultado_total  = resultado_x * resultado_y
        resultado_total = int(resultado_total)

        return render_template('resultados.html', resultado_total=resultado_total)
    except ValueError:
        return "Error: Ingresa valores numéricos válidos en los campos."


if __name__ == '__main__':
    app.run(debug=True)

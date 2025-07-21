from flask import Flask, render_template, request
from elc import (
    calculate_surface_area_cabin,
    calculate_volume_of_cabin,
    calculate_weight_of_cabin,
    calculate_counterweight
)

app = Flask(__name__)

@app.route("/")
def pre_index():
    return render_template("pre index.html")

@app.route("/calculate1", methods=["GET", "POST"])
def pre1_index():
    return render_template("pre1 index.html")

@app.route("/calculate2", methods=["GET", "POST"])
def pre2_index():
    return render_template("pre2 index.html")

@app.route("/calculate4", methods=["GET", "POST"])
def pre4_index():
    return render_template("pre4 index.html")

@app.route("/calculate3", methods=["GET", "POST"])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get input values from form
            L = float(request.form['L'])
            B = float(request.form['B'])
            H = float(request.form['H'])
            payload = float(request.form['payload'])

            # Perform calculations
            area = calculate_surface_area_cabin(L, B, H)
            volume = calculate_volume_of_cabin(area)
            weight = calculate_weight_of_cabin(volume)
            counterweight = calculate_counterweight(weight, payload)

            result = {
                'area': area,
                'volume': volume,
                'weight': weight,
                'counterweight': counterweight
            }

        except Exception as e:
            result = {'error': f"Error: {str(e)}"}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

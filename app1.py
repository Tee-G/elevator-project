from flask import Flask, render_template, request
from elc import (
    calculate_surface_area_cabin,
    calculate_volume_of_cabin,
    calculate_weight_of_cabin,
    calculate_counterweight
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
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

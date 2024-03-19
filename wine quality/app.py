from flask import Flask, render_template, request
app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        ph = float(request.form['ph'])  # Extracting pH value from the form
        alcohol = float(request.form['alcohol'])  # Extracting alcohol value from the form
        
        # Here you can implement your prediction logic using ph and alcohol values
        
        # For now, let's just return a dummy response
        return f"Predicted quality for pH={ph}, Alcohol={alcohol}: High"

if __name__ == '__main__':
    app.run(debug=True)

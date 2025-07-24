from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model/spam_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    prediction = model.predict([message])[0]
    result = "Spam ❌" if prediction == 1 else "Not Spam ✅"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)

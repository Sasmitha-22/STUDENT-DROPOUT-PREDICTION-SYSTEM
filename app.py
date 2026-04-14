from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model files
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        sem1 = float(request.form['sem1'])
        sem2 = float(request.form['sem2'])
        fees = int(request.form['fees'])
        prev = float(request.form['prev'])

        data = [[age, gender, sem1, sem2, fees, prev]]
        df = pd.DataFrame(data, columns=features)

        scaled = scaler.transform(df)
        prediction = model.predict(scaled)[0]

        label_map = {
            0: "Dropout",
            1: "Enrolled",
            2: "Graduate"
        }

        result = label_map[prediction]

        if prediction == 0:
            rec = "⚠️ High risk of dropout!"
        elif prediction == 1:
            rec = "📊 Monitor performance"
        else:
            rec = "🎓 Likely to graduate"

        return render_template('index.html', prediction=result, recommendation=rec)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
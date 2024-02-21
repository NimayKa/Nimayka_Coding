from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

import pickle

app = Flask(__name__)

# Load trained machine learning model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data['features'])
    return {'prediction': prediction.tolist()}

if __name__ == '__main__':
    app.run(debug=True)


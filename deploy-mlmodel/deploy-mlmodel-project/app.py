from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    # bulan = request.form["bulan"]
    # tahun = int(request.form["tahun"])
    # kualitas = (request.form["kualitas"])
    # prediction = model.predict([[bulan, tahun, kualitas]])
    # output = round(prediction[0],2)
        prediction = 0 # Nilai prediksi diisi di sini
        return render_template('index.html', prediction=prediction)
if __name__ == "__main__":
    app.run()
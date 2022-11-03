from flask import Flask, redirect, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        bulan = request.form["bulan"]
        tahun = int(request.form["tahun"])
        kualitas = (request.form["kualitas"])
        # prediction = model.predict([[bulan, tahun, kualitas]])

        if (kualitas == "premium"):
            kualitas = 0
        elif (kualitas == "medium"):
            kualitas = 1
        elif (kualitas == "luar_kualitas"):
            kualitas = 2

        pickled_model = pickle.load(open('model/model.pkl', 'rb'))
        result = pickled_model.predict([[tahun, bulan, kualitas]])

        output = round(result[0],2)
        prediction = output # Nilai prediksi diisi di sini
        return render_template('index.html', prediction=("Prediksi harga beras: Rp " + str(prediction)))
if __name__ == "__main__":
    app.run()
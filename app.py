from flask import Flask, redirect, request, render_template
import pickle
import numpy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        bulan = int(request.form["bulan"])
        tahun = int(request.form["tahun"])
        kualitas = int(request.form["kualitas"])

        kualitas_value = {
            0: "Premium",
            1: "Medium",
            2: "Luar Kualitas",
        }

        bulan_value = {
            0: "Januari",
            1: "Februari",
            2: "Maret",
            3: "April",
            4: "Mei",
            5: "Juni",
            6: "Juli",
            7: "Agustus",
            8: "September",
            9: "Oktober",
            10: "November",
            11: "Desember"
        }

        pickled_model = pickle.load(open('model/model.pkl', 'rb'))
        result = pickled_model.predict([[tahun, bulan, kualitas]])

        output = numpy.round(result[0],2)
        prediction = output[0] # Nilai prediksi diisi di sini
        return render_template('index.html', first_line=("Prediksi harga beras " + kualitas_value[kualitas]), second_line=(" Bulan " + bulan_value[bulan] + " " + str(tahun) + " Rp " + str(prediction)))
if __name__ == "__main__":
    app.run()
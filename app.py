from flask import Flask, request, render_template, send_from_directory
import main

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    college_code = request.form['code']
    starting_roll_no = request.form['start']
    ending_roll_no = request.form['end']
    output_file_name = request.form['output']
    main.Du_Crawler(college_code, starting_roll_no, ending_roll_no, output_file_name)
    return send_from_directory('static/Scrapped csv files/', output_file_name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify

from Functions.getting_random_words import get_word
from Functions.loading_data_per_page import read_load_json_file
from Functions.text_messages import getting_started, select_mode

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word', methods=['POST'])
def get_new_word():
    request_data = request.json

    page = request_data['page']
    language = request_data['language']

    if language == 'eng_to_arm':
        mode = 1
    else:
        mode = 0
    data = read_load_json_file('Data/data.json', page)
    words = get_word(data, mode)

    return jsonify({"word": words[0], "translation": words[1]})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')


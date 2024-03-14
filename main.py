import keyboard
from Functions.getting_random_words import  get_word
from Functions.loading_data_per_page import read_load_json_file
from Functions.text_messages import getting_started

# keyboard.wait('enter')
# print("Word: XXX", end="", flush=True)
# keyboard.wait('enter')
# print("Translation ", end="", flush=True)

if __name__ == "__main__":
    pages = getting_started()
    data = read_load_json_file(r"C:\Users\Mikayel\PycharmProjects\EnglishApp\Data\data.json",pages)

    for i in range(10):
        print(get_word(data))
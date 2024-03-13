import json


def read_load_json_file(filename, page_number):
    '''
    Reads file and returns data by page (data is sorted by page)
    :param filename: Name of file where is data
    :param page: number of wanted page
    :return: return json format data
    '''
    with open(filename, 'r') as file:
        data = json.load(file)
    page = f'page{page_number}'

    return data[page]

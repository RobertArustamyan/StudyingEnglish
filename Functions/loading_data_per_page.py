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
    return_data = []
    if type(page_number) == list:
        for p in page_number:
            page = f'page{p}'
            return_data.extend(data[page])
        return return_data
    else:
        return data[f'page{page_number}']
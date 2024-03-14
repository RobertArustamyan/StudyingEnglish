import json


def read_load_json_file(filename, page_numbers):
    '''
    Reads file and returns data by page (data is sorted by page)
    :param filename: Name of file where is data
    :param page_numbers: List of page numbers
    :return: Return JSON format data
    '''
    with open(filename, 'r',encoding='utf-8') as file:
        data = json.load(file)

    return_data = {}

    if isinstance(page_numbers, list):
        for page_number in page_numbers:
            page_key = f'page{page_number}'
            if page_key in data:
                return_data.update(data[page_key])
    else:
        page_key = f'page{page_numbers}'
        if page_key in data:
            return_data.update(data[page_key])

    return return_data


if __name__ == "__main__":
   print(read_load_json_file(r'C:\Users\Mikayel\PycharmProjects\EnglishApp\Data\data.json', [1,2,3]))

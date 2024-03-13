def getting_started():
    print("Hello! This is my console application for Armenians to learn English words.")
    print("You can choose only one page or can combine and mix them and get mixed words.")
    page_mode = int(input("0 if you want to practice one page, 1 if many: "))
    while page_mode not in [0,1]:
        page_mode = int(input("0 if you want to practice one page, 1 if many: "))

    if page_mode:
        pages_with_commas = input("Enter page numbers, seperated by commas: ")
        pages = [int(val) for val in pages_with_commas.split(',')]
    else:
        pages = int(input("Enter page number: "))

    return pages

if __name__=='__main__':
    print(getting_started())
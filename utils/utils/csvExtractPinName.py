import csv
import re

def extract_csv_element(csv_file_name):
    list_var = []
    list_end_with_1 = []
    list_end_with_2 = []
    list_end_with_3 = []
    list_end_with_4 = []
    list_end_normal = []
    # Load the csv data
    with open(csv_file_name, 'r', encoding='utf-8-sig') as csvfile:  # '\ufefftest' in csv file
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            for item in row:
                if item is not None and item != '':
                    if re.match('(.*)_1', item):
                        list_end_with_1.append(item)
                    elif re.match('(.*)_2', item):
                        list_end_with_2.append(item)
                    elif re.match('(.*)_3', item):
                        list_end_with_3.append(item)
                    elif re.match('(.*)_4', item):
                        list_end_with_4.append(item)
                    else:
                        list_end_normal.append(item)

    list_end_with_1.sort()
    list_end_with_2.sort()
    list_end_with_3.sort()
    list_end_with_4.sort()
    list_end_normal.sort()
    list_var = [list_end_with_1, list_end_with_2, list_end_with_3, list_end_with_4, list_end_normal]

    return list_var


if __name__ == '__main__':
    [list_1, list_2, list_3, list_4, list_normal] = extract_csv_element(r'./data/PINNAME_ONLY.csv')
    print([list_1, list_2, list_3, list_4, list_normal])

    len_max = max(len(list_1), len(list_2), len(list_3), len(list_4), len(list_normal))

    # write to csv file
    with open(r'./data/PINNAME_ONLY_sort.csv', 'w', newline='') as myfile:

        for i in range(len_max):
            myfile.write( (list_1[i] if i < len(list_1) else '') + ','
                        + (list_2[i] if i < len(list_2) else '') + ','
                        + (list_3[i] if i < len(list_3) else '') + ','
                        + (list_4[i] if i < len(list_4) else '') + ','
                        + (list_normal[i] if i < len(list_normal) else '') + '\n'
                        )

# unique
    unique_1 = list(set(list_1))
    unique_2 = list(set(list_2))
    unique_3 = list(set(list_3))
    unique_4 = list(set(list_4))
    unique_normal = list(set(list_normal))
    len_max_unique = max(len(unique_1), len(unique_2), len(unique_3), len(unique_4), len(unique_normal))

    with open(r'./data/PINNAME_ONLY_unique.csv', 'w', newline='') as myfile:
        for i in range(len_max_unique):
            myfile.write(   (unique_1[i] if i < len(unique_1) else '') + ','
                          + (unique_2[i] if i < len(unique_2) else '') + ','
                          + (unique_3[i] if i < len(unique_3) else '') + ','
                          + (unique_4[i] if i < len(unique_4) else '') + ','
                          + (unique_normal[i] if i < len(unique_normal) else '') + '\n'
                        )

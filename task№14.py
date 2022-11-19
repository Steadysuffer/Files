filename = r"filename.txt"


def get_popular_name_from_file(filename):
    name_list = []
    frequency_list = []
    popular_name = ''
    with open(filename, encoding='utf-8') as f:
        for line in f:
            name_list.append(line[:line.find(" ")])
        for i in name_list:
            if i == '':
                name_list.remove('')
        name_list.sort()
        frequency_of_occurrence = {i: name_list.count(i) for i in name_list}
        for i in frequency_of_occurrence.values():
            frequency_list.append(i)
        most_frequent = max(frequency_list)
        for i in frequency_of_occurrence.items():
            if i[1] == most_frequent:
                popular_name += str(i[0])
                popular_name += ', '
    return popular_name[:len(popular_name)-2]

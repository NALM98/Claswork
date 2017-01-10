def objectives(fname):
    text_file = open(fname, encoding = 'utf-8')
    s = text_file.read()
    word_list = s.split()
    text_file.close()
    linearr = []
    for item in word_list:
        i = len(item)
        end = item[i - 2:]
        if end == 'ый' or end == 'ий' or end == 'ой':
            linearr.append(item)
    return linearr
print(objectives(input()))

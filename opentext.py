def opentext(fname):
    text_file = open(fname, encoding = 'UTF-8')
    s = text_file.read()
    text_file.close()
    text_list = s.split()
    arr = []
    for item in text_list:
        item = item.lower()
        item = item.strip('. ? !, ()')
        arr.append(item)
    return arr

def first_letter(letter, lis):
    d = opentext(lis)
    arr = []
    for item in d:
        if item[0] == letter:
            arr.append(item)
    return arr

def questions():
    print('Type in any latin letter you like:')
    letter = input()
    print('Type in the name of the file:')
    a = input()
    print('Type in any number:')
    ciph = int(input())
    fin = first_letter(letter, a)
    fin_arr = []
    for item in fin:
        if len(item) >= ciph:
            fin_arr.append(item)
    return fin_arr



print(questions())
    


        
    

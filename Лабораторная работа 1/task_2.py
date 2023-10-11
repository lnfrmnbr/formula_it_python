v = 1.44 * 1024 * 1024
num_pages = 100
num_strings = 50
num_symbols = 25
v_of_symbol = 4

def count_books(v_, num_pages_, num_strings_, num_symbols_, v_of_symbol_):
    v_books = 0
    k = 0
    while v_books<v_:
        v_books+= num_pages_*num_strings_*num_symbols_*v_of_symbol_
        k+=1
    return k-1
print("Количество книг, помещающихся на дискету:", count_books(v, num_pages, num_strings, num_symbols, v_of_symbol))

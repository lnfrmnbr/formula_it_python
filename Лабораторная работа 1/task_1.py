numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

def change_skipped_el(ls):
    k = -1;
    summ = 0;
    for i in range(len(ls)):
        if ls[i] == None:
            k = i
        else:
            summ+=ls[i];
    ls[k] = summ/(len(ls))

change_skipped_el(numbers)

print("Измененный список:", numbers)

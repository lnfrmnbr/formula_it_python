def str_to_list(s, delimeter):
    ls = []
    name = ''
    for i in range(len(s)):
        if s[i] == delimeter:
            ls.append(name)
            name = ''
        elif i == len(s) - 1:
            name += s[i]
            ls.append(name)
        else:
            name += s[i]
    return ls


def find_common_participants(group1, group2, delimiter=','):
    ls_group1 = str_to_list(group1, delimiter)
    ls_group2 = str_to_list(group2, delimiter)
    ls_common = []
    for el in ls_group1:
        if el in ls_group2:
            ls_common.append(el)
    ls_common.sort()
    return ls_common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

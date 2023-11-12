import json


def task() -> float:
    summ = 0.0
    with open("input.json") as f:
        list_of_dict = json.load(f)
    for d in list_of_dict:
        summ += d["score"] * d["weight"]
    return round(summ, 3)


print(task()) 

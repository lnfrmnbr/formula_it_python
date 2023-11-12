import csv, json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ls = []
    with open(INPUT_FILENAME) as f_in:
        with open(OUTPUT_FILENAME, 'w') as f_out:
          lines = [line for line in csv.DictReader(f_in)]
          for line in lines:
            ls.append(line)
          f_out.write(json.dumps(ls, indent=4))


task()

with open(OUTPUT_FILENAME) as output_f:
  for line in output_f:
     print(line, end="")

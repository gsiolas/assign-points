#!/usr/bin/env python

import sys
import json
import os
import csv

input_file = sys.argv[1]
name_split = os.path.splitext(input_file)
output_file = name_split[0] + "-wp" + name_split[1]
correct_file = name_split[0] + "-corr.tsv"

rng = "12,24-69"
points_correct = 3
points_wrong = -1
points_missing = 0


def _parse_range(numbers: str):
    for x in numbers.split(','):
        x = x.strip()
        if x.isdigit():
            yield int(x)
        elif '-' in x:
            xr = x.split('-')
            yield from range(int(xr[0].strip()), int(xr[1].strip()) + 1)
        else:
            raise ValueError(f"Unknown range specified: {x}")


questions = []
for i in _parse_range(rng):
    if i % 3 == 0:
        questions.append(i)

if not os.path.isfile(correct_file):
    with open(input_file) as json_file:
        data = json.load(json_file)

    with open(correct_file, 'w', encoding='utf8') as corrfile:
        for lst_item in data:
            if lst_item["number"] in questions:
                line = str(lst_item["number"]) + "\t" + lst_item["question"].replace('\n', ' ') + "\t"
                if lst_item["number"] != questions[-1]:
                    line = line + "\n"
                corrfile.write(line)
                lst_item["points_correct"] = points_correct
                lst_item["points_wrong"] = points_wrong
                lst_item["points_missing"] = points_missing
    with open(output_file, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)
else:
    answersdict = {}
    with open(correct_file, newline='\n') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
            answersdict[row[0]] = row[2]
    with open(output_file) as json_file:
        data = json.load(json_file)
    for lst_item in data:
        q = lst_item["number"]
        if q in questions:
            lst_item["answer"] = answersdict.get(str(q))
    with open(output_file, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)

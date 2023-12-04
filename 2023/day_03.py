from collections import defaultdict, deque
from typing import TYPE_CHECKING

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(3, 2023)


def parse_raw(raw: str):
    raw = raw.splitlines()
    table = []
    for r in raw:
        line = []
        num = ""
        for c in r:
            #for part 1:
            # if c.isdigit():
                # line.append(c)
            # elif c == ".":
                # line.append(c)
            # else:
                # line.append("#")
        #for part 2:
            if c.isdigit():
                line.append(0)
                num = num+c
            elif c == ".":
                if num != "":
                    for i in range(len(num)):
                        line[-i-1] = int(num)
                    num = ""
                line.append(0)
            else:
                if num != "":
                    for i in range(len(num)):
                        line[-i-1] = int(num)
                    num = ""
                line.append(c)
        if num !="":
            for i in range(len(num)):
                line[-i-1] = int(num)
        #end part2
        table.append(line)
    return table


data = parse_raw(raw)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for i in range(len(data)):
        num = ""
        index = []
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                num=num+data[i][j]
                if i>0 and j > 0:
                    index.append((i-1, j-1))
                if i>0:
                    index.append((i-1, j))
                if i>0 and j < len(data[i])-1:
                    index.append((i-1, j+1))
                if j >0:
                    index.append((i, j-1))
                if j <len(data[i])-1:
                    index.append((i, j+1))
                if i<len(data)-1 and j > 0:
                    index.append((i+1, j-1))
                if i<len(data)-1:
                    index.append((i+1, j))
                if i<len(data)-1 and j < len(data[i])-1:
                    index.append((i+1, j+1))
            else:
                if num != "":
                    number = int(num)
                    num = ""
                    for pair in list(dict.fromkeys(index)):
                        if data[pair[0]][pair[1]] in "#*?$+/%":
                            sums = sums + number
                    index = []
        if num != "":
            number = int(num)
            num = ""
            for pair in list(dict.fromkeys(index)):
                if data[pair[0]][pair[1]] == "#":
                    sums = sums + number
            index = []
    return sums


#aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for i in range(len(data)):
        index = []
        for j in range(len(data[i])):
            if data[i][j] == "*":
                if i>0 and j > 0:
                    index.append((i-1, j-1))
                if i>0:
                    index.append((i-1, j))
                if i>0 and j < len(data[i])-1:
                    index.append((i-1, j+1))
                if j >0:
                    index.append((i, j-1))
                if j <len(data[i])-1:
                    index.append((i, j+1))
                if i<len(data)-1 and j > 0:
                    index.append((i+1, j-1))
                if i<len(data)-1:
                    index.append((i+1, j))
                if i<len(data)-1 and j < len(data[i])-1:
                    index.append((i+1, j+1))
                numbers = []
                for pair in list(dict.fromkeys(index)):
                    if data[pair[0]][pair[1]] != 0:
                        numbers.append(data[pair[0]][pair[1]])
                num_list = list(dict.fromkeys(numbers))
                if len(num_list) == 2:
                    prod = num_list[0]*num_list[1]
                    sums = sums + prod
                index = []
    return sums


aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_two)

#aoc_helper.lazy_submit(day=3, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2023, solution=part_two, data=data)

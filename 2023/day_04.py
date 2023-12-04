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

raw = aoc_helper.fetch(4, 2023)


def parse_raw(raw: str):
    raw = raw.splitlines()
    lines = []
    for r in raw:
        l = r.split(":")[1].strip()
        l = l.split("|")
        win, my_num = (l[0].strip().split(" "), l[1].strip().split(" "))
        win_int = []
        my_num_int = []
        for n in win:
            if n != "":
                win_int.append(int(n))
        for n in my_num:
            if n != "":
                my_num_int.append(int(n))
        lines.append(((win_int, my_num_int), 1))
    return lines


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for d in data:
        win = d[0][0]
        my = d[0][1]
        count = 0
        for n in win:
            if n in my:
                count = count +1
        if count != 0:
            sums = sums + pow(2, count-1)
    return sums


aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for i, d in enumerate(data):
        win = d[0][0]
        my = d[0][1]
        count = 0
        for n in win:
            if n in my:
                count = count +1
        print(count)
        for j in range(count):
            if i +j+ 1 < len(data):
                data[i+j+1] = (data[i+j+1][0], data[i+j+1][1] + 1*d[1])
        
    print(data)
    for d in data:
        sums = sums + d[1]
    return sums


aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2023, solution=part_two, data=data)

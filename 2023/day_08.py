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

from math import gcd

raw = aoc_helper.fetch(8, 2023)


def parse_raw(raw: str):
    data = {}
    raw = raw.splitlines()
    steps = raw.pop(0)
    raw.pop(0)
    for r in raw:
        data[r.split(" = ")[0]] = r.split(" = ")[1][1:-1].split(", ")
    return (steps, data)


data = parse_raw(raw)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    steps = data[0]
    current = "AAA"
    current_val = data[1][current]
    count = 0
    i = 0
    while current != "ZZZ":
        if i > len(steps)-1:
            i = 0
        if steps[i] == "R":
            current = current_val[1]
            current_val = data[1][current]
        elif steps[i] == "L":
            current = current_val[0]
            current_val = data[1][current]
        i += 1
        count += 1
    return count


aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    steps = data[0]
    keys = list(data[1].keys())
    search_keys = []
    count = 0
    for k in keys:
        if k[2] == 'A':
            search_keys.append(k)
    end = []
    i = 0
    print(search_keys)
    for k in search_keys:
        current = k
        current_val = data[1][k]
        while current[2] != "Z":
            if i > len(steps)-1:
                i = 0
            if steps[i] == "R":
                current = current_val[1]
                current_val = data[1][current]
            elif steps[i] == "L":
                current = current_val[0]
                current_val = data[1][current]
            i += 1
            count += 1
        end.append(count)
        count = 0
        i = 0
        
    lcm = 1
    for i in end:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2023, solution=part_two, data=data)

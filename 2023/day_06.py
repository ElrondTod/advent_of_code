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

raw = aoc_helper.fetch(6, 2023)


def parse_raw(raw: str):
    t = []
    t_2 = 0
    d = []
    d_2 = 0
    for r in raw.splitlines():
        if "Time" in r:
            t = list(map(int, r.split(": ")[1].split()))
            t_2= int(r.split(": ")[1].strip(" ").replace(" ", ""))
        elif "Distance" in r:
            d = list(map(int, r.split(": ")[1].split()))
            d_2= int(r.split(": ")[1].strip(" ").replace(" ", ""))
    return (list(zip(t, d)), (t_2, d_2))


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    prod = 1
    for t, d in data[0]:
        pos_time = []
        for i in range(t+1):
            if i * (t-i) > d:
                pos_time.append(i)
        prod *= len(pos_time)
    return prod
        


aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    pos_time = 0
    for i in range(data[1][0]):
        if i * (data[1][0]-i) > data[1][1]:
            pos_time +=1
    return pos_time


aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2023, solution=part_two, data=data)

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

raw = aoc_helper.fetch(2, 2023)


def parse_raw(raw: str):
    data = []
    for r in raw.splitlines():
        l = {"blue" : 0, "green" : 0, "red" : 0}
        r = r.split(":")[1][1:]
        r = r.split(";")
        for s in r:
            s = s.split(",")
            for c in s:
                c = c.lstrip().split(" ")
                if "blue" in c[1]:
                    if l["blue"] < int(c[0]):
                        l["blue"] = int(c[0])
                if "red" in c[1]:
                    if l["red"] < int(c[0]):
                        l["red"] = int(c[0])
                if "green" in c[1]:
                    if l["green"] < int(c[0]):
                        l["green"] = int(c[0])
        data.append(l)
        l = {"blue" : 0, "green" : 0, "red" : 0}
    return data


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for i in range(len(data)):
        if data[i]["red"] <= 12 and data[i]["green"] <= 13 and data[i]["blue"] <= 14:
            sums = sums + i + 1
    return sums


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    prod = 1
    for d in data:
        prod = d["red"] * d["blue"] * d["green"]
        sums = sums + prod
        prod = 0
    return sums


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2023, solution=part_two, data=data)

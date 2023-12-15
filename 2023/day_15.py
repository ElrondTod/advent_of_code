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

raw = aoc_helper.fetch(15, 2023)


def parse_raw(raw: str):
    data = [r for r in raw.split(",")]
    return data


data = parse_raw(raw)

def calc_hash(chars):
    hash_num = 0
    for c in chars:
        hash_num += ord(c)
        hash_num *= 17
        hash_num = hash_num % 256
    return hash_num

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for d in data:
        sums += calc_hash(d)
    return sums


aoc_helper.lazy_test(day=15, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    boxes = [{} for i in range(256)]
    sums = 0
    for d in data:
        cs = ""
        num = -1
        if d[-1] == "-":
            cs = d[:-1]
        else:
            cs, num = d.split("=")
        num = int(num)
        hash_num = calc_hash(cs)
        if num == -1 and cs in boxes[hash_num]:
            boxes[hash_num].pop(cs)
        elif num != -1:
            boxes[hash_num][cs] = num
    for i, b in enumerate(boxes):
        for j, h in enumerate(b.values()):
            sums += (i+1) * (j + 1) *h
    return sums


aoc_helper.lazy_test(day=15, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=15, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=15, year=2023, solution=part_two, data=data)

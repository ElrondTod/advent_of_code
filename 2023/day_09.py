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
    #list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(9, 2023)


def parse_raw(raw: str):
    data = []
    for r in raw.splitlines():
        data.append(list(map(int, r.split())))
    return data


data = parse_raw(raw)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for d in data:
        i = 0
        diff_list = [d]
        diff = []
        while not all(item == 0 for item in diff_list[i]):
            diff = [diff_list[i][j+1]-diff_list[i][j] for j in range(len(diff_list[i])-1)]
            diff_list.append(diff)
            i += 1
        prev = 0
        current = 0
        while i >= 0:
            current = diff_list[i][-1]+prev
            prev = current
            i -= 1
        sums += prev
    return sums


aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for d in data:
        i = 0
        diff_list = [d]
        diff = []
        while not all(item == 0 for item in diff_list[i]):
            diff = [diff_list[i][j+1]-diff_list[i][j] for j in range(len(diff_list[i])-1)]
            diff_list.append(diff)
            i += 1
        prev = 0
        current = 0
        while i >= 0:
            current = diff_list[i][0] - prev
            prev = current
            i -= 1
        sums += prev
    return sums


aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2023, solution=part_two, data=data)

from collections import defaultdict, deque
from typing import TYPE_CHECKING

from itertools import combinations
from itertools import repeat
from itertools import zip_longest

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

raw = aoc_helper.fetch(12, 2023)


def parse_raw(raw: str):
    data = [(r.split(" ")[0], list(map(int, r.split(" ")[1].split(",")))) for r in raw.splitlines()]
    return data

data = parse_raw(raw)

def gen(l, m, memed, i, j, count):
    if (i, j, count) in memed:
        return memed[(i, j, count)]
    if len(l) == i:
        if count == 0 and j == len(m):
            return 1
        elif count != 0 and j == len(m) - 1 and m[j] == count:
            return 1
        else:
            return 0
    sums = 0
    if l[i] == "?":
        # .
        if count == 0:
            sums += gen2(l, m, memed, i+1, j, count)
        elif count != 0 and j < len(m) and m[j] == count:
            sums += gen2(l, m, memed, i+1, j+1, 0)
        # #
        sums += gen2(l, m, memed, i+1, j, count +1)
    elif l[i] == ".":
        if count == 0:
            sums += gen2(l, m, memed, i+1, j, count)
        elif count != 0 and j < len(m) and m[j] == count:
            sums += gen2(l, m, memed, i+1, j+1, 0)
    elif l[i] == "#":
        sums += gen2(l, m, memed, i+1, j, count +1)
    memed[(i, j, count)] = sums
    return sums

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for m, n in data:
        p = gen2(m, n, {}, 0, 0, 0)
        sums += p
    return sums

aoc_helper.lazy_test(day=12, year=2023, parse=parse_raw, solution=part_one)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    i = 1
    for m, n in data:
        if 0 >= (len(m) - sum(n) -len(n)+1) <=1:
            sums += 1
            i+=1
            continue
        m = "?".join(repeat(m, 5))
        n = n*5
        p = gen(m, n, {}, 0, 0, 0)
        i+= 1
        sums += p
    return sums

aoc_helper.lazy_test(day=12, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2023, solution=part_two, data=data)

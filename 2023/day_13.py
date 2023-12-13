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

raw = aoc_helper.fetch(13, 2023)


def parse_raw(raw: str):
    data = [[k for k in r.splitlines()] for r in raw.split("\n\n")]
    return data


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for d in data:
        row = []
        for i, l in enumerate(d):
            for j, k in enumerate(d[i+1:]):
                if l == k:
                    row.append((i, i+j+1))
        row_v = 0
        for i in range(len(d)-1):
            if (i, i+1) in row:
                k = i-1
                n = i+2
                failed = False
                while (k >= 0 and n < len(d)) and not failed:
                    failed = not (k, n) in row
                    k -= 1
                    n += 1
                if not failed:
                    row_v = i+1
        d_t = [[d[j][i] for j in range(len(d))] for i in range(len(d[0]))]
        hor = []
        for i, l in enumerate(d_t):
            for j, k in enumerate(d_t[i+1:]):
                if l == k:
                    hor.append((i, i+j+1))
        hor_v = 0
        for i in range(len(d_t)-1):
            if (i, i+1) in hor:
                k = i-1
                n = i+2
                failed = False
                while (k >= 0 and n < len(d_t)) and not failed:
                    failed = not (k, n) in hor
                    k -= 1
                    n += 1
                if not failed:
                    hor_v = i+1
        sums += row_v*100+hor_v
    return sums


aoc_helper.lazy_test(day=13, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for d in data:
        for i in range(len(d)-1):
            count = 0
            k = i
            n = i+1
            while (k >= 0 and n < len(d)):
                count += list(map(lambda a: a[0] == a[1], zip(d[k], d[n]))).count(False)
                k -= 1
                n += 1
            if count == 1:
                sums += (i+1) * 100
        d_t = [[d[j][i] for j in range(len(d))] for i in range(len(d[0]))]
        for i in range(len(d_t)-1):
            count = 0
            k = i
            n = i+1
            while (k >= 0 and n < len(d_t)):
                count += list(map(lambda a: a[0] == a[1], zip(d_t[k], d_t[n]))).count(False)
                k -= 1
                n += 1
            if count == 1:
                sums += (i+1)
    return sums


aoc_helper.lazy_test(day=13, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=13, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=13, year=2023, solution=part_two, data=data)

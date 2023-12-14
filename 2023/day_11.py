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

raw = aoc_helper.fetch(11, 2023)


def parse_raw(raw: str):
    data = [list(r) for r in raw.splitlines()]
    return data


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    insert_lis = []
    for i in range(len(data)):
        if all(c == "." for c in data[i]):
            insert_lis.append(i)
    for i in insert_lis[::-1]:
        for k in range(10):
            data.insert(i, data[i].copy())
    data_t = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    insert_lis = []
    for i in range(len(data_t)):
        if all(c == "." for c in data_t[i]):
            insert_lis.append(i)
    for i in insert_lis[::-1]:
        for k in range(10):
            data_t.insert(i, data_t[i].copy())
    data = [[data_t[j][i] for j in range(len(data_t))] for i in range(len(data_t[0]))]
    gal_coor = []
    for i, d in enumerate(data):
        for j, c in enumerate(data[i]):
            if c == "#":
                gal_coor.append((i, j))
    
    sums = 0
    for i in range(len(gal_coor)):
        for j in range(i+1, len(gal_coor)):
            sums = sums + abs(gal_coor[i][0] - gal_coor[j][0]) + abs(gal_coor[i][1] - gal_coor[j][1])
            #pairs.append((gal_coor[i], gal_coor[j]))
    return sums


aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    gal_coor = []
    for i, d in enumerate(data):
        for j, c in enumerate(data[i]):
            if c == "#":
                gal_coor.append((i, j))
    insert_lis_x = []
    for i in range(len(data)):
        if all(c == "." for c in data[i]):
            insert_lis_x.append(i)
    data_t = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    insert_lis_y = []
    for i in range(len(data_t)):
        if all(c == "." for c in data_t[i]):
            insert_lis_y.append(i)
    
    new_gal_coor = []
    for i in range(len(gal_coor)):
        x_add = 0
        for k in insert_lis_x:
            if k <= gal_coor[i][0]:
                x_add += 999999
        y_add = 0
        for k in insert_lis_y:
            if k <= gal_coor[i][1]:
                y_add += 999999
        new_gal_coor.append((gal_coor[i][0]+x_add, gal_coor[i][1]+y_add))
       
    sums = 0
    for i in range(len(new_gal_coor)):
        for j in range(i+1, len(new_gal_coor)):
            sums = sums + abs(new_gal_coor[i][0] - new_gal_coor[j][0]) + abs(new_gal_coor[i][1] - new_gal_coor[j][1])
    return sums

aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2023, solution=part_one, data=data.copy())
aoc_helper.lazy_submit(day=11, year=2023, solution=part_two, data=data)

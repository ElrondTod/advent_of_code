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

import functools

raw = aoc_helper.fetch(7, 2023)


def parse_raw(raw: str):
    raw = raw.splitlines()
    cards = []
    cards2 = []
    for r in raw:
        card = r.split()
        CARD_LIST = "AKQJT98765432"
        CARD_LIST2 = "AKQT98765432"
        count_list = []
        count_list2 = []
        for c in CARD_LIST:
            count_list.append(card[0].count(c))
        for c in CARD_LIST2:
            count_list2.append(card[0].count(c) + card[0].count("J"))
        t = "h"
        if 5 in count_list:
            t = "5"
        elif 4 in count_list:
            t = "4"
        elif 3 in count_list and 2 in count_list:
            t = "f"
        elif 3 in count_list:
            t = "3"
        elif count_list.count(2) == 2:
            t = "22"
        elif count_list.count(2) == 1:
            t = "2"
        cards.append(((card[0], int(card[1])), t))
        t = "h"
        if 5 in count_list2:
            t = "5"
        elif 4 in count_list2:
            t = "4"
        elif 3 in count_list2 and 2 in count_list2 and card[0].count("J") == 0 or count_list2.count(3) == 2:
            t = "f"
        elif 3 in count_list2:
            t = "3"
        elif count_list2.count(2) == 2:
            t = "22"
        elif count_list2.count(2) == 1 or card[0].count("J") == 1:
            t = "2"
        cards2.append(((card[0], int(card[1])), t))
    return (cards, cards2)

def comp(i1, i2):
    CARD_LIST = "AKQJT98765432"
    for i in range(5):
        if i1[0][0][i] != i2[0][0][i]:
            if CARD_LIST.find(i1[0][0][i]) < CARD_LIST.find(i2[0][0][i]):
                return 1
            elif CARD_LIST.find(i1[0][0][i]) > CARD_LIST.find(i2[0][0][i]):
                return -1
    return 0
    
def comp2(i1, i2):
    CARD_LIST = "AKQT98765432J"
    for i in range(5):
        if i1[0][0][i] != i2[0][0][i]:
            if CARD_LIST.find(i1[0][0][i]) < CARD_LIST.find(i2[0][0][i]):
                return 1
            elif CARD_LIST.find(i1[0][0][i]) > CARD_LIST.find(i2[0][0][i]):
                return -1
    return 0


data = parse_raw(raw)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    fives = sorted([d for d in data[0] if '5' == d[1]], key=functools.cmp_to_key(comp))
    fours = sorted([d for d in data[0] if "4" == d[1]], key=functools.cmp_to_key(comp))
    full = sorted([d for d in data[0] if "f" == d[1]], key=functools.cmp_to_key(comp))
    threes = sorted([d for d in data[0] if "3" == d[1]], key=functools.cmp_to_key(comp))
    twop = sorted([d for d in data[0] if "22" == d[1]], key=functools.cmp_to_key(comp))
    pair = sorted([d for d in data[0] if "2" == d[1]], key=functools.cmp_to_key(comp))
    high = sorted([d for d in data[0] if "h" == d[1]], key=functools.cmp_to_key(comp))
    
    full_list = []
    if high is not None:
        full_list.extend(high)
    if pair is not None:
        full_list.extend(pair)
    if twop is not None:
        full_list.extend(twop)
    if threes is not None:
        full_list.extend(threes)
    if full is not None:
        full_list.extend(full)
    if fours is not None:
        full_list.extend(fours)
    if fives is not None:
        full_list.extend(fives)
    
    for i, f in enumerate(full_list):
        sums += f[0][1] * (i+1)
    
    return sums


aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    fives = sorted([d for d in data[1] if '5' == d[1]], key=functools.cmp_to_key(comp2))
    fours = sorted([d for d in data[1] if "4" == d[1]], key=functools.cmp_to_key(comp2))
    full = sorted([d for d in data[1] if "f" == d[1]], key=functools.cmp_to_key(comp2))
    threes = sorted([d for d in data[1] if "3" == d[1]], key=functools.cmp_to_key(comp2))
    twop = sorted([d for d in data[1] if "22" == d[1]], key=functools.cmp_to_key(comp2))
    pair = sorted([d for d in data[1] if "2" == d[1]], key=functools.cmp_to_key(comp2))
    high = sorted([d for d in data[1] if "h" == d[1]], key=functools.cmp_to_key(comp2))

    full_list = []
    if high is not None:
        full_list.extend(high)
    if pair is not None:
        full_list.extend(pair)
    if twop is not None:
        full_list.extend(twop)
    if threes is not None:
        full_list.extend(threes)
    if full is not None:
        full_list.extend(full)
    if fours is not None:
        full_list.extend(fours)
    if fives is not None:
        full_list.extend(fives)
    
    for i, f in enumerate(full_list):
        sums += f[0][1] * (i+1)
    
    return sums


aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2023, solution=part_two, data=data)

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

raw = aoc_helper.fetch(1, 2023)


def parse_raw(raw: str):
    numbers = []
    number = ""
    sums = 0
    for r in raw.splitlines():
        #for part 2
        r = r.replace("one", "one1one")
        r = r.replace("two", "two2two")
        r = r.replace("three", "three3three")
        r = r.replace("four", "four4four")
        r = r.replace("five", "five5five")
        r = r.replace("six", "six6six")
        r = r.replace("seven", "seven7seven")
        r = r.replace("eight", "eight8eight")
        r = r.replace("nine", "nine9nine")
        #end of part2
        for c in r:
            if str.isdigit(c):
               number = number + c
               break;
        for c in r[::-1]:
            if str.isdigit(c):
               number = number + c
               break;
        numbers.append(int(number))
        number = ""
    return numbers

data = parse_raw(raw)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for n in data:
        sums = sums + n
    return sums


aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for n in data:
        sums = sums + n
    return sums


aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2023, solution=part_two, data=data)

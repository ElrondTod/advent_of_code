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

raw = aoc_helper.fetch(14, 2023)


def parse_raw(raw: str):
    data = [list(r) for r in raw.splitlines()]
    return data


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O":
                k = i-1
                while k>= 0 and data[k][j] =='.':
                    k -= 1
                data[i][j] = '.'
                data[k+1][j] = 'O'
    for i, d in enumerate(data):
        sums += d.count("O") * (len(data) - i)
    return sums


aoc_helper.lazy_test(day=14, year=2023, parse=parse_raw, solution=part_one)


def guess_seq_len(seq):
    guess = -1
    max_len = int(len(seq) / 2)
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    # print("\n".join(["".join(row) for row in data]))
    # print()
    count_list = []
    for i in range(1000):
        count = 0
        for i in range(1, len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "O":
                    k = i-1
                    while k>= 0 and data[k][j] =='.':
                        k -= 1
                    data[i][j] = '.'
                    data[k+1][j] = 'O'
        # print("\n".join(["".join(row) for row in data]))
        # print()
        for i in range(len(data)):
            for j in range(0, len(data[i])):
                if data[i][j] == "O":
                    k = j-1
                    while k>= 0 and data[i][k] =='.':
                        k -= 1
                    data[i][j] = '.'
                    data[i][k+1] = 'O'
        # print("\n".join(["".join(row) for row in data]))
        # print()
        for i in range(len(data)-2,-1, -1):
            for j in range(len(data[i])):
                if data[i][j] == "O":
                    k = i+1
                    while k< len(data) and data[k][j] =='.':
                        k += 1
                    data[i][j] = '.'
                    data[k-1][j] = 'O'
        # print("\n".join(["".join(row) for row in data]))
        # print()
        for i in range(len(data)):
            for j in range(len(data[i])-2, -1, -1):
                if data[i][j] == "O":
                    k = j+1
                    while k< len(data[i]) and data[i][k] =='.':
                        k += 1
                    data[i][j] = '.'
                    data[i][k-1] = 'O'
        for i, d in enumerate(data):
            count += d.count("O") * (len(data) - i)
        count_list.append(count)
    inv = []
    prev = 0
    prev_2 = 0
    guess = 0
   
    for i in range(len(count_list)):
        guess = guess_seq_len(count_list[i:])
        if guess == prev and guess == prev_2:
            break
        else:
            inv.append(guess)
            if guess != -1:
                prev_2 = prev
                prev = guess
    return count_list[(1000000000-len(inv)+2)%guess+len(inv)-2-1]


aoc_helper.lazy_test(day=14, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=14, year=2023, solution=part_one, data=data.copy())
aoc_helper.lazy_submit(day=14, year=2023, solution=part_two, data=data)

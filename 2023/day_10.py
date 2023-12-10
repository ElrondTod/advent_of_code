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

raw = aoc_helper.fetch(10, 2023)


def parse_raw(raw: str):
    data = [[c for c in r] for r in raw.splitlines()]
    pos_s = ()
    for i, d in enumerate(data):
        if 'S' in d:
            pos_s = (i, d.index('S'))
            break;
    if data[pos_s[0]-1][pos_s[1]] in "|7F":
        if data[pos_s[0]][pos_s[1]+1] in "-J7":
            data[pos_s[0]][pos_s[1]] = 'L'
        elif data[pos_s[0]+1][pos_s[1]] in "|LJ":
            data[pos_s[0]][pos_s[1]] = '|'
        elif data[pos_s[0]][pos_s[1]-1] in "-LF":
            data[pos_s[0]][pos_s[1]] = 'J'
    elif data[pos_s[0]][pos_s[1]+1] in "-J7":
        if data[pos_s[0]+1][pos_s[1]] in "|LJ":
            data[pos_s[0]][pos_s[1]] = 'F'
        elif data[pos_s[0]][pos_s[1]-1] in "-LF":
            data[pos_s[0]][pos_s[1]] = '-'
    elif data[pos_s[0]+1][pos_s[1]] in "|LJ":
        if data[pos_s[0]][pos_s[1]-1] in "-LF":
            data[pos_s[0]][pos_s[1]] = '7'
    return (data, pos_s)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    dis = [[-1 for j in range(len(data[0][0]))] for i in range(len(data[0]))]
    d, start = data
    dis[start[0]][start[1]] = 0
    queue = []
    
    pos_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    if d[start[0]][start[1]] in "|LJ":
        queue.append((tuple(map(sum, zip(pos_list[0], start))), 1))
    if d[start[0]][start[1]] in "-LF":
        queue.append((tuple(map(sum, zip(pos_list[3], start))), 1))
    if d[start[0]][start[1]] in "|7F":
        queue.append((tuple(map(sum, zip(pos_list[2], start))), 1))
    if d[start[0]][start[1]] in "-7J":
        queue.append((tuple(map(sum, zip(pos_list[1], start))), 1))
    
    max_dis = 0
    while len(queue) != 0:
        actual, dist = queue.pop(0)
        dis[actual[0]][actual[1]] = dist
        if dist > max_dis:
            max_dis = dist
        new_pos =  tuple(map(sum, zip(pos_list[0], actual)))
        if d[actual[0]][actual[1]] in "|LJ" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == -1:
            queue.append((new_pos, dist+1))
        new_pos =  tuple(map(sum, zip(pos_list[3], actual)))
        if d[actual[0]][actual[1]] in "-LF" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == -1:
            queue.append((new_pos, dist+1))
        new_pos =  tuple(map(sum, zip(pos_list[2], actual)))
        if d[actual[0]][actual[1]] in "|7F" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == -1:
            queue.append((new_pos, dist+1))
        new_pos =  tuple(map(sum, zip(pos_list[1], actual)))
        if d[actual[0]][actual[1]] in "-7J" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == -1:
            queue.append((new_pos, dist+1))
    
    return max_dis


aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    dis = [[1 for j in range(len(data[0][0]))] for i in range(len(data[0]))]
    d, start = data
    dis[start[0]][start[1]] = d[start[0]][start[1]]
    queue = []
    
    pos_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    if d[start[0]][start[1]] in "|LJ":
        new_pos = tuple(map(sum, zip(pos_list[0], start)))
        queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
    if d[start[0]][start[1]] in "-LF":
        new_pos = tuple(map(sum, zip(pos_list[3], start)))
        queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
    if d[start[0]][start[1]] in "|7F":
        new_pos = tuple(map(sum, zip(pos_list[3], start)))
        queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
    if d[start[0]][start[1]] in "-7J":
        new_pos = tuple(map(sum, zip(pos_list[3], start)))
        queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
    
    while len(queue) != 0:
        actual, dist = queue.pop(0)
        dis[actual[0]][actual[1]] = dist
        new_pos =  tuple(map(sum, zip(pos_list[0], actual)))
        if d[actual[0]][actual[1]] in "|LJ" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == 1:
            queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
        new_pos =  tuple(map(sum, zip(pos_list[3], actual)))
        if d[actual[0]][actual[1]] in "-LF" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == 1:
            queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
        new_pos =  tuple(map(sum, zip(pos_list[2], actual)))
        if d[actual[0]][actual[1]] in "|7F" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == 1:
            queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
        new_pos =  tuple(map(sum, zip(pos_list[1], actual)))
        if d[actual[0]][actual[1]] in "-7J" and new_pos not in queue and dis[new_pos[0]][new_pos[1]] == 1:
            queue.append((new_pos, d[new_pos[0]][new_pos[1]]))
    
    count = 0
    for i, d in enumerate(dis):
        count_pipes = 0
        for j, c in enumerate(d):
            if c != 1:
                if count_pipes == 0 and c in "|F7":
                    count_pipes = 1
                elif count_pipes == 1 and c in "|F7":
                    count_pipes = 0
            if c == 1 and count_pipes == 1:
                count += 1
                dis[i][j] = "O"
    # for d in dis:
        # print(''.join(list(map(str, d))))
    return count


aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2023, solution=part_two, data=data)

from enum import Enum
from functools import cmp_to_key
from part1 import Order, compare

def cmp(a, b):
    match (compare(a, b)):
        case Order.WRONG:
            return 1
        case Order.EQUAL:
            return 0
        case Order.RIGHT:
            return -1

def solution(packets):
    packets = [i for s in packets for i in s] + [[[2]], [[6]]]
    packets = list(sorted(packets, key=cmp_to_key(cmp)))

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

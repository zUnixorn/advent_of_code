from enum import Enum

class Order(Enum):
    WRONG = 0
    RIGHT = 1
    EQUAL = 2

def compare(lhs, rhs):
    lhs_int = isinstance(lhs, int)
    rhs_int = isinstance(rhs, int)

    if lhs_int and rhs_int:
        if lhs == rhs:
            return Order.EQUAL
        else:
            return (Order(int(lhs < rhs)))
    
    if lhs_int and not rhs_int:
        return compare([lhs], rhs)

    if not lhs_int and rhs_int:
        return compare(lhs, [rhs])

    for sides in zip(lhs, rhs):
        comparison = compare(sides[0], sides[1])

        if comparison != Order.EQUAL:
            return comparison

    return compare(len(lhs), len(rhs))

def solution(packets):
    parts = 0

    for i in range(len(packets)):
        if compare(packets[i][0], packets[i][1]) == Order.RIGHT:
            parts += i + 1

    return parts

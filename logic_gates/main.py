from gates import *
from test import *

if __name__ == '__main__':
    variants = [(False, False), (False, True), (True, False), (True, True)]
    and_gate = AND()
    not_gate = NOT()
    nor_gate = NOR()

    for variant in variants:
        and_gate.set_a(variant[0])
        and_gate.set_b(variant[1])
        not_gate.set_a(variant[1])
        nor_gate.set_a(and_gate.get_out())
        nor_gate.set_b(not_gate.get_out())
        print(nor_gate.get_out())

def test_gate(gate):
    print("Test Gate:")
    variants = [(False, False), (False, True), (True, False), (True, True)]
    for variant in variants:
        gate.set_a(variant[0])
        gate.set_b(variant[1])
        print(gate.get_out())
    print("---")

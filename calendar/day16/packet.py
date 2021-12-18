class BitReader:
    def __init__(self, bits):
        self.bits = bits
        self.bits_read = 0

    def read(self, n):
        self.bits_read += n
        return (next(self.bits) for i in range(n))


def product(*args):
    prod = 1
    for n in args:
        prod *= n
    return prod


OPERATIONS = {
    0: lambda *x: sum(x),
    1: lambda *x: product(x),
    2: lambda *x: min(x),
    3: lambda *x: max(x),
    5: lambda x, y: int(x > y),
    6: lambda x, y: int(x < y),
    7: lambda x, y: int(x == y),
}


class Packet:
    def __init__(self, version, type_id, params):
        self.version = version
        self.type_id = type_id
        self.params = params

    def get_version_total(self):
        total = self.version
        if "subpackets" in self.params:
            for subpacket in self.params["subpackets"]:
                total += subpacket.get_version_total()
        return total

    def evaluate(self, verbose=False):
        op = self.type_id
        if op == 4:
            ret_val = self.params["literal"]
        else:
            args = [p.evaluate(verbose) for p in self.params["subpackets"]]
            operation = OPERATIONS[op]
            ret_val = operation(*args)
        if verbose:
            print(f"Evaluating ({op}): {ret_val}")
        return ret_val

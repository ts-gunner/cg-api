from decimal import Decimal


def round_1(number: float):
    return Decimal(number).quantize(Decimal("0.0"))


def round_2(number: float):
    return Decimal(number).quantize(Decimal("0.00"))


if __name__ == '__main__':
    print(round_1(2.8))

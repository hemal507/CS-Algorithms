from fractions import Fraction


def videoPart(p, t):
    l = lambda v: sum([int(i) * j for i, j in zip(v.split(":"), [3600, 60, 1])])
    n = l(p)
    d = l(t)
    r = Fraction(n, d)
    return [r.numerator, r.denominator]

print(videoPart("02:20:00", "07:00:00"))
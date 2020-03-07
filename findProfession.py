findProfession = lambda l,p : "Engineer" if bin(p - 1).count('1') % 2 == 0 else "Doctor"

print(findProfession(3,3))
print(findProfession(4,2))
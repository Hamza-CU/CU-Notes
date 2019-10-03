p1 = float(input("input price 1: "))
p2 = float(input("input price 2: "))
p3 = float(input("input price 3: "))

sub1 = abs(5 - (p1 * 0.87))
sub2 = abs(5 - (p2 * 0.87))
sub3 = abs(5 - (p3 * 0.87))

if sub1 < sub2 and sub1 < sub3:
    print(p1, "CAD is the closest to 5 USD")
elif sub2 < sub1 and sub2 < sub3:
    print(p2, "CAD is the closest to 5 USD")
else:
    print(p3, "CAD is the closest to 5 USD")

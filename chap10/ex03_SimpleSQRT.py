number = int(input("simple sqrt: "))
sqrt = 0
while((sqrt + 1) * (sqrt + 1) <= number):
    sqrt += 1
print(sqrt)
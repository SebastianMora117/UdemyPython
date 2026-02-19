def suma(**kwarg):
    total = 0
    for c, v in kwarg.items():
        print(f"{c} = {v}")
        total += v
    return total

print(suma(x=2, y=3, z =4))
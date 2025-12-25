with open("multiplication.txt", "w") as f:
    for a in range(2, 21):
        j = 1
        while j <= 10:
            var = a * j
            f.write(f"{a} x {j} = {a * j}\n")
            j += 1

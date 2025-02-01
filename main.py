while True:
    try:
        a = int(input("Temperature in F\n: "))
        f = (a - 32) * 5 / 9
        print(f"Temperature in C: {f:.1f}")
        print("  ")
    except ValueError:
        print("Incorrect data formal!")

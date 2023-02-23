if args is not None:
    try:
        print(open(args[0], encoding='utf-8').read())
    except FileNotFoundError:
        print(f"No such file - {args[0]}")
else:
    print("Argument not found - file.")


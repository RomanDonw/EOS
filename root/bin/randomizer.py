import random

if args is not None:
    min_num = int(args[0])
    max_num = int(args[1])
    random_num = random.randint(min_num, max_num)
    print(f"Random number between\n  {min_num} and {max_num} is {random_num}.")
else:
    print("Arguments not found.")
    


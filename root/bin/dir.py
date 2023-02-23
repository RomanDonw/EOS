if args is not None:
    files = os.listdir(args[0])
else:
    files = os.listdir(ROOT_PATH)
    
for file in files:
    if os.path.isdir(file):
        print(f"{file}  <DIR>")
    else:
        print(file)

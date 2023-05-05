import sys

if len(sys.argv) != 2:
    print("missing command line ")
    sys.exit(1)
else:
   print(f"hello,{sys.argv[1]}")
   sys.exit(0) 
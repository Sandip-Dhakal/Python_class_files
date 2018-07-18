import sys

def sum( *args):
    total = 0
    arg = args[1:]
    for x in arg:
        total += int(x)
    return total

if __name__ == "__main__":
    print(sys.argv)
    print(sum(*sys.argv))

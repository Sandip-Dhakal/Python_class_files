import sys

def sum_avg( *args):
    total = 0
    arg = args[1:]
    for x in arg:
        total += int(x)
    return total, int(total/len(arg))

if __name__ == "__main__":
    print(sys.argv)
    print(sum_avg(*sys.argv))


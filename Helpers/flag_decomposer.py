print("Utility for finding individual flag values present in decimal integer.")
print("Also defines deflag(int) for e.g. further interactive shell use.")
print("Enter integer:")
target = int(input())

def deflag(composed_integer):
    print("Flag values:")
    for i in range(0, 64):
        if composed_integer & (1 << i):
            print(1 << i)

deflag(target)

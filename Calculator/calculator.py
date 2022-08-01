import statistics
import pandas as pd
from collections import namedtuple
from math import floor

print("Made By b9803bd23b22b214707ab49402510c57b6dcbb684155b183b7d94d31a840c3a3")
print("Put in your numbers with spaces between them")
print("They no not have to be in order")
print("\n")

def stemplot(stem):
    d = []
    interval = float(10**float(stem.leafdigits))
    for data in sorted(stem.data):
        data = float(floor(data))
        stm, lf = divmod(data,interval)
        d.append( (float(stm), float(lf)) )
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s,l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % ( stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    out.append('\n\nKey:\n Stem multiplier: %i\n X | Y  =>  %i*X+Y\n'
               % (interval, interval))
    return ''.join(out)

def main():  
    str_input = input(": ")
    lst = str_input.split()
    data = [float(x) for x in lst]

    int_min = float(min(data))
    int_max = float(max(data))

    frequency = {
        'Number':lst,
    }
    df = pd.DataFrame(frequency)

    Stem = namedtuple('Stem', 'data, leafdigits')
    Stem_Data = Stem((data),
                    1.0)

    print("\n")
    print("Data: " + str_input)
    print("Mean: " + str(statistics.mean(data)))
    print("Mode: " + str(statistics.multimode(data)))
    print("Median: " + str(statistics.median(data)))
    print("Range: " + str(int_max - int_min))
    print("\n")
    print("Frequency Table")
    print( df[['Number']].value_counts())
    print("\n")
    print("Stem Leaf Plot")
    print( stemplot(Stem_Data))
    print("\n")

while True:
    main()
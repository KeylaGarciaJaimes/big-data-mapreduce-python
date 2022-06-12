#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    list = []
    for line in sys.stdin:
        line = line.strip("\n")
        key, val = line.split(",")
        val = float(val)

        list.append((key, val))

    d = {}
    for x, y in list:
        d.setdefault(x, []).append(y)

    for x, y in d.items():
        sys.stdout.write("{}\t{}\t{}\n".format(x, sum(y), (sum(y)/len(y))))
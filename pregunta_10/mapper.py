#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        list = line.split("\t")
        sys.stdout.write("{}\t{}".format(list[0], list[1]))
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    list = []

    for line in sys.stdin:
        key, val1, val2 = line.split(",")
        val2 = int(val2)

        list.append((key, val1, val2))

        list.sort(key=lambda i: i[2], reverse=False)

    for element in list[0:6]:
        sys.stdout.write("{}   {}   {}\n".format(element[0], element[1], element[2]))
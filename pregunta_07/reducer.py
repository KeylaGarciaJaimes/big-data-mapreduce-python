#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista1 = []

    for line in sys.stdin:
        key, val1, val2 = line.split(",")
        val2 = int(val2)

        lista1.append((key, val1, val2))

        lista1.sort(key=lambda i: (i[0], i[2]), reverse=False)

    for element in lista1:
        sys.stdout.write("{}   {}   {}\n".format(element[0], element[1], element[2]))
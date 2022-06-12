#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    import sys

import sys

if __name__ == "__main__":

    list = []
    
    for line in sys.stdin:

        key, val = line.split(",")
        val = int(val)

        list.append((key, val))

        list.sort(key=lambda i: i[1], reverse=False)

    for element in list:
        sys.stdout.write("{},{}\n".format(element[0], element[1]))
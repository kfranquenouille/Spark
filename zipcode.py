from __future__ import print_function

import csv
import sys
from random import random
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    """
        Usage: zipcode [partitions] [department] [outputFile]
    """
    if len(sys.argv) < 4:
    	print("Usage: zipcode [partitions] [department] [outputFile]")
    	sys.exit(0)

    sc = SparkContext(appName="PythonZipCode")
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    liste =[]
    output = "(===||:::::::::::::::>  NB DE VILLES  <:::::::::::::::||===)\n\n"

    cr = csv.reader(open("base.csv","rb"), delimiter=';', quotechar='|')
    for row in cr:
        if (row[2].startswith( sys.argv[2] )):
            tmp = []
            tmp.append(1)
            liste.append( tmp )
            output = output + row[2] + " - " + row[1] + "\n"

    villesChoisies = sc.parallelize(liste).flatMap(lambda z: z).reduce(lambda x,y: x+y)
    
    output = output + "\nTOTAL : " + str(villesChoisies) + "\n----------------------- ( o ) ( o ) ------------------------"

    text_file = open(sys.argv[3], "w")
    text_file.write("%s" % output)
    text_file.close()

    sc.stop()
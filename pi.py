from __future__ import print_function

import csv
import sys
from random import random
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    sc = SparkContext(appName="PythonPi")
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    #count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    #cr = csv.reader(open("base.csv","rb"), delimiter=';', quotechar='|')
    sc.textFile("/home/base.csv").map(lambda line: line.split(";")).filter(lambda line: len(line)<=1).collect()
    #villesChoisies = sc.parallelize(list(cr)).map().reduce(lambda a, b: a + b)
    #print("%s" % (villesChoisies))
    #for row in cr:
   	#    print(row[2], row[1])
    #print("---------------((((((---------------")
    #print(list(cr))
    sc.stop()
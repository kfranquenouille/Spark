import csv
import sys
from random import random
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
   """
       Usage: zipcode [department] [outputFile]
   """
   if len(sys.argv) < 3:
       print("Usage: zipcode [department] [outputFile]")
       sys.exit(0)

   sc = SparkContext(appName="PythonZipCode")

   liste =[]
   output = "(===||:::::::::::::::>  NB DE VILLES  <:::::::::::::::||===)\n"

   cr = csv.reader(open("base.csv","rb"), delimiter=';', quotechar='|')
   lines=list(cr)

   # On parallelise le decoupage des villes en map et on reduit par les clés (code postal)
   villesChoisies = sc.parallelize(lines).map(lambda z: (z[2], 1)).reduceByKey(add)
   res = villesChoisies.collect()
   
   num_ville = 0

   # On recherche en fonction de la ville et on compte le nombre de villes par département
   for (ville, count) in res:
       if (ville.startswith(sys.argv[1])):
           num_ville += count

   print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
   print (num_ville)
   print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

   output = output + "TOTAL : " + str(num_ville) + "\n----------------------- ( o ) ( o ) ------------------------"

   text_file = open(sys.argv[2], "w")
   text_file.write("%s" % output)
   text_file.close()

   sc.stop()

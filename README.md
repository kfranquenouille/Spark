# Spark
Tutoriel d'utilisation d'Apache Spark pour le cours de SID en Master TIIR @ Université de Lille 1

## Installation d'un Docker Spark
### Sous Linux
Il faut d'abord installer Docker.io avec les librairies correspondantes. Pour cela, il faut executer le script docker.sh.

Une fois cela fait, il faut récupérer le container contenant Spark. La commande docker pull sequenceiq/spark:1.6.0 permet cela

###Sous Windows



## Utilisation de Spark
docker run -it --rm -p 8042:8042 -p 8080-8088:8080-8088 -h sandbox sequenceiq/spark:1.6.0 bash

cd /usr/local/spark

bash sbin/start-all.sh  // non fonctionnel

bash sbin/start-slave.sh spark://sandbox:7077

MASTER=spark://sandbox:7077 pyspark

##Sources 
 * [https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/][1]
 * [http://www.toptal.com/spark/introduction-to-apache-spark][2]
 * [https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python][3]
 * [http://www.tutorialspoint.com/apache_spark/apache_spark_core_programming.htm][4]
 * [http://spark.apache.org/docs/latest/quick-start.html][5]
 * [http://spark.apache.org/documentation.html][6]
 * [http://spark.apache.org/docs/latest/spark-standalone.html][7]

###Writting code ###

    #!javascript
    function hi(){
        alert('hi!');
    }


  [1]: https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/
  [2]: http://www.toptal.com/spark/introduction-to-apache-spark
  [3]: https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python
  [4]: http://www.tutorialspoint.com/apache_spark/apache_spark_core_programming.htm
  [5]: http://spark.apache.org/docs/latest/quick-start.html
  [6]: http://spark.apache.org/documentation.html
  [7]: http://spark.apache.org/docs/latest/spark-standalone.html


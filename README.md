# Spark

Tutoriel d'utilisation d'Apache Spark pour le cours de SID en Master TIIR @ Université de Lille 1

[TOC]

## Installation d'un Docker Spark
### Sous Linux
Il faut d'abord installer Docker.io avec les librairies correspondantes. Pour cela, il faut executer le script docker.sh.

Une fois cela fait, il faut récupérer le container contenant Spark. La commande ci dessous permet cela.

    docker pull sequenceiq/spark:1.6.0

###Sous Windows
Installer le logiciel Docker sous Windows



## Utilisation de Spark
    
    docker run -it --rm -p 8042:8042 -p 8080-8088:8080-8088 -h sandbox sequenceiq/spark:1.6.0 bash
    cd /usr/local/spark
    bash sbin/start-all.sh  // non fonctionnel
    bash sbin/start-slave.sh spark://sandbox:7077
    MASTER=spark://sandbox:7077 pyspark

Pour acceder à l'interface web du container Docker, il suffit d'aller sur http://localhost:8080/

##Sources 
 * https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/
 * http://www.toptal.com/spark/introduction-to-apache-spark
 * https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python
 * http://www.tutorialspoint.com/apache_spark/apache_spark_core_programming.htm
 * http://spark.apache.org/docs/latest/quick-start.html
 * http://spark.apache.org/documentation.html
 * http://spark.apache.org/docs/latest/spark-standalone.html
 * https://blog.cloudera.com/blog/2014/09/how-to-translate-from-mapreduce-to-apache-spark/
 * http://spark.apache.org/docs/latest/
 * http://www.ipponusa.com/blog/intro-mapreduce-spark/
 * https://www.gitbook.com/book/jaceklaskowski/mastering-apache-spark/details


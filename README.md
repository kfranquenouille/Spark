# Spark

Tutoriel d'utilisation d'Apache Spark pour le cours de SID en Master TIIR @ Université de Lille 1

##Table des matières
[toc]

## Installation d'un Docker Spark
### Sous Linux
Il faut d'abord installer Docker.io avec les librairies correspondantes. Pour cela, il faut exécuter le script ```docker.sh```.

Une fois cela fait, il faut récupérer le container contenant Spark. La commande ci dessous permet cela.

    docker pull sequenceiq/ spark:1.6.0

###Sous Windows
Installer le logiciel Docker sous Windows disponible à l'adresse suivante :
https://docs.docker.com/engine/installation/windows/


## Utilisation de Spark

Pour lancer le master, voici les commandes à exécuter :
   
    docker run -it --rm -v $HOME/Documents/sid/tp-spark:/home -p 8080:8080 -p 7077:7077 --name master -h master sequenceiq/spark:1.6.0 bash
    cd /usr/local/spark
    bash sbin/start-master.sh

Pour les slaves, il s'agit des commandes suivantes :     

    docker run -d --name slaves -v $HOME/Documents/sid/tp-spark:/home -e SPARK_MASTER_IP=192.168.12.106 -e SPARK_WORKER_CORES=1 -e SPARK_WORKER_MEMORY=1g -e SPARK_WORKER_INSTANCES=4 sequenceiq/spark:1.6.0 '/usr/local/spark/sbin/start-slave.sh spark://${SPARK_MASTER_IP}:7077 ; tail -f /usr/local/spark/logs/*'
    4348a9f97a3f6330437e53eaac4bcd63046ce051d18ca00eba1742c99430b409
    
    docker logs -f 4348a9f97a3f

    docker exec -it NOM_CONTAINER bash          #Pour obtenir le bash 

Pour acceder à l'interface web du container Docker, il suffit d'aller sur http://localhost:8080/

Depuis le master, si l'on souhaite exécuter un programme, voici la commande :

    MASTER=spark://192.168.12.106:7077 spark-submit zipcode.py 50 59 villes.txt

Dans le fichier de sortie, les villes sont listées par ordre alphabétiques et sont référencées avec leur code postal. A la fin du fichier, on y trouve le nombre total de villes présentes dans le département.

##Sources pour l'algorithme
 * http://researchcomputing.github.io/meetup_spring_2014/python/spark.html //Documentation principale
 * https://github.com/demibenari/spark-example
 * https://github.com/aseigneurin/spark-sandbox
 * http://web.cs.ucla.edu/~spencertung/CS239/ @Pi Estimator
 * https://github.com/apache/spark
 * http://beekeeperdata.com/posts/hadoop/2015/12/14/spark-scala-tutorial.html

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


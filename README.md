# Spark
Tutoriel d'utilisation d'Apache Spark pour le cours de SID en Master TIIR @ Université de Lille 1

## Installation d'un Docker Spark
### Sous Linux
toto




## Utilisation de Spark
docker run -it --rm -p 8042:8042 -p 8080-8088:8080-8088 -h sandbox sequenceiq/spark:1.6.0 bash

cd /usr/local/spark

bash sbin/start-all.sh  // non fonctionnel

bash sbin/start-slave.sh spark://sandbox:7077

MASTER=spark://sandbox:7077 pyspark

### Writting code ###

    #!javascript
    function hi(){
        alert('hi!');
    }



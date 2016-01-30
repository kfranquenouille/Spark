import scala.math.random
import org.apache.spark._

object SparkPi {
	def main(args: Array[String]) {
		val conf = new SparkConf().setAppName("Spark test")
		val spark = new SparkContext(conf)
		val villes = spark.textFile(args(0))
		val villesChoisies = villes.filter(line => line.split("0")(2).startsWith("08"))
		/**
		val slices = if (args.length > 0) args(0).toInt else 2
		val n = math.min(100000L * slices, Int.MaxValue).toInt // avoid overflow
		val count = spark.parallelize(1 until n, slices).map 
		{ i =>
			i.length
		}.reduce(_ + _)
		*/
		villesChoisies.saveAsTextFile(args(1))
		println("NOMBRE DE VILLES : " + count / n)
		spark.stop()
	}
}



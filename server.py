import findspark
findspark.init()  # Initialize PySpark

from pyspark.sql import SparkSession

# Create the SparkSession
spark = SparkSession.builder \
    .appName('quakes_etl') \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:2.4.1') \
    .getOrCreate()

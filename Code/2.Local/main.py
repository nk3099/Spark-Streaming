from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,split

if __name__=='__main__':
    print("creating spark session")

    spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Neeraj Spark Streaming") \
    .config("spark.sql.shuffle.partitions","8") \
    .getOrCreate()


#read the data
    lines = spark.readStream.format("socket") \
        .option("host","localhost") \
        .option("port","9998") \
        .load()
    
#processing logic
    words = lines.select(explode(split(lines.value," ")).alias("word"))
    wordCounts = words.groupBy("word").count()

#writing to the sink
    query = wordCounts.writeStream \
        .format("console") \
        .outputMode("complete") \
        .option("checkpointLocation","checkpointdir1") \
        .start()
    
    query.awaitTermination()

    
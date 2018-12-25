from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext

def main():
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    data = spark.read.text("/sample_fpgrowth.txt")
    print(data.count)


if __name__ == '__main__':
    main()

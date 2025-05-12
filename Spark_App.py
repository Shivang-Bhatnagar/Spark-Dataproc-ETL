# Creating Spark Session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Spark_Project") \
    .enableHiveSupport() \
    .getOrCreate()

# Defining Schema and Reading data from HDFS
schema = StructType([
    StructField("UserId", IntegerType(), True),
    StructField("TransactionId", IntegerType(), True),
    StructField("TransactionTime", StringType(), True),
    StructField("ItemCode", IntegerType(), True),
    StructField("ItemDescription", StringType(), True),
    StructField("NumberOfItemPurchased", IntegerType(), True),
    StructField("CostPerItem", DoubleType(), True),
    StructField("Country", StringType(), True)
])
transaction_df = spark.read.format("csv").option("header", "true").option("inferSchema", "false").schema(schema).load("/user/input_data")
print("Successfull Data Read")

# Cleaning and Tranforming Data
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
transaction_df = transaction_df.withColumn("TransactionTime", to_timestamp("TransactionTime", "EEE MMM dd HH:mm:ss z yyyy"))
transaction_df = transaction_df.withColumn("Year", year(col("TransactionTime"))).withColumn("Month", month(col("TransactionTime")))
transaction_df = transaction_df.withColumn("UserId", col("UserId").cast("int")) \
       .withColumn("TransactionId", col("TransactionId").cast("int")) \
       .withColumn("ItemCode", col("ItemCode").cast("int")) \
       .withColumn("Sales", col("NumberOfItemPurchased").cast("int")) \
       .withColumn("Price", col("CostPerItem").cast("double"))

transaction_df = transaction_df.filter(col("UserId").isNotNull() & col("Price").isNotNull())
print("Data is cleaned and transformed")


# Writing Data into Hive Tabel

spark.sql("""set hive.exec.dynamic.partition.mode=nonstrict""")

spark.sql("""USE spark_db""")

spark.sql("""
    CREATE TABLE IF NOT EXISTS transactional_data (
        UserId INT,
        TransactionId INT,
        TransactionTime TIMESTAMP,
        Sales INT,
        Price DOUBLE,
        Country STRING,
        Month INT
    ) PARTITIONED BY (Year INT)
    STORED AS PARQUET
""")

transaction_df.select('UserId',
              'TransactionId',
              'TransactionTime',
              'Sales',
              'Price',
              'Country',
                'Month',       
              'Year').write.mode("append").insertInto("transactional_data")

print("Data write successfully")

# Stop the Spark Session
spark.stop()


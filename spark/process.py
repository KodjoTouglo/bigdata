from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import col, trim, regexp_replace, to_timestamp

# Configuration Spark
conf = SparkConf() \
    .setAppName("Yelp Reviews Cleaner") \
    .set("spark.driver.memory", "4g") \
    .set("spark.executor.memory", "4g")

# Création de la session Spark
spark = SparkSession.builder \
    .config(conf=conf) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Lecture JSON brut
df = spark.read.json("hdfs://namenode:9000/data/raw/yelp/review.json")

# Nettoyage et typage
df_clean = df.select(
    col("review_id").cast("string"),
    col("user_id").cast("string"),
    col("business_id").cast("string"),
    col("stars").cast("float"),
    regexp_replace(trim(col("text")), "[^\\x00-\\x7F]", "").alias("text"),
    to_timestamp("date").alias("review_date")
)

# Écriture en Parquet compressé (Snappy par défaut)
df_clean.write.mode("overwrite").parquet("hdfs://namenode:9000/data/cleaned_data/yelp/")

print("[+] Données nettoyées et enregistrées.")

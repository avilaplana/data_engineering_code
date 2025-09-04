# 1. What is the total purchase amount for each gender in the dataset? Use the
# data_cleaned_gender dataframe and Group the data by gender and calculate the sum
# of all purchase amounts.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, lit, when
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType

spark = SparkSession.newSession()

schema = StructType([
    StructField("Customer_ID", IntegerType(), True),
    StructField("Customer_Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Gender", StringType(), True),
    StructField("Purchase_Amount", FloatType(), True),
    StructField("Purchase_Date", DateType(), True)
])
# Read data from CSV file into DataFrame
data = spark.read \
    .option("header", "true") \
    .option("inferSchema", "false") \
    .schema(schema) \
    .csv("./sample_data.csv")
# Question: How do you remove duplicate rows based on customer ID in PySpark?
data_unique = data.dropDuplicates()
# Question: How do you handle missing values by replacing them with 0 in PySpark?
data_cleaned_missing = data_unique.select(
    col("Customer_ID"),
    col("Customer_Name"),
    coalesce(col("Age"), lit(0)).alias("Age"),
    col("Gender"),
    coalesce(col("Purchase_Amount"), lit(0.0)).alias("Purchase_Amount"),
    col("Purchase_Date"))
# Question: How do you remove outliers (e.g., age > 100 or purchase amount > 1000) in PySpark

data_cleaned_outliers = data_cleaned_missing.filter(
(col("Age") <= 100) & (col("Purchase_Amount") <= 1000)
)

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male
data_cleaned_gender = data_cleaned_outliers.withColumn(
"Gender_Binary",
when(col("Gender") == "Female", 0).otherwise(1)
)

data_cleaned_gender \
    .groupby(col("Gender")) \
    .agg(col("Purchase_Amount") \
    .alias("total_amount"))
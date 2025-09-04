# 2. What is the average purchase amount for different age groups? Use the data_cleaned
# dataframe and create age group categories (18-30, 31-40, 41-50, 51-60, 61-70) and calcu-
# late the mean purchase amount for each group.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, lit, when, split, mean
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

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name
data_cleaned = data_cleaned_gender.select(
    col("Customer_ID"),
    split(col("Customer_Name"), " ").getItem(0).alias("First_Name"),
    split(col("Customer_Name"), " ").getItem(1).alias("Last_Name"),
    col("Age"),
    col("Gender_Binary"),
    col("Purchase_Amount"),
    col("Purchase_Date")
)
# 18-30, 31-40, 41-50, 51-60, 61-70
data_with_group_age = data_cleaned.withColumn("age_group", \
                        when(col("Age").between(18,30), "18-30")
                        .when(col("Age").between(31,40), "31-40")
                        .when(col("Age").between(41,50), "41-50")
                        .when(col("Age").between(51,60), "51-60")
                        .when(col("Age").between(61,70), "61-70")
                        .otherwise(">70"))

average_purchase_by_age_group = data_with_group_age \
    .groupby(col("age_group")) \
    .agg(mean(col("Purchase_Amount")).alias("Average_Purchase_Amount"))




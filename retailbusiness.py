from calendar import month
import pyspark
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession
customers_df = spark.read.option("delimiter", "\t").csv("hdfs://localhost:9000/retailbusiness/customers-tab-delimited")  # type: ignore

from pyspark.ml.feature import VectorAssembler
input_cols = ["col1", "col2", "col3"]
vectorAssembler = VectorAssembler(inputCols=input_cols, outputCol="features")

from pyspark.sql.functions import col
california_customers = customers_df.filter(col("_c4") == "CA").select("_c1", "_c2")

from pyspark.sql.functions import col, concat, from_unixtime, lit, to_date, year

california_customers = california_customers.withColumn("full_name",concat(california_customers["_c1"],lit(" "), california_customers["_c2"]))

california_customers = california_customers.select("full_name")
california_customers.show()

output_path = "hdfs://localhost:9000/retail/result/scenario1/solution" 
california_customers.write.mode("overwrite").text(output_path)                                       

# ======================task 2.3 ====================================

# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("RetailAnalytics").getOrCreate()

order_schema = StructType([
    StructField("order_number", StringType(), True),
    StructField("order_date", StringType(), True),
   StructField("current_status", StringType(), True)
 ])


order_data = spark.read.parquet("hdfs://localhost:9000/retailbusiness/orders_parquet")

# Show all orders with the order status value "COMPLETE"
complete_orders = order_data.filter(col("order_status") == "COMPLETE")

# Select only the required columns
selected_columns = ["order_number", "order_date"]
# from pyspark.sql.functions import col, from_unixtime
 
complete_orders = order_data.filter(col("order_status") == "COMPLETE") 
selected_columns = ["order_id", "order_date"]

# The "order date" column should be in the "YYYY-MM-DD" format
converted_orders = complete_orders.withColumn("order_date", from_unixtime("order_date"))

# Define the output path
output_path = "hdfs://localhost:9000/retailbusiness/result/scenario2/solution"


# Save the filtered data in JSON format with GZIP compression
converted_orders.write.mode("overwrite").json(output_path, compression="gzip")   


# ====================task2.4 ==================
# from pyspark.sql import SparkSession


customer_data = spark.read.option("delimiter", "\t").csv("hdfs://localhost:9000/retail/customers-tab-delimited")

caguas_customers = customer_data.filter(customer_data["_c3"] == "Caguas")
                                                        
output_path = "hdfs://localhost:9000/retail/result/scenario3/solution"

caguas_customers.write.mode("overwrite").format("orc").option("compression", "snappy").save(output_path)



# ================ task2.5 =====================
# from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Explore Category Records").getOrCreate()


category_data = spark.read.csv("hdfs://localhost:9000/retailbusiness/categories")

output_path = "hdfs://localhost:9000/retailbusiness/result/scenario4/solution"
category_data.write.mode("overwrite").option("compression", "lz4").csv(output_path)


# ============== Task 2.6 =================


# from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Explore Product Records").getOrCreate()

# Explore all product records that are saved in the “products_avro” database
product_data = spark.read.format("avro").load("hdfs://localhost:9000/retailbusiness/products_avro")

# Only products with a price of more than 1000.0 should be included in the output
# Remove data from the table if the product price is lesser than 1000.0
filtered_products = product_data.filter(product_data["product_price"] > 1000.0)

# Save the data in the result/scenario5/solution directory on HDFS
output_path = "hdfs://localhost:9000/retailbusiness/result/scenario5/solution"

# Use snappy compression to compress the output
filtered_products.write.mode("overwrite").format("parquet").option("compression", "snappy").save(output_path)

spark.stop()

# ================task 2.7======================
# from pyspark.sql import SparkSession 
# from pyspark.sql.functions import col 

spark = SparkSession.builder.appName("Explore Product Records").getOrCreate()


# Explore the “products_avro” stored in product records
product_data = spark.read.format("avro").load("hdfs://localhost:9000/retailbusiness/products_avro")

#Only products with a price of more than 1000.0 should be in the output
#The pattern "Treadmill" appears in the product name

filtered_products = product_data.filter((col("product_price") > 1000.0) & (col("product_name").like("%Treadmill%")))

# Save the data in the result/scenario6/solution directory on HDFS
output_path = "hdfs://localhost:9000/retailbusiness/result/scenario6/solution"
 
# Save the output files in parquet format
# Use GZIP compression to compress the output
filtered_products.write.mode("overwrite").format("parquet").option("compression", "gzip").save(output_path)                                              

# =======================task 2.8 =========================

# from pyspark.sql.functions import col, year, month, from_unixtime, to_date

spark = SparkSession.builder.appName("Explore Order Records").getOrCreate()

order_data = spark.read.parquet("hdfs://localhost:9000/retailbusiness/orders_parquet")


# Order date should be in the YYY-MM-DD format
order_data = order_data.withColumn("order_date", to_date(from_unixtime(col("order_date"))))

#Output all PENDING orders in July 2013
filtered_orders = order_data.filter((col("order_status") == "PENDING") & (year("order_date") == 2013) & (month("order_date") == 7))

# Only entries with the order status value of "PENDING" should be included in the result
selected_columns = ["order_date", "order_status"]
filtered_orders = filtered_orders.select(*selected_columns)


#Save the data in the result/scenario7/solution directory on HDFS.
output_path = "hdfs://localhost:9000/retailbusiness/result/scenario7/solution"

# Use snappy compression to compress the output, which should just contain the order date and order status
filtered_orders.write.mode("overwrite").option("compression", "snappy").json(output_path)


# Stop the SparkSession
spark.stop()


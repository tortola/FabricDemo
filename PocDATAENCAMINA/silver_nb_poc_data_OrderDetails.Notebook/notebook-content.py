# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8b97c59f-02a7-436c-9028-4cc1cb400d9b",
# META       "default_lakehouse_name": "Silver_lh_poc_data",
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.sql("SELECT OrderID \
                ,ProductID \
                ,UnitPrice \
                ,Quantity \
                ,Discount \
                ,cast(UnitPrice*Quantity as DECIMAL(18,2)) as Total \
                ,cast((1.00 - Discount)*UnitPrice*Quantity as DECIMAL(18,2)) as TotalWithDiscount \
            FROM Bronze_lh_poc_data.Order_Details")

df.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/Order_Details")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

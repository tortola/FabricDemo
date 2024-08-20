# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "59295084-1e7d-4721-93a9-383be40ff972",
# META       "default_lakehouse_name": "Gold_lh_poc_data",
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.sql("SELECT SupplierID \
                    ,CompanyName AS SupplierName \
                    ,City AS SupplierCity \
                    ,Region AS SupplierRegion \
                    ,Country AS SupplierCountry \
                FROM Silver_lh_poc_data.Suppliers")

df.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/dimSuppliers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

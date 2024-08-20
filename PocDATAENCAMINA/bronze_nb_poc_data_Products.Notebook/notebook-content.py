# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "02a1339a-a0f5-4c3c-9f88-060646d0a357",
# META       "default_lakehouse_name": "Bronze_lh_poc_data",
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.sql("SELECT * FROM Raw_lh_poc_data.Products")

df.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/Products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

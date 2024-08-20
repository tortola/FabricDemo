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
df = spark.sql("SELECT EmployeeID \
                    ,FirstName + ' ' + LastName AS EmployeeName \
                    ,Title AS EmployeeTitle \
                    ,City AS EmployeeCity \
                    ,Region AS EmployeeRegion \
                    ,Country AS EmployeeCountry \
                FROM Silver_lh_poc_data.Employees")

df.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/dimEmployees")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

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
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee",
# META       "known_lakehouses": [
# META         {
# META           "id": "59295084-1e7d-4721-93a9-383be40ff972"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.sql("SELECT O.OrderID \
                ,O.OrderDate \
                ,O.CustomerID \
                ,O.EmployeeID \
                ,O.ShipName \
                ,O.ShipCity \
                ,O.ShipRegion \
                ,O.ShipCountry \
                ,D.ProductID \
                ,D.UnitPrice \
                ,D.Quantity \
                ,D.Discount \
                ,D.Total \
                ,D.TotalWithDiscount \
            FROM Silver_lh_poc_data.Orders O \
                INNER JOIN Silver_lh_poc_data.Order_Details D \
                    ON O.OrderID = D.OrderID")

df.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/factOrders")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

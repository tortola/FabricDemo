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
# META       "known_lakehouses": []
# META     }
# META   }
# META }

# CELL ********************

import pandas as pd

spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

def create_date_dimension(start='2000-01-01', end='2050-12-31'):
    df = pd.DataFrame({"Date": pd.date_range(start, end)})
    df["Day"] = df.Date.dt.day
    df["Month"] = df.Date.dt.month
    df["Quarter"] = df.Date.dt.quarter
    df["Year"] = df.Date.dt.year
    df["DayName"] = df.Date.dt.day_name()
    df["MonthName"] = df.Date.dt.month_name()

    return spark.createDataFrame(df)

date_dimension = create_date_dimension()

date_dimension.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/dimDate")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

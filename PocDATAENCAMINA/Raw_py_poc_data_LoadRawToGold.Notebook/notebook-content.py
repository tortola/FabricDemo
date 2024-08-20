# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6e603f41-5502-4d2a-86ff-5f806b73a423",
# META       "default_lakehouse_name": "Raw_lh_poc_data",
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee",
# META       "known_lakehouses": [
# META         {
# META           "id": "6e603f41-5502-4d2a-86ff-5f806b73a423"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# 
# #### Run the cell below to install the required packages for Copilot


# CELL ********************


#Run this cell to install the required packages for Copilot
%pip install https://aka.ms/chat_magics-0.0.0-py3-none-any.whl
%load_ext chat_magics


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

source = "abfss://WS_POC_DATA_ENCAMINA@onelake.dfs.fabric.microsoft.com/Raw_lh_poc_data.Lakehouse/Tables/Categories/"
dest = "abfss://WS_POC_DATA_ENCAMINA@onelake.dfs.fabric.microsoft.com/Gold_lh_poc_data.Lakehouse/Tables/Categories"
df = spark.read.format("delta").load(source)
df.write.mode("overwrite").format("delta").save(dest)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

source = "abfss://WS_POC_DATA_ENCAMINA@onelake.dfs.fabric.microsoft.com/Raw_lh_poc_data.Lakehouse/Tables/"
dest = "abfss://WS_POC_DATA_ENCAMINA@onelake.dfs.fabric.microsoft.com/Gold_lh_poc_data.Lakehouse/Tables/"
files=["Categories","DimTiempo","DimTiempo"]
for x in files:
    tablax = source + x
    destx= dest+ x
    display(tablax)
    display(destx)
    df = spark.read.format("delta").load(destx)
    df.write.mode("overwrite").format("delta").save(destx)
    display("terminado")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

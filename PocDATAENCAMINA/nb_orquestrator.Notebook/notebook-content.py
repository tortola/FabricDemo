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
# META       "default_lakehouse_workspace_id": "5370d354-d5bc-43fe-96f9-946edbf670ee",
# META       "known_lakehouses": []
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%configure
# MAGIC 
# MAGIC {
# MAGIC     "defaultLakehouse": { 
# MAGIC         "name": {
# MAGIC                 "parameterName": "DefaultLakehouseName",
# MAGIC                 "defaultValue": "Bronze_lh_poc_data"
# MAGIC             }
# MAGIC     }
# MAGIC }

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

path_config_file = "Files/config_files/bronze_config_file.csv"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import SparkSession

# Inicializar Spark Session
spark = SparkSession.builder.appName("NotebookOrchestration").getOrCreate()

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("sep", ";") \
    .load(path_config_file)

names_list = [row['NotebookName'].strip() for row in df.select('NotebookName').collect()]

# Crear las actividades para el DAG basándonos en los nombres de notebooks obtenidos
activities = [
    {
        "name": name, 
        "path": name, 
        "timeoutPerCellInSeconds": 120,
    }
    for name in names_list
]

# Definir la estructura del DAG
DAG = {
    "activities": activities,
    "timeoutInSeconds": 3600, 
    "concurrency": 5
}

# Ejecutar los notebooks en paralelo y visualizar el DAG
mssparkutils.notebook.runMultiple(DAG, {"displayDAGViaGraphviz": True, "DAGLayout": "spectral", "DAGSize": 11})

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

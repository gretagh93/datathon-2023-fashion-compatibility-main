from pandasql import sqldf
import pandas as pd
# import numpy as np 

# Read CSV files 
product_data = pd.read_csv("/Python/datathon/dataset/product_data.csv") 
outfit_data = pd.read_csv("/Python/datathon/dataset/outfit_data.csv")

aux = input("")

print(sqldf(f'''SELECT o.cod_outfit, pm.des_color_specification_esp, pm.des_agrup_color_eng, pm.des_fabric, pm.des_product_category, pm.des_product_aggregated_family, pm.des_product_type
            FROM product_data pm natural inner join outfit_data o
            WHERE  {aux} == o.cod_outfit'''))

print(sqldf('''SELECT pm.cod_modelo_color
                FROM product_data pm
                WHERE pm.des_agrup_color_eng == "GREY" and pm.des_product_type == "Troussers" LIMIT 3'''))
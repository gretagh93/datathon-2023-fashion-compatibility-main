from pandasql import sqldf
import pandas as pd
import random
# import numpy as np 
# "57036014-30","30","MARRON","BROWN","BROWN","Adult","HOME","P-PLANA","Home","Decor","Deco Textiles","Plaid","datathon/images/2023_57036014_30.jpg"
# Read CSV files 
product_data = pd.read_csv("/Users/l1rel/OneDrive/Escritorio/Programacion/Python/datathon/dataset/product_data.csv") 
outfit_data = pd.read_csv("/Users/l1rel/OneDrive/Escritorio/Programacion/Python/datathon/dataset/outfit_data.csv") 

cod_modelo_color_aux = input("")
cod_color_code_aux = input("")
des_color_specification_esp_aux = input("")
des_agrup_color_eng_aux = input("")
des_sex_aux = input("")
des_age_aux = input("")
des_line_aux = input("")
des_fabric_aux = input("")
des_product_category_aux = input("")
des_product_aggregated_family_aux = input("")
des_product_family_aux = input("")
des_product_type_aux = input("")
des_filename_aux = input("")

if (des_product_category_aux == "Tops"):
    print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
            FROM product_data pm
            WHERE pm.cod_modelo_color <> {cod_modelo_color_aux} and pm.des_agrup_color_eng == {des_agrup_color_eng_aux}
                  and (pm.des_sex == {des_sex_aux} and pm.des_age == {des_age_aux}'''))
elif (des_product_category_aux == "Bottoms"):
    print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
            FROM product_data pm
            WHERE pm.cod_modelo_color <> {cod_modelo_color_aux} and pm.des_agrup_color_eng == {des_agrup_color_eng_aux}
                  and (pm.des_sex == {des_sex_aux} and pm.des_age == {des_age_aux}'''))
elif (des_product_category_aux == "Home"):
    if (des_product_aggregated_family_aux == "Decor"):
        if (des_agrup_color_eng_aux == "Brown"):
            if (des_product_family_aux == "Deco Textiles"):
                print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
                    FROM product_data pm
                    WHERE pm.cod_modelo_color == "Home" and (pm.des_agrup_color_eng == "WHITE" or pm.des_agrup_color_eng == "GREY")
                          and pm.des_age == {des_age_aux} and des_product_family == "Deco Accessories"'''))
            elif (des_product_family_aux == "Deco Accessories"):
                print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
                    FROM product_data pm
                    WHERE pm.cod_modelo_color == "Home" and (pm.des_agrup_color_eng == "WHITE" or pm.des_agrup_color_eng == "GREY")
                          and pm.des_age == {des_age_aux} and des_product_family == "Deco Textiles"'''))
        else:
            if (des_product_family_aux == "Deco Textiles"):
                print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
                    FROM product_data pm
                    WHERE pm.cod_modelo_color == "Home" and pm.des_agrup_color_eng == "BROWN"
                          and pm.des_age == {des_age_aux} and des_product_family == "Deco Accessories"'''))
            elif (des_product_family_aux == "Deco Accessories"):
                print(sqldf(f'''SELECT pm.cod_modelo_color, pm.des_filename  
                    FROM product_data pm
                    WHERE pm.cod_modelo_color == "Home" and pm.des_agrup_color_eng == "BROWN"
                          and pm.des_age == {des_age_aux} and des_product_family == "Deco Textiles"'''))
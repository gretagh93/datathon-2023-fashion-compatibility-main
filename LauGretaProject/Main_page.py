import streamlit as st
from pandasql import sqldf
import pandas as pd
from PIL import Image
from random import *

st.set_page_config (
    page_title = "Main page"
)
st.sidebar.markdown("# Main page")

# Read CSV files 
product_data = pd.read_csv("/Python/datathon/dataset/product_data.csv") 
outfit_data = pd.read_csv("/Python/datathon/dataset/outfit_data.csv") 

st.header("MANGO")

st.title(" Fashion Compatibility Challenge ")
st.write("(Any question with a :red[*] has to be answered before continuing.)")
st.markdown("""---""")

text_in_MC = st.text_input("Which is the code of your product based on its model and color? :red[*]", key="cod_modelo_color_aux")
text_in_S = st.radio(
                "To which gender does the product belong? :red[*]",
                ["Female", "Male", "Unisex"])
text_in_A = st.radio(
                "To which age is these product directed too :red[*]",
                ["Adult", "Kids"])
text_in_F = st.text_input("Which is the fabric of the product? :red[*]", key="des_fabric_aux")
text_in_C = st.text_input("To which category does it belongs? :red[*]", key="des_product_category_aux")
text_in_CAF = st.text_input("To which aggregated family does it belongs? :red[*]", key="des_product_aggregated_family_aux")
text_in_CF = st.text_input("To which family does it belongs? :red[*]", key="des_product_family_aux")
text_in_T = st.text_input("Which is it's type? :red[*]", key="des_product_type_aux")
text_in_URL = st.text_input("And, finally, which is its filename? :red[*]", key="des_filename_aux")

while (not text_in_MC or not text_in_S or not text_in_S or not text_in_A or not text_in_F or not text_in_C or not text_in_CAF or not text_in_CF or not text_in_T or not text_in_URL):
    st.stop()
    
text_in_L = "vacio"
if (text_in_C == "Home"): text_in_L = "HOME"
elif (text_in_A == "Kids"): text_in_L = "KIDS"
elif (text_in_S == "Female"): text_in_L = "SHE"
else: text_in_L = "HE"

text_in_CC = text_in_MC[9:11]

while (not text_in_CC):
    st.stop()
text_in_CS = product_data.loc[product_data["cod_modelo_color"] == text_in_MC, ["des_color_specification_esp"]] 
text_in_GE = product_data.loc[product_data["cod_modelo_color"] == text_in_MC, ["des_agrup_color_eng"]] 

st.image(Image.open(text_in_URL))

st.markdown("""---""")
st.write("If this is your outfit and you wanna continue, please, do so.")
st.write("If not, you can change you answers above.")

st.button("Hi")
st.markdown("""---""")

if (text_in_CF == "Dresses"):
    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "BROWN" and pm.des_product_family == "Footwear" LIMIT 1'''))
    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ORO" and pm.des_product_type == "Necklace" LIMIT 1'''))
    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ARENA" and pm.des_product_family == "Bags" LIMIT 1'''))
elif (text_in_CF == "Tops"):
    num = random.randint(1, 2)

    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "BROWN" and pm.des_product_family == "Footwear" LIMIT 1'''))
    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "BROWN" and pm.des_product_category == "Bottoms" LIMIT 1'''))
    if (num == 1): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ORO" and pm.des_product_type == "Necklace" LIMIT 1'''))
    if (num == 1): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ARENA" and pm.des_product_family == "Bags" LIMIT 1'''))
    if (num == 2): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ORO" and pm.des_product_family == "Ring" LIMIT 1'''))
        
elif (text_in_CF == "Bottoms"):
    num = random.randint(1, 2)

    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "BROWN" and pm.des_product_family == "Footwear" LIMIT 1'''))
    st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "BROWN" and pm.des_product_category == "Tops" LIMIT 1'''))
    if (num == 1): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ORO" and pm.des_product_type == "Necklace" LIMIT 1'''))
    if (num == 1): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ARENA" and pm.des_product_family == "Bags" LIMIT 1'''))
    if (num == 2): st.write(sqldf('''SELECT *
                      FROM product_data pm
                      WHERE pm.des_agrup_color_eng == "WHITE" and pm.des_color_specification_esp == "ORO" and pm.des_product_family == "Ring" LIMIT 1'''))
    
    
import streamlit as st
from pandasql import sqldf
import pandas as pd
from PIL import Image

st.set_page_config (
    page_title = "Outfit page"
)
st.sidebar.markdown("# Outfit page")

# Read CSV files 
product_data = pd.read_csv("/Python/datathon/dataset/product_data.csv") 
outfit_data = pd.read_csv("/Python/datathon/dataset/outfit_data.csv") 

st.header("MANGO")

st.title(" Outfits examples ")
st.markdown("""---""")

st.write("- 1º outfit:")
st.write("-> Dresses")
st.write("      53030840-50, 50, CELESTE, BLUE, Female, Adult, SHE, P-PLANA, Dresses, jumpsuits and Complete set, Dresses and jumpsuits, Dresses, Dress, datathon/images/2019_53030840_50.jpg")
st.image(Image.open("datathon/images/2019_53030840_50.jpg"))
st.write("      37010684-CU, CU, CUERO, BROWN, Female, Adult, SHE, C-COMPLEMENTOS, Accesories, Swim and Intimate, Accessories, Footwear, Sandals, datathon/images/2022_37010684_CU.jpg")
st.image(Image.open("datathon/images/2022_37010684_CU.jpg"))
st.markdown("""---""")

st.write("- 2º outfit:")
st.write("-> Top - Skirts")
st.write("      53085772-02, 02, OFFWHITE, WHITE, Female, Adult, SHE, P-PLANA, Tops, Tops, Tops, Top, datathon/images/2019_53085772_02.jpg")
st.image(Image.open("datathon/images/2019_53085772_02.jpg"))
st.write("      53080547-TO, TO, TEJANO OSCURO, BLUE, Female, Adult, SHE, J-JEANS, Bottoms, Skirts and shorts, Skirts, Skirt, datathon/images/2019_53080547_TO.jpg")
st.image(Image.open("datathon/images/2019_53080547_TO.jpg"))
st.write("57091502-OR, OR, ORO, WHITE, Female, Adult, SHE, C-COMPLEMENTOS, Accesories, Swim and Intimate, Accessories, Jewellery, Earrings, datathon/images/2023_57091502_OR.jpg")
st.image(Image.open("datathon/images/2023_57091502_OR.jpg"))
st.write("      37010684-CU, CU, CUERO, BROWN, Female, Adult, SHE, C-COMPLEMENTOS, Accesories, Swim and Intimate, Accessories, Footwear, Sandals, datathon/images/2022_37010684_CU.jpg")
st.image(Image.open("datathon/images/2022_37010684_CU.jpg"))
st.write("      47097833-OR, OR, ORO, WHITE, Female, Adult, SHE, C-COMPLEMENTOS, Accesories, Swim and Intimate, Accessories, Jewellery, Ring, datathon/images/2023_47097833_OR.jpg")
st.image(Image.open("datathon/images/2023_47097833_OR.jpg"))
st.markdown("""---""")

st.write("- 3º outfit:")
st.write("-> Top - Trousers")
st.write("      53085772-02, 02, OFFWHITE, WHITE, Female, Adult, SHE, P-PLANA, Tops, Tops, Tops, Top, datathon/images/2019_53085772_02.jpg")
st.image(Image.open("datathon/images/2019_53085772_02.jpg"))
st.write("      53041096-OR, OR, ORO, WHITE, Female, Adult, SHE, C-COMPLEMENTOS, Accesories, Swim and Intimate, Accessories, Jewellery, Necklace, datathon/images/2019_53041096_OR.jpg")
st.image(Image.open("datathon/images/2019_53041096_OR.jpg"))
st.write("      53000586-TO, TO, TEJANO OSCURO, BLUE, Female, Adult, SHE, J-JEANS, Bottoms, Jeans, Jeans, Jeans, datathon/images/2019_53000586_TO.jpg")
st.image(Image.open("datathon/images/2019_53000586_TO.jpg"))
st.markdown("""---""")

st.write("- 4º outfit:")
st.write("Home -> Deco Textil")
st.write("      57026311-08, 08, BEIGE, WHITE, Unisex, Adult, HOME, P-PLANA, Home, Decor, Deco Textiles, Plaid, datathon/images/2023_57026311_08.jpg")
st.image(Image.open("datathon/images/2023_57026311_08.jpg"))
st.write("      47042516-08, 08, BEIGE, WHITE, Unisex, Adult, HOME, C-COMPLEMENTOS, Home, Decor, Deco Accessories, Basket, datathon/images/2023_47042516_08.jpg")
st.image(Image.open("datathon/images/2023_47042516_08.jpg"))
st.write("      47117159-95, 95, ANTRACITA, GREY, Unisex, Adult, HOME, P-PLANA, Home, Bedroom, Bedding, Duvet Covers, datathon/images/2023_47117159_95.jpg")
st.image(Image.open("datathon/images/2023_47117159_95.jpg"))
st.markdown("""---""")

st.write("- 5º outfit:")
st.write("Home -> Deco Accessories")
st.write("      57074776-30, 30, MARRON, BROWN, Unisex, Adult, HOME, C-COMPLEMENTOS, Home, Decor, Deco Accessories, Basket, datathon/images/2023_57074776_30.jpg")
st.image(Image.open("datathon/images/2023_57074776_30.jpg"))
st.write("      57071179-08, 08, BEIGE, WHITE, Unisex, Adult, HOME, P-PLANA, Home, Decor, Deco Textiles, Cushion Case, datathon/images/2023_57071179_08.jpg")
st.image(Image.open("datathon/images/2023_57071179_08.jpg"))
st.markdown("""---""")
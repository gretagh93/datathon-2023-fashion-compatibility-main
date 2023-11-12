from pandasql import sqldf
import pandas as pd
import numpy as np
import tensorflow as tf

# Read CSV files
product_data = pd.read_csv("datathon/dataset/product_data.csv")
outfit_data = pd.read_csv("datathon/dataset/outfit_data.csv")

# PRODUCT_DATA

# Features of each column
cols_product_data = list(product_data.columns)
dict_list_features={p:(product_data[p].unique().tolist()) for p in product_data}

# OUTFIT_DATA

# List outfit code
list_cod_outfit = list(outfit_data["cod_outfit"])

# Dictionary of outfit code and products code
df_outfit_products_codes = (outfit_data.groupby("cod_outfit")["cod_modelo_color"].apply(list))
dic_outfit_products_codes = (df_outfit_products_codes.to_dict())

# List of products code of an outfit
def outfit_codes(outfit_code, dic_oc=dic_outfit_products_codes):
  return dic_oc[outfit_code]
# print(outfit_codes(2))

# ANSALYSE PRODUCT_DATA AND OUTFIT_DATA

# Dataset of a product features
def product(code, df=product_data):
  new_df = df.loc[df["cod_modelo_color"] == code]
  return new_df
# print(product("53103803-OR"))

# Dataset list of a product features of an outfit
def product_list(list_code):
  l=[product(c) for c in list_code]
  return l
# print(product_list(outfit_codes(2)))

# Dictionary of features of the prodocts that are in an outfit
def summarize_data(outfit_code, k=cols_product_data):
  list_df = product_list(outfit_codes(outfit_code))
  d={}
  for df in list_df:
    for c in k:
      if c not in d:
        d[c] = []
      else:
        d[c].append(df[c].item())
  return(d)
dic_outfit_products_data = summarize_data(2)
# print(dic_outfit_products_data)

# des_prod = dic_outfit_products_data["des_product_aggregated_family"]
# Create a list of lists
list_outfit_code = dic_outfit_products_codes.keys()
list_specific_values = []
for o in list_outfit_code:
  l = (summarize_data(o))["des_product_aggregated_family"]
  if "Tops" in l:
    list_specific_values.append(l)
# print(list_specific_values)

# Join lists to a dictionary
dict_combinations = {}
for element in list_specific_values:
  for e in element:
    if e in dict_combinations.keys():
      dict_combinations[e] += 1
    else:
      dict_combinations[e] = 1
print(dict_combinations)



#  for e in element:
#    if e not in all_in_one:
 #     all_in_one.append(e)
#print(all_in_one)

"""
for c in list_cod_outfit:
  convinations = summarize_data(c)["des_product_aggregated_family"]
  dict_convinations = {}
  for convi in convinations:
    if convi in dict_convinations.keys():
      dict_convinations[convi] += 1
    else:
      dict_convinations[convi] = 1
  print(dict_convinations)


# List with the
def value_subset(code, col, df=product_data):
  new_df = df.loc[df["cod_modelo_color"] == code, col].item()
  return new_df

def characteristichs_outfits(col, outfit):
  list_code = outfit_codes(outfit)
  l=[value_subset(code, col) for code in list_code]
  return l
print(characteristichs_outfits("cod_color_code", 2))


"""


# sqldf(f'''SELECT des_agrup_color_eng, des_fabric, des_product_category, des_product_aggregated_family, des_product_family, des_product_type
#         FROM product_data pm natural inner join outfit_data o
#         WHERE {list_id[i]} == o.cod_outfit and des_product_category == "Home"''')



# train, val, test = np.split(product_data.sample(frac=1), [int(0.8*len(product_data)), int(0.9*len(product_data))])
# print(len(train), 'training examples')
# print(len(val), 'validation examples')
# print(len(test), 'test examples')

# DataFrame to TensorFlow DataSet
# def df_to_tfds(dataframe, shuffle=True, batch_size=32):
#   df = dataframe.copy()
#   labels = list(df.columns)
  # df = {key: value[:,tf.newaxis] for key, value in dataframe.items()}
#   ds = tf.data.Dataset.from_tensor_slices((dict(df), labels))
#   return ds

# print(df_to_tfds(train))

# print(product_data.columns)
# print(outfit_data.columns)

# while (i > 0):
#     i -= 1 
#     hola = sqldf(f'''SELECT des_agrup_color_eng, des_fabric, des_product_category, des_product_aggregated_family, des_product_family, des_product_type
#         FROM product_data pm natural inner join outfit_data o
#         WHERE {list_id[i]} == o.cod_outfit and des_product_category == "Home"''')
# print(hola)
# print(type(hola))
    #list.append(hola) 
# print(list)
# list.to_csv("data_export.csv", index=False)

#--------------------------------------------------------------------------#


# product_data["product_data"].value_counts()

# dataset = tf.data.Dataset.from_tensor_slices((df_train.values))
# print(dataset)
#print(df_train.pop('des_product_category'))

# diccionario = dict(zip(outfit_data["cod_outfit"], outfit_data["cod_modelo_color"]))
# print(diccionario)
# print(product_data.head())
# outwear = product_data.loc[product_data["des_product_category"]=="Outerwear", ["des_filename", "des_product_family"]]
# print(outwear)
# print(sqldf('''SELECT des_product_category, des_filename 
# FROM product_data LIMIT 5'''))
# print(product_data.columns)
# print(list(product_data["des_product_category"].unique()))
# def ejemplo(x,y):
#     print(sqldf(f'''SELECT {x}, {y} FROM product_data LIMIT 5'''), locals())
# x="des_product_category"
# y="des_filename"
# ejemplo(x, y)


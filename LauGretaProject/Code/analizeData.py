from pandasql import sqldf
import pandas as pd
import numpy as np
import tensorflow as tf

# Read CSV files
product_data = pd.read_csv("datathon/dataset/product_data.csv")
outfit_data = pd.read_csv("datathon/dataset/outfit_data.csv")

list_cod_outfit = list(outfit_data["cod_outfit"])

df_outfit_products_codes = (outfit_data.groupby("cod_outfit")["cod_modelo_color"].apply(list))
dic_outfit_products_codes = (df_outfit_products_codes.to_dict())
def outfit_codes(outfit_code, dic_oc=dic_outfit_products_codes):
  return dic_oc[outfit_code]
# print(outfit_codes(2))

def product(code, df=product_data):
  new_df = df.loc[df["cod_modelo_color"] == code]
  return new_df
# print(product("53103803-OR", "des_fabric"))

def product_list(list_code):
  l=[product(c) for c in list_code]
  return l
# print(product_list(outfit_codes(2)))

cols = list(product_data.columns)
def summarize_data(outfit_code, k=cols):
  list_df = product_list(outfit_codes(outfit_code))
  print(list_df)
  d={}
  for df in list_df:
    for c in k:
      if c not in d:
        d[c] = []
      else:
        d[c].append(df[c].item())
  print(d)
summarize_data(2)





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


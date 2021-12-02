import pandas as pd
import plotly.express as px

df = pd.read_csv("globalterrorismdb_0718dist.csv", engine='python', encoding = "ISO-8859-1")



df_tree = df.copy()

get_country_attack = lambda row: 1
df_tree = df_tree[df_tree['attacktype1_txt']!='Unknown']

dict_region = {y:3*(x) for x,y in enumerate(df['region_txt'].value_counts().index)}

df_tree['amount'] = df_tree.apply(get_country_attack, axis=1)

df_tree = df_tree.groupby(['region_txt', 'country_txt', 'attacktype1_txt']).sum()

df_tree['region_txt'] = list(map(lambda x: x[0], df_tree.index))
df_tree['country_txt'] = list(map(lambda x: x[1], df_tree.index))
df_tree['attacktype1_txt'] = list(map(lambda x: x[2], df_tree.index))




fig = px.treemap(df_tree,
                path=[px.Constant("World"), 'region_txt', 'country_txt', 'attacktype1_txt'],
                branchvalues='total',
                values='amount')
                
fig.update_traces(root_color="lightgrey")
fig.update_coloraxes(showscale=False)
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.show()
fig.write_html("index.html")
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv("transformed_data.csv")
data2=pd.read_csv("raw_data.csv")
print(data)

print(data.head())
print(data2.head())

print(data["COUNTRY"].value_counts())
print(data["COUNTRY"].value_counts().mode())
# aggregating the data
code=data["CODE"].unique().tolist()
country=data["COUNTRY"].unique().tolist()
hdi=[]
tc=[]
td=[]
sti=[]
population=data["POP"].unique().tolist()
gdp=[]

for i in country:
    hdi.append((data.loc[data["COUNTRY"]==i,"HDI"]).sum()/294)
    tc.append((data2.loc[data2["location"]==i,"total_cases"].sum()))
    td.append((data2.loc[data2["location"]==i,"total_deaths"].sum()))
    sti.append((data.loc[data["COUNTRY"]==i,"STI"].sum()/294))
    population.append((data2.loc[data2["location"]==i,"population"].sum()/294))
    aggregated_data=append=pd.DataFrame(list(zip(code,country,hdi,tc,td,sti,population)),columns=["Country Code","Country","HDI","Total Cases","Total Deaths","Stringency Index","Population"])
    print(aggregated_data.head())

#sorting Data According to Total cases
data=aggregated_data.sort_values(by=["Total Cases"],ascending=False)
print(data.head())

#Top 10 Countries with the highest Covid cases
data=data.head(10)
print(data)

# analyzing the spread of Covid 19
figure=px.bar(data,y='Total Cases',x="Country",title="Countries with Highest Covid cases ")
figure.show()

figure=px.bar(data,y="Total Deaths",x="Country",title="Countries with Highest Deaths")
figure.show()
#comparing the total deaths and number of cases
fig=go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Cases"],
    name='Total Cases',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Deaths"],
    name='Total Deaths',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()
# Percentage of Total Cases and Deaths
cases = data["Total Cases"].sum()
deceased = data["Total Deaths"].sum()

labels = ["Total Cases", "Total Deaths"]
values = [cases, deceased]

fig = px.pie(data, values=values, names=labels,
             title='Percentage of Total Cases and Deaths', hole=0.5)
fig.show()
#calculating the death rate according to Total cases
death_rate = (data["Total Deaths"].sum() / data["Total Cases"].sum()) * 100
print("Death Rate = ", death_rate)

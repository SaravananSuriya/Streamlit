import streamlit as st
import plotly.express as px
import pandas as pd

a=['saravanan','mohan','manjunath','dinesh','kamal','babu']
b=[121,43,5,3,22,55]

# pie chart
pie = px.pie(names=a,values=b,color=a)
st.plotly_chart(pie,use_container_width=True)

# line chart
# line = px.line(x=a,y=b,color=a,orientation='v')
line = px.line(x=a,y=b,orientation='h')
st.plotly_chart(line)

# bar chart
# bar = px.bar(x=a,y=b,color=a,orientation='v')
bar = px.bar(x=b,y=a,color=a,orientation='h',barmode='relative') # barmode = ['stack', 'group', 'overlay', 'relative']
st.plotly_chart(bar)

# sunburst chart
df = pd.DataFrame({
'name':['saravanan','mohan','manjunath','dinesh','kamal','babu'],
'dob':[2001,1999,1993,1995,1800,2023],
'power':[450,490,460,450,230,300],
'place':['rkpet','chennai','iyyampet','mysore','rkpet','pudur']
})
sunburst = px.sunburst(df,path=['name','dob','power','place'],values='power')
st.plotly_chart(sunburst)

# area chart
area = px.area(x=a,y=b)
st.plotly_chart(area)

# box plot
a=['saravanan','mohan','manjunath','dinesh','kamal','babu','saravanan','manjunath','dinesh','saravanan','kamal','saravanan']
b=[121,43,5,3,22,55,2,434,54,22,542,21]
box = px.box(x=a,y=b)
st.plotly_chart(box)

# funnel chart
a=['saravanan','mohan','manjunath','dinesh','kamal','babu','saravanan','manjunath','dinesh','saravanan','kamal','saravanan']
b=[121,43,5,3,22,55,2,434,54,22,542,21]
funnel = px.funnel_area(names=a,values=b)
st.plotly_chart(funnel)

# scatter chart
scatter = px.scatter(x=a,y=b,color=a,size=b)
st.plotly_chart(scatter)

# scatter geo map
latitude = ['11.618170591192758','13.09194432071248' ] 
longitude = ['79.06308680906575','80.27159737387089']
num = [324424,6575677]
state = ['tamil nadu','chennai']
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='natural earth')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='conic equal area')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='conic conformal')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='equirectangular')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='mercator')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='orthographic')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='kavrayskiy7')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='mollweide')
# scatter_geo = px.scatter_geo(lat=la,lon=lo,size=num,projection='winkel tripel')
scatter_geo = px.scatter_geo(lat=latitude,lon=longitude,size=num,projection='aitoff',opacity=0.5,hover_name=state,color=state,scope='asia') # opacity mentions a scatter brightnes
st.plotly_chart(scatter_geo)

# scatter mapbox
fig = px.scatter_mapbox(lat=latitude,lon=longitude,zoom=10,color=state,width=1100,height=600,color_continuous_scale='jet',size = state,size_max=50,hover_name=state,title ='Scatter MapBox')
fig.update_layout(mapbox_style='carto-positron') # mapbox_style = [carto-positron,open-street-map,carto-darkmatter]
fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
fig.update_geos(fitbounds="locations")
st.plotly_chart(fig)

# histogram chart
hist = px.histogram(x=a,y=b,color=a)
st.plotly_chart(hist)

# map
st.map(data=None, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)

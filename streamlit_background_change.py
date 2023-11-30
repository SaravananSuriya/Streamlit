import streamlit as st
import base64

# 1. Here is the two code for changing background color using images in strteamlit app. but it doesn't work for local images

# code 1
page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
}
[data-testid = "stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True) 

# code 2
page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/32/Mc8kW4x9Q3aRR3RkP5Im_IMG_4417.jpg?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTQ5MzN8&ixlib=rb-4.0.3");
    background-size: cover;
}
[data-testid = "stHeader"] {
    background-color: rgba(0,0,0,0);
}
[data-testid = "stToolbar"] {

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("it is summer")

# This are the few sample unsplash images link

https://images.unsplash.com/photo-1606787366850-de6330128bfc?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTIyOTN8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1613592237010-a29414f72d61?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTI3OTF8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1546818920-cefa8f7b4011?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTMxMDR8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTM0Njh8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1533139143976-30918502365b?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTM5NDV8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1526282817947-54d7a0d9928f?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTQzNzJ8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1508195578732-2d3d3eacf15f?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTQ1OTh8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTQ3Nzl8&ixlib=rb-4.0.3
https://images.unsplash.com/32/Mc8kW4x9Q3aRR3RkP5Im_IMG_4417.jpg?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTQ5MzN8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1695073444254-032b346a3084?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTUzMjR8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1541723011216-c57eaed19919?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTU0Mzd8&ixlib=rb-4.0.3
https://images.unsplash.com/photo-1586788224331-947f68671cf1?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTU1ODV8&ixlib=rb-4.0.3  - plain blue background
https://images.unsplash.com/photo-1556690171-9f6645f4455e?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTU3NTB8&ixlib=rb-4.0.3     - pink pineapple picture
https://images.unsplash.com/photo-1548685913-fe6678babe8d?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTU4NTl8&ixlib=rb-4.0.3     - plain white paint pic
https://images.unsplash.com/photo-1532892082175-d4a24ce91b99?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTU5OTV8&ixlib=rb-4.0.3  - sea water pic
https://images.unsplash.com/photo-1527261460248-b0abfd14c0da?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTYxODV8&ixlib=rb-4.0.3  - desert with blue sky
https://images.unsplash.com/photo-1521193089946-7aa29d1fe776?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTczNTN8&ixlib=rb-4.0.3  - plain img
https://images.unsplash.com/photo-1555679427-1f6dfcce943b?ixid=M3w1MjYzMTh8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk1NTc3OTJ8&ixlib=rb-4.0.3     - plain blue and purplr



# 2. this way only used to change with default theme color
# solution is to use the theme flags when running streamlit from the command line

streamlit run webapp.py --theme.primaryColor="FFF700" --theme.base="dark"


# 3. this way is used to change the background color ,primary color, secondary color and also text color of your streamlit app
"""
Now, to change the theme colour, you first have to create a file named 
“config.toml” and save it inside the directory named “.streamlit” 
and place this directory in the same directory as your python script for the streamlit app.

To do this, you can follow these steps.
    1. First, create a directory named “.streamlit” within the directory
      that contains the python script for your web app (here, my python script is called SurgeApplication.py)
    2. Create a “config.toml” file inside the directory “.streamlit”

Now, you must add colour codes of different elements inside the config.toml, 
and your app will automatically update upon the next run.
    1. “primaryColor”: Primary accent for interactive elements.
    2. “backgroundColor”: Background color.
    3. secondaryBackgroundColor”: Background colour of the sidebar and interactive widgets.
    4. textColor”: Color used for text
"""

# this is the code to add in "config.toml" to change in your streamlit application.

[theme] # You have to add this line

primaryColor = '#FF8C02' # Bright Orange

backgroundColor = '#00325B' # Dark Blue

secondaryBackgroundColor = '#55B2FF' # Lighter Blue

# As your wish you can use the color codes
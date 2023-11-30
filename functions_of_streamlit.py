import streamlit as st

#title
st.title('welcome to my project')

#header
st.header('Youtube data harvesting and warehousing')

#sub header
st.subheader('channel links')

# information
st.info('enter a channel link')

#warning message
st.warning('plaese paste the link here')

#error
st.error('wrong link')

#success message
st.success('successfully updated')

#write
st.write('maths fucntions')
st.write(range(20))

#markdown
st.markdown('# project')
st.markdown('# :star:')

#text
st.text('my first project')

#caption
st.caption('caption is here')

#to display a mathematic function
st.latex(r"(a+b)^2")

#image
#st.image('Screenshot (24).png') it is giving error

#widget
#check box
st.checkbox('login')

#button
st.button('click')

#radio button
st.radio('pick your gender',['male','female','others'])

#select box
st.selectbox('pick your choice',['python','java','html','data science'])

#multi select
st.multiselect('choose a department',['sales','accounts','finance','hr'])

#select slider
st.select_slider('ratings',['bad','good','excellent','outstanding'])

#slider
st.slider('enter a number',0,20)

#number input
st.number_input('pick a number',0,20)

#text input
st.text_input('enter a channel id')

#date input
st.date_input('college passed out')

#time input
st.time_input('enter a working time')

#text area
st.text_area('welcome tell about yourself')

#file upload
st.file_uploader('upload your file')

#color
st.color_picker('select color')

#progress
st.progress(50)

#spinner
with st.spinner('plaese wait'):
    t.sleep(1)

#ballons
st.balloons()

#sidebar
st.sidebar.text_input('enter name')
st.sidebar.text_input('enter age')
st.sidebar.radio('select profession',['student','working','studying'])
st.sidebar.button('submit')

#data visualization
st.title('bar chart')
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)


#sidebar
with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ['home','projects','contact'],
    icons = ['house','book','envelope'],
    menu_icon = 'cast',
    default_index = 0,
    orientation = 'horizontal', # here we use 'vertical' also
  )

if selected == 'home':
   st.title(f'you have selected {selected}')
elif selected == 'project':
   st.title(f'you have selected {selected}')
else:
   st.title(f'you hace selected {selected}')
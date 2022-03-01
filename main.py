import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('Fast Virus Download Portal')

st.write('Mode: Auto Download')

'processing...'

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
     latest_iteration.text (f'downloading... {i+1} %')
     bar.progress(i + 1)
     time.sleep(0.2)

'Completed!!!!'












left_column,right_column = st.columns(2)
button = left_column.button ('Display letters on the right column')

if button:
    right_column.write ('This is the right column.')

expander1 = st.expander ('Enquiry 1')
expander1.write ('The answer of enquiry 1')
expander2 = st.expander ('Enquiry 2')
expander2.write ('The answer of enquiry 2')
expander3 = st.expander ('Enquiry 3')
expander3.write ('The answer of enquiry 3')




# hobby = st.text_input ('What is ur hobby?')
# condition = st.slider('How are u today?',0,10,5)

# 'Ur hobby is', hobby, '.'
# "Today's condition:", condition 


# option = st.selectbox(
#     'what is your favorite number?',
#     list (range (1, 11))
#     )
    
# 'ur favorite number is', option, '.'



# if st.checkbox ('Show Image'):
#     img = Image.open('Filthyfrank.jpg')
#     st.image (img, caption = 'Filthy Frank', use_column_width = True)


# df = pd.DataFrame (
#     np. random. rand (100, 2) / [50,50] + [35.69, 139.70],
#     columns = ['lat', 'lon'])

# st. map(df)

#st.table (df.style.highlight_max(axis = 0))


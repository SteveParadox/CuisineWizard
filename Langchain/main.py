import streamlit as st
from langchainhelper import get_restaurant_name_and_items, how_to

st.title('Fancy Cultural Dishes')

cuisine = st.sidebar.selectbox("Pick a Cuisine",
(
    None,
    'Indian',
    'Chinese',
    'Japanese',
    'Nigerian',
    'Korean',
    'Mexican',
    'Spanish',
    'Italian',
    'Ghanian',
    'English',
    'Russian',
    'Arabic',
    'Finnish',
    'Welsh',
    'Australlian',
    'Argentine',
    'Colombian',
    'Philipino'
))

menu_items = []


if cuisine is not None:
    response = get_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    menu_items = menu_items[0].split('\n')
    menu_items = [item.strip('- ') for item in menu_items if item.strip('- ')]

    st.write('**Menu Items**')
    for i in menu_items:
        st.write(i)
        how_to_options = how_to(i)
        print(how_to_options)
        
        
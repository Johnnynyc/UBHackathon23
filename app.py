from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

    lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

    with st.columns(2):
        st_lottie(lottie_coding, height=300, key="coding")

# Your code for other pages...

if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    #Ellicott | Greiner Hall
    st.header("Ellicott | Greiner Hall")
    col1, col2 = st.columns([1, 3])  
    col1.image("TheElli.png", use_column_width=True)
    col2.subheader("The Elli")
    col2.write("The Elli is our convenience store in the Ellicott Food Court!")

    col1, col2 = st.columns([1, 3])  
    col1.image("aubonpain.png", use_column_width=True)
    col2.subheader("au bon pain The Bakery Cafe")
    col2.write("At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups and salads, our lively, bustling marketplace allows you to personally select the freshest choices.")

    col1, col2 = st.columns([1, 3])  
    col1.image("Hubies.png", use_column_width=True)
    col2.subheader("Hubies")
    col2.write("Hubies in the Ellicott Food Court has a little of everything. Hot, fresh pizza? - you bet - it's a UB tradition. And nobody does wings, fingers and subs like Hubies.")

    col1, col2 = st.columns([1, 3])  
    col1.image("Wrapitup.png", use_column_width=True)
    col2.subheader("Wrap it up")
    col2.write("Make mine a wrap! It will be hard to choose from all the varieties of wraps we offer at Wrap it Up in the Ellicott Food Court. Whether it's filled with meat, eggs, vegetables or even fruit, we've got a wrap variety that will soon become your favorite. As a side, we offer hearty soups and salted snacks. This is also the place for bagels; top one with butter, one of our flavored cream cheeses, or add meat and cheese to make a sandwich.")

    col1, col2 = st.columns([1, 3])  
    col1.image("Sizzles.png", use_column_width=True)
    col2.subheader("Sizzles")
    col2.write("What a grill we've got! Meet us at Sizzles in the Ellicott Food Court for breakfast and try our fresh eggs, sausage, bacon and hash browns. Our lunch and dinner fare features hot, grilled sandwiches, made just how you want them. So for all things grilled, this is the place to go.")

    col1, col2 = st.columns([1, 3])  
    col1.image("The Bowl.png", use_column_width=True)
    col2.subheader("The Bowl")
    col2.write("The Bowl in the Ellicott Food Court is the place to go when you're thinking lighter or maybe some comforting soup. Our salad bar offers a tremendous variety; the freshest veggies, an assortment of greens, cheeses, crispy toppings, specialty oils and vinegars, and dressings.")

    col1, col2 = st.columns([1, 3])  
    col1.image("guacandroll.png", use_column_width=True)
    col2.subheader("Guac and Roll")
    col2.write("If authentic Mexican food is what you're craving, stop by Guac and Roll in the Ellicott Food Court. Our menu features traditional Mexican favorites — tacos, burritos, nachos and more — with a wide variety of sides to accompany your main dish. Choose from one of our homemade salsas and guacamole. We've got everything to give you that South of the Border eating experience.")

    col1, col2 = st.columns([1, 3])  
    col1.image("perks.png", use_column_width=True)
    col2.subheader("Perks")
    col2.write("Perks in the Ellicott Food Court is so much more than your average neighborhood coffee house. Comfortable couches and our cool blues and jazz motif sets the mood for sipping high quality, fresh roasted coffees and teas. Choose from a regular cup of joe or tea, to espresso and specialty iced coffees. Every day we offer a variety of different brew blends from a light roast to a darker roast. A freshly baked muffin, cookie or scone is the perfect compliment to your hot beverage. The Ice Cream Shoppe offers delightfully refreshing treats with sundaes, milkshakes and cones.")

    #North Campus Academic Buildings
    st.header("North Campus Academic Buildings")
    col1, col2 = st.columns([1, 3])  
    col1.image("champa.png", use_column_width=True)
    col2.subheader("Champa Sushi")
    col2.write("Order Champa Sushi in the Student Union for some fresh sushi!")

    col1, col2 = st.columns([1, 3])  
    col1.image("jamba.png", use_column_width=True)
    col2.subheader("Jamba")
    col2.write("Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety for smoothies, fruit juices and so much more.")

    for item in menu_items:
        col1, col2 = st.columns([1, 3])
        col1.image(item["image"], use_column_width=True)
        col2.subheader(item["name"])
        col2.write(item["description"])

if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """
)







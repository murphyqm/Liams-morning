import streamlit as st
import datetime

st.header("Good morning Liam! :sun_with_face:")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

dt_obj = datetime.datetime.now()

st.subheader(f"Let's start {dt_obj.strftime('%A')} off with a nice breakfast! :knife_fork_plate:")

st.subheader("1. Make some tea!  :coffee: ")

with st.expander(":coffee: Tap here to make tea! :coffee:"):
    st.write('''
        #### 1. Fill kettle with water
        #### 2. Make sure lid is on
        #### 3. Switch kettle on
        #### 4. Get cup from cupboard (high up, near the sink)
        #### 5. Get teabag from shelf (high up, over kettle)
        #### 6. Put the teabag in the cup
        #### 7. Pour hot water from the kettle into the cup

    ''')

st.subheader("2. Make some toast!  :bread: ")

with st.expander(":bread: Tap here to make toast! :bread:"):
    st.write('''
        #### 1. Get two slices of bread
        #### 2. Put the bread in the toaster
        #### 3. Switch toaster on
        #### 4. Get a plate from cupboard (high up, near the sink)
        #### 5. Get a butter knife (not sharp, from the drawer near the sink)
        #### 6. Get the butter
        #### 7. Take the toast out of the toaster carefully
        #### 8. Butter the toast

    ''')

st.subheader("3. Get some fruit  :banana: ")
with st.expander(":apple: Tap here to get some fruit :banana:"):
    st.write('''
        #### What kind of fruit would you like?
        
        #### :banana: :tangerine: :apple: :pear: :strawberry: :pineapple:
             
        #### 1. Is there any fruit on the counter that you want?
        #### 2. Is there any fruit in the fruit bowl that you want?
        #### 3. Is there any fruit in the fridge that you want?
    ''')

st.subheader("4. Get some sausages :hotdog: ")
with st.expander(":hotdog: Tap here to get some sausages :hotdog:"):
    st.write('''
        #### 1. Get the lunchbox of sausages from the fridge
        #### 2. Smell them to see if they are still good
        #### 3. Take as many as you want and put them on your plate
        #### 4. If the lunchbox is empty, put it by the sink
        #### 5. If there are still sausages in the lunchbox, put it back in the fridge
    ''')

st.subheader("5. The last thing - a nice glass of water :potable_water:")

st.subheader("Enjoy your breakfast Liam! :sunglasses:")
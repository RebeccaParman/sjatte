import streamlit as st

# Set up the page configuration (title and sidebar)
st.set_page_config(page_title="Rebecca's CV")
st.title("Rebecca's CV")
st.sidebar.success("Select a page above.")



# Custom background image (apply the CSS styling)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/b2ee91ac-78f3-4325-b7f1-0791dd72f0b9/djh4e4o-f8befbb7-c711-4b7e-8628-27284c03cd16.png");
background-size: cover;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}
</style>
"""

# Apply background image to the app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Layout: Containers (Each container will display some content)
with st.container():
    st.write("1")

with st.container():
    st.write("2")

with st.container():
    st.write("3")

with st.container():
    st.write("4")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Left side content")
    with right_column:
        st.write("Right side content")

with st.container():
    st.write("5")

with st.container():
    st.write("6")
#importing streamlit library

import streamlit as st

from PIL import Image

#opening the image

image = Image.open('homeimage.png')

# Define the HTML and CSS for the background image and hovering effect
html_code = """
<style>
body {
    margin: 0;
    padding: 0;
    background: url('homeimage.png') no-repeat center center fixed;
    background-size: cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    text-align: center;
    color: #FFFFFF;
    position: relative;
}

h1 {
    font-size: 72px;
    position: relative;
    text-shadow: 4.5px 5px 4.5px rgba(84, 164, 243, 1); /* Dark yellow shadow */
}

.pulse {
    animation: pulse 4s infinite alternate;
}

@keyframes pulse {
    from {
        font-size: 42px;
    }
    to {
        font-size: 84px;
    }
}

h3 {
    color: yellow; /* Sky blue color */
}
</style>

<body>
<div class="container">
    <h1 class="pulse">ProfitPulse</h1></div>
     <div class ="container">
    
   <h3> Welcome to ProfitPulse! <br ></h3><h4>An approach to provide smart financial decisions for you stock market endeavours </h4>
 </div>
</body>
"""

# Display the HTML code and the image
st.markdown(html_code, unsafe_allow_html=True)
st.image(image, caption='', use_column_width=True)

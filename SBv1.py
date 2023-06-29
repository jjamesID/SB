import streamlit as st
from numpy import arange
import pandas as pd
from fractions import Fraction
import re
import math

st.image('https://uploads-ssl.webflow.com/61dd080b3d2f9fec43b08948/61e5d398a2373f0282831465_InfinityDrainLogo_blk.png', caption = 'Infinite Possibilities')
st.title("Custom Shower Base")
shba = 155
grt = 0
gg = ''
col1, col2 = st.columns(2)
with col1:
    dim1 = st.text_input("Enter dimensions of shower base: ", placeholder = 36, key = 'dim1')
with col2:
    dim2 = st.text_input('', placeholder = 60, key = 'dim2', label_visibility = 'hidden')
if dim1 and dim2:
    side = st.radio('Select Side with Grate:', (dim1 + '"',dim2 + '"'), horizontal = True)
    
drain = st.radio('Select Drain:',('Linear Drain', 'Center Drain'), horizontal = True)
gs1 = ['Wedge Wire', 'Tile Insert', 'Slotted']
if drain == 'Linear Drain':
    grate = st.selectbox('', gs1, key = 'grate', label_visibility = 'collapsed')
    gg = grate
    if grate == 'Wedge Wire':
        grt = 150
    elif grate == 'Tile Insert':
        grt = 125
    else:
        grt = 95
else:
    grt = 50
    gg = drain
mod = st.checkbox('Modify Pricing')
if mod:
    ncol1, ncol2 = st.columns(2)
    with ncol1:
        nsh = st.text_input("Enter cost per square foot for shower base: ", placeholder = 155, key = 'nsh')
    if drain == 'Linear Drain':
        with ncol2:
            ngrt = st.text_input("Enter cost per foot for grate: ", placeholder = 150, key = 'ngrt')
        
st.text('')
calculate = st.button("Calculate")
"---"
if calculate:
    a = 0
    b = 0
    sqft = (math.ceil((int(dim1)/12) * (int(dim2)/12))) + 1
    st.write(str(dim1) + '" x ' + str(dim2) + '" - **' + str(sqft) + " Square Feet**")
    if mod == True:
        if nsh:
            sh = int(nsh) * sqft
            a = str(nsh) + " / sqft"
        else:
            sh = shba * sqft
            a = str(shba) + " / sqft"
    else:
        sh = shba * sqft
        a = str(shba) + " / sqft"
    lrg = math.ceil(int(side.strip('"'))/12)
    if drain == 'Linear Drain':
        if mod == True:
            if ngrt:
                gr = lrg * int(ngrt)
                b = str(ngrt) + ' / ft'
            else:
                gr = lrg * grt
                b = str(grt) + ' / ft'
        else:
            gr = lrg * grt
            b = str(grt) + ' / ft'
    else:
        gr = grt
        b = str(grt)
    fin1, fin2 = st.columns(2)
    with fin1:
        st.write("Shower Base: $" + str(sh))
        st.write(str(gg) + ": $" + str(gr))
        st.write("**Total: $" + str(sh + gr)+'**')
    with fin2:
        st.write("Shower Base: $" + str(a))
        st.write("Grate: $" + str(b))
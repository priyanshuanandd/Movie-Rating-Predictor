# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:29:12 2024

@author: mepri
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home,dataset,form

st.set_page_config(page_title="Movie Rating", page_icon="🎬", layout="wide")
selected = option_menu(
                        menu_title="Movie Rating",
                        options=["Welcome","Data Overview","Form"],
                        icons=["house-heart", "database-down","ui-radios"],
                        default_index=0,
menu_icon="film",                        orientation="horizontal"
                      )

if selected == "Welcome":
    home.welcome()
if selected == "Data Overview":
    dataset.data_overview()
if selected == "Form":
    form.rating_prediction()
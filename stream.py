import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

import datetime
st.set_option('deprecation.showPyplotGlobalUse', False)

# Replace with your Heroku app URL

# Adresse du backend Flask
BACKEND_URL = 'https://backend.herokuapp.com'
def main():
   menu = ['Introduction','Environnement_d_un_Projet Smart Building','Visu Audit Energie + Deploiement Iot','Visu Solutions Iot + Plan Comptage','Visu Conso Energies(Elec/Gaz/Eau)',"Bilan Conso Energies(Elec/Gaz/Eau)"," Axes d'amélioration identifiées",'Visu Suivi des KPI Conso(Elec/Gaz/Eau)','Visu objectifs Réduction Conso Energies','Info + contacts utiles sites']
   choice=st.sidebar.selectbox("Menu",menu)
   
   
   
   
   
   
   
   
   
   
   
   
if __name__ == '__main__':
    main()
import streamlit as s
import stellar_classify as sc
import titanic_data as td



s.set_page_config(page_title='Kaggle Data Sets',layout='wide')
with s.sidebar:
    
    rad=s.radio("Ocean Data Set Page",['Stellar Classification','Titanic Dataset']) 

if(rad=='Carbonate Chemistry'):
    sc.main()

elif(rad=='Carbonate Concentration'):
    td.main()

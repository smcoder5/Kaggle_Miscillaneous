import streamlit as s
import stellar_classify as sc
import obesity_classify as oc
import titanic as td
import flood_probability as fp



s.set_page_config(page_title='Kaggle Data Sets',layout='wide')
with s.sidebar:
    
    rad=s.radio(" Machine Learning Miscellanious",['Stellar Classification','Obesity Classification','Flood Probability','Titanic Dataset']) 

if(rad=='Stellar Classification'):
    sc.main()

elif(rad=='Titanic Dataset'):
    td.main() 
elif(rad=='Obesity Classification'):
    oc.main()
elif(rad=='Flood Probability'):
    fp.main()

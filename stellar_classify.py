import streamlit as s
import tensorflow as tf


def main():
    c1=s.columns(3)
    with c1[0]:
        rs=s.number_input(" Redshift value based on the increase in wavelength",min_value=-1.0, max_value=10.0, value=0.5, step=0.01)
    with c1[1]:
        u=s.number_input("Ultraviolet filter in the photometric system",min_value=0.0, max_value=40.0, value=0.5, step=0.010)
    with c1[2]:
        g=s.number_input("Green filter in the photometric system",min_value=0.0, max_value=40.0, value=0.5, step=0.010)
    c2=s.columns(3)
    with c2[0]:
        r=s.number_input("Red filter in the photometric system",min_value=0.0, max_value=40.0, value=0.5, step=0.010)
    with c2[1]:
        i=s.number_input("Near Infra Red filter in the photometric system",min_value=0.0, max_value=40.0, value=0.5, step=0.010)
    with c2[2]:
        z=s.number_input("Infra Red filter in the photometric system",min_value=0.0, max_value=40.0, value=0.5, step=0.010)
    ## 'redshift','z','u','i','g','r'

    input=[[rs,u,g,r,i,z]] 
    

    s.button("Predict", type="primary")
    if s.button:
        model=tf.keras.models.load_model('stellar_classify_model.h5', compile=False)
        c=s.columns(3) 
        out=model.predict(input)[0]
        with c.columns[0]:
            s.metric("Star Probability in %",round(out[0]*100,2))
        with c.columns[1]:
            s.metric("Galaxy Probability in %",round(out[1]*100,2))
        with c.columns[2]:
            s.metric("Quasor Probability in %",round(out[2]*100,2))

    pass

if __name__=='__main__':


    s.set_page_config(page_title='Stellar Classification',layout='wide')
    main()

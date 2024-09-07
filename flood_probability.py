import streamlit as s
import tensorflow as tf
import numpy as n


def main():
    c1=s.columns(5) 

    with c1[0]:
        mi=s.number_input("Scale the Intensity of Mansoon",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="000") 
    with c1[1]:
        td=s.number_input("Scale the topographic drainage",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="001")
    with c1[2]:
        rm=s.number_input("Scale the River Management",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="002") 
    with c1[3]:
        dft=s.number_input("Scale the Deforestation",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="003") 
    with c1[4]:
        ub=s.number_input("Scale the Urbanization",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="004") 
    
    c2=s.columns(5) 

    with c2[0]:
        cc=s.number_input("Scale the Climate Change",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="005") 
    with c2[1]:
        dq=s.number_input("Scale the Quality of dams",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="006") 
    with c2[2]:
        st=s.number_input("Scale the amount of Siltation",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="007") 
    with c2[3]:
        ap=s.number_input("Scale the Agricultural practices ",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="008") 
    with c2[4]:
        en=s.number_input("Scale the amount of Encroachements",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="009") 

    c3=s.columns(5) 

    with c3[0]:
        idp=s.number_input("Scale the Ineffective Disaster Preparedeness",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="010")
    with c3[1]:
        ds=s.number_input("Scale the Drainage Systems",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="011")
    with c3[2]:
        cv=s.number_input("Scale the Coastal Vulnerability",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="012") 
    with c3[3]:
        ls=s.number_input("Scale the Landslides",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="013") 
    with c3[4]:
        ws=s.number_input("Scale the Watershed Management",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="014")

    c4=s.columns(5) 

    with c4[0]:
        di=s.number_input("Scale the Deterioating Infrastrucure",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="015") 
    with c4[1]:
        ps=s.number_input("Scale the Population Score",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="016") 
    with c4[2]:
        wl=s.number_input("Scale the Wetland Loss",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="017") 
    with c4[3]:
        ip=s.number_input("Scale the Inadequate Planning",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="018") 
    with c4[4]:
        pf=s.number_input("Scale the Political Factors",min_value=0.0,max_value=20.0,value=5.0,step=0.1,key="019") 

    inp=n.array([[mi,td,rm,dft,ub,cc,dq,st,ap,en,idp,ds,cv,ls,ws,di,ps,wl,ip,pf]]) 

    model=tf.keras.models.load_model('model_flood.keras', compile=False) 
    if(s.button("Predict", type="primary",key="025")):
        s.write(inp)
        out=model.predict(inp)[0] 
        s.write(" Flood Probability for given conditions is: "+str(out*100)+"%")


if __name__=="__main__":
    main()

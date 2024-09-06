import streamlit as s
import tensorflow as tf


'''
gend = {'Male': 0, 'Female':1}
fam_hist= {'yes':1, 'no':0}
favc= {'yes':1, 'no':0}     
caec={'Sometimes':3, 'no':2, 'Always':1, 'Frequently':0}
SMOKE= {'no':0, 'yes':1}
SCC= {'no':1,'yes':0} 
CALC= {'Frequently':0, 'no':1, 'Sometimes':2}
MTRANS= {'Walking':0, 'Motorbike':1, 'Bike':2, 'Automobile':3, 'Public_Transportation':4}



'''
def main():
    c1=s.columns(8)
    with c1[0]:
        age=s.number_input("Enter the agw in years",min_value=5,max_value=135,value=25,key="000") 
    with c1[1]:
        ht=s.number_input("Enter the height in meters",min_value=0.5,max_value=2.5,value=1.5,step=0.01,key="001")
    with c1[2]:
        wt=s.number_input("Enter the mass in kg ",min_value=30,max_value=250,value=75,key="002")
    with c1[3]:
        wa=s.number_input("Enter the daily water consumption in liters ",min_value=0.0,max_value=10.0,step=0.1,key="003")   ##Consumption of water daily
    with c1[4]:
        faf=s.number_input("Enter the daily number of main meals ",min_value=0,max_value=7,value=2,step=1,key="004") # Physical activity frequency
    with c1[5]:
        tue=s.number_input("Enter the Time using Technological Devices ",min_value=0.0,max_value=5.0,value=2.0,step=0.01,key="005") ## Time using technology devices 
    with c1[6]:
        ncp=s.number_input("Enter the daily number of main meals ",min_value=0,max_value=7,value=2,step=1,key="006")  ## Number of main meals 
    with c1[7]:
        fcvc=s.number_input("Enter the frequency of vegetable consumption ",min_value=0.0,max_value=5.0,value=2.0,step=0.01,key="007")  ## Frequency of consumption of vegetables

    c2=s.columns(5)

    with c2[0]:
        gend=s.radio("Gender",['Male','Female'],key="008") 
    with c2[1]:
        fam_hist=s.radio("Family History",['Yes','No'],key="009") 
    with c2[2]:
        smoke=s.radio("Smoking History",['Yes','No'],key="010") 
    with c2[3]:
        favc=s.radio("Frequent consumption of high caloric food ",["Yes","No"],key="011") 
    with c2[4]:
        scc=s.radio("Calories consumption monitoring ",['Yes','No'],key="012") 

    caec=s.radio("Consumption of food between meals",['Sometimes','No','Always','Freqiently'],horizontal=True,key="013")
    calc=s.radio("Consumption of Alcohol",['Sometimes','No','Freqiently'],horizontal=True,key="014")
    mtrans=s.radio("Method of Transportation",["Walking","Motorcycle","Cycle","Automobile","Public Transport"],horizontal=True,key="015")

    gender = {'Male': 0, 'Female':1}
    family_hist= {'Yes':1, 'No':0}
    FAVC= {'Yes':1, 'No':0}
    CAEC={'Sometimes':3, 'No':2, 'Always':1, 'Frequently':0}
    SMOKE= {'No':0, 'Yes':1}
    SCC= {'No':1,'Yes':0} 
    CALC= {'Frequently':0, 'No':1, 'Sometimes':2}
    MTRANS= {'Walking':0, 'Motorbike':1, 'Bike':2, 'Automobile':3, 'Public_Transportation':4}

    BMI=wt/ht/ht
    gend,fam_hist,smoke,favc,scc,calc,mtrans=gender[gend],family_hist[fam_hist],SMOKE[smoke],FAVC[favc],SCC[scc],CALC[calc],MTRANS[mtrans]  
    inp=n.array([['gend','age','BMI','fam_hist','favc','fcvc','ncp','caec','smoke','wa','scc','faf','tue','calc',mtrans]]) 
    model=tf.keras.models.load_model('obesity_classify_model.h5', compile=False) 

    if(s.button("Predict", type="primary",key="016")):
        out=model.predict(inp)[0]
        pr,ind=out.max(),n.where(out == out.max())[0][0] 
        obes_class=['Insufficient_Weight','Normal_Weight','Overweight_Level_I','Overweight_Level_II','Obesity_Type_I','Obesity_Type_II','Obesity_Type_III'] 

        s.write(" The given Person is classified as: "+obes_class[ind])
    
    

    



if __name__=="__main__":
    s.set_page_config(page_title='Stellar Classification',layout='wide') 
    main()
    


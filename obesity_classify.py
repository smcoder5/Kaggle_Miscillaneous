import streamlit as s

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



if __name__=="__main__":
    s.set_page_config(page_title='Stellar Classification',layout='wide') 

    c1=s.columns(8)
    with c1[0]:
        age=s.number_input("Enter the agw in years",min_value=5,max_value=135,value=25) 
    with c1[1]:
        ht=s.number_input("Enter the height in meters",min_value=0.5,max_value=2.5,value=1.5,step=0.01)
    with c1[2]:
        wt=s.number_input("Enter the mass in kg ",min_value=30,max_value=250,value=75)
    with c1[3]:
        wa=s.number_input("Enter the daily water consumption in liters ",min_value=0,max_value=10.0,step=0.1)   ##Consumption of water daily
    with c1[4]:
        faf=s.number_input("Enter the daily number of main meals ",min_value=0,max_value=7,value=2,step=1) # Physical activity frequency
    with c1[5]:
        tue=s.number_input("Enter the Time using Technological Devices ",min_value=0,max_value=5,value=2,step=0.01) ## Time using technology devices 
    with c1[6]:
        ncp=s.number_input("Enter the daily number of main meals ",min_value=0,max_value=7,value=2,step=1)  ## Number of main meals 
    with c1[7]:
        fcvc=s.number_input("Enter the frequency of vegetable consumption ",min_value=0,max_value=5,value=2,step=0.01)  ## Frequency of consumption of vegetables

    c2=s.columns(5)

    with c2[0]:
        gend=s.radio("Gender",['Male','Female']) 
    with c2[1]:
        fam_hist=s.radio("Family History",['Yes','No']) 
    with c2[2]:
        smoke=s.radio("Smoking History",['Yes','No']) 
    with c2[3]:
        favc=s.radio("",["Yes","No"]) 
    with c2[4]:
        scc=s.radio("",['Yes','No']) 

    caec=s.radio("",['Sometimes','No','Always','Freqiently'],horizontal=True)
    calc=s.radio("",['Sometimes','No','Freqiently'],horizontal=True)
    mtrans=s.radio("Method of Transportation",["Walking","Motorcycle","Cycle","Automobile","Public Transport"],horizontal=True)

    gender = {'Male': 0, 'Female':1}
    family_hist= {'yes':1, 'no':0}
    favc= {'yes':1, 'no':0}
    caec={'Sometimes':3, 'no':2, 'Always':1, 'Frequently':0}
    SMOKE= {'no':0, 'yes':1}
    SCC= {'no':1,'yes':0} 
    CALC= {'Frequently':0, 'no':1, 'Sometimes':2}
    MTRANS= {'Walking':0, 'Motorbike':1, 'Bike':2, 'Automobile':3, 'Public_Transportation':4}


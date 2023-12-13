import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title (":car: Fatality Prediction Dashboard for Road Traffic Accidents :ambulance:")
st.subheader("Please select the input parameters for the following road traffic accident attributes:")

col1, col2 = st.columns(2)
with col1:
    MONTHS = {0:'Jan',1:'Feb',2:'Mar',3:'Apr',4:'May',5:'Jun',6:'Jul',7:'Aug',8:'Sep',9:'Oct',10:'Nov',11:'Dec'}
    month = st.selectbox('Month of accident', MONTHS.keys(), format_func=lambda x: MONTHS[x])
    #st.write(month)
    
    HOURS = {0:'0:00-1:59',8:'2:00-3:59',9:'4:00-5:59',10:'6:00-7:59',11:'8:00-9:59',1:'10:00-11:59',2:'12:00-13:59',3:'14:00-15:59',
             4:'16:00-17:59',5:'18:00-19:59',6:'20:00-21:59',7:'22:00-23:59'}
    hour = st.selectbox('Hour of accident', HOURS.keys(), format_func=lambda x: HOURS[x])
    #st.write(hour)

    DAYS = {3:'Sun',1:'Mon',5:'Tue',6:'Wed',4:'Thu',0:'Fri',2:'Sat'}
    day = st.selectbox('Day of week', DAYS.keys(), format_func=lambda x: DAYS[x])
    #st.write(day)

    SEXES = {0:'Female',1:'Male',2:'Unknown'}
    sex = st.selectbox('Gender of driver', SEXES.keys(), format_func=lambda x: SEXES[x])
    #st.write(sex)

    AGES = {7:'<15',0:'16-20',1:'21-25',2:'26-35',3:'36-45',4:'46-55',5:'56-65',6:'66-75',8:'>75',9:'Unknown'}
    age_driver = st.selectbox('Age of driver', AGES.keys(), format_func=lambda x: AGES[x])
    #st.write(age_driver)

    HOMES = {0:'Rural',1:'Small town',3:'Urban area',2:'Unknown'}
    home = st.selectbox("Driver's home area", HOMES.keys(), format_func=lambda x: HOMES[x])
    #st.write(home)

    FIRSTS = {3:'Motorway or A(M)',0:'A',1:'B',2:'C',4:'Unknown'}
    first = st.selectbox("First road class", FIRSTS.keys(), format_func=lambda x: FIRSTS[x])
    #st.write(first)

    SECONDS = {3:'Motorway or A(M)',0:'A',1:'B',2:'C',4:'Not at junction or within 20m',5:'Unknown'}
    second = st.selectbox("Second road class", SECONDS.keys(), format_func=lambda x: SECONDS[x])
    #st.write(second)

    RD_TYPES = {2:'Roundabout',1:'One-way street / Slip road',0:'Dual carriageway',3:'Single carriageway',4:'Unknown'}
    rd_type = st.selectbox("Road type", RD_TYPES.keys(), format_func=lambda x: RD_TYPES[x])
    #st.write(rd_type)

    JN_DETAILS = {2:'Not at junction or within 20m',4:'Roundabout',6:'T or staggered junction',5:'Slip road',0:'Crossroads',
                  1:'More than 4 arms (not roundabout)',3:'Private drive or entrance',7:'Unknown'}
    jn_detail = st.selectbox("Junction detail", JN_DETAILS.keys(), format_func=lambda x: JN_DETAILS[x])
    #st.write(jn_detail)

    RD_SURFACES = {0:'Dry',4:'Wet or damp',3:'Snow',1:'Frost or ice',2:'Others / Unknown'}
    rd_surface = st.selectbox("Road surface conditions", RD_SURFACES.keys(), format_func=lambda x: RD_SURFACES[x])
    #st.write(rd_surface)

    SPEEDS = {0:'20',1:'30',2:'40',3:'50',4:'60',5:'70',6:'Unknown'}
    speed = st.selectbox("Speed limit", SPEEDS.keys(), format_func=lambda x: SPEEDS[x])
    #st.write(speed)

with col2:
    VEH_TYPES = {5:'Pedal cycle',3:'Motorcycle',6:'Taxi',1:'Car',0:'Bus',7:'Van',2:'Goods vehicle',4:'Others / Unknown'}
    veh_type = st.selectbox("Vehicle type", VEH_TYPES.keys(), format_func=lambda x: VEH_TYPES[x])
    #st.write(veh_type)

    ENGINES = {0:'0-500',3:'501-1000',1:'1001-1500',2:'1501-2000',4:'>2000',5:'Unknown'}
    engine = st.selectbox("Engine capacity cc", ENGINES.keys(), format_func=lambda x: ENGINES[x])
    #st.write(engine)

    AGES_VEH = {0:'0-1',4:'2-3',5:'4-5',6:'6-7',7:'8-9',1:'10-11',2:'12-13',3:'14 and above',8:'Unknown'}
    age_veh = st.selectbox('Age of vehicle', AGES_VEH.keys(), format_func=lambda x: AGES_VEH[x])
    #st.write(age_veh)

    VEH_NUMS = {0:'1',1:'2',2:'3',3:'4',4:'5 and above'}
    veh_num = st.selectbox('Number of vehicles involved', VEH_NUMS.keys(), format_func=lambda x: VEH_NUMS[x])
    #st.write(veh_num)

    MANS = {10:'Reversing',9:'Parked',16:'Waiting to go - held up',11:'Slowing or stopping',5:'Moving off',14:'U-turn',
            12:'Turning left',17:'Waiting to turn left',13:'Turning right',18:'Waiting to turn right',0:'Changing lane to left',
            1:'Changing lane to right',7:'Overtaking moving vehicle - offside', 8:'Overtaking static vehicle - offside',
            6:'Overtaking - nearside',2:'Going ahead left-hand bend',4:'Going ahead right-hand bend',3:'Going ahead other',
            15:'Unknown'} 
    man = st.selectbox('Vehicle manoeuvre', MANS.keys(), format_func=lambda x: MANS[x])
    #st.write(man)

    JN_LOCS = {8:'Not at junction or within 20m',0:'Approaching junction or waiting/parked at junction approach',
               1:'Cleared junction or waiting/parked at junction exit',6:'Leaving roundabout',4:'Entering roundabout',
               5:'Leaving main road',3:'Entering main road',2:'Entering from slip road',7:'Mid Junction - on roundabout or on main road',
               9:'Unknown'}
    jn_loc = st.selectbox("Junction location", JN_LOCS.keys(), format_func=lambda x: JN_LOCS[x])
    #st.write(jn_loc)

    SKIDDINGS = {1:'None',3:'Skidded',4:'Skidded and overturned',0:'Jackknifed',2:'Overturned',5:'Unknown'}
    skidding = st.selectbox("Skidding and overturning", SKIDDINGS.keys(), format_func=lambda x: SKIDDINGS[x])
    #st.write(skidding)

    LEAVES = {0:'Did not leave carriageway',1:'Nearside',3:'Straight ahead at junction',2:'Offside',4:'Unknown'}
    leave = st.selectbox("Vehicle leaving carriageway", LEAVES.keys(), format_func=lambda x: LEAVES[x])
    #st.write(leave)

    IMPACTS = {1:'Did not impact',2:'Front',0:'Back',4:'Offside',3:'Nearside',5:'Unknown'}
    impact = st.selectbox("First point of impact", IMPACTS.keys(), format_func=lambda x: IMPACTS[x])
    #st.write(impact)

    LIGHTS = {3:'Daylight',0:'Darkness - lights lit',1:'Darkness - lights unlit',2:'Darkness - no lighting',4:'Unknown'}
    light = st.selectbox("Lighting conditions", LIGHTS.keys(), format_func=lambda x: LIGHTS[x])
    #st.write(light)

    WEATHERS = {0:'Fine no high winds',3:'Raining no high winds',4:'Snowing no high winds',2:'High winds',1:'Fog or mist',5:'Unknown'}
    weather = st.selectbox("Weather conditions", WEATHERS.keys(), format_func=lambda x: WEATHERS[x])
    #st.write(weather)

    RD_AREAS = {2:'Urban',0:'Rural',1:'Unknown'}
    rd_area = st.selectbox("Urban or rural area", RD_AREAS.keys(), format_func=lambda x: RD_AREAS[x])
    #st.write(rd_area)

X_test_le = pd.DataFrame(np.array([[month, hour, day, veh_num, first, rd_type, speed, jn_detail, second, light, weather, rd_surface,
                                    rd_area,veh_type, man, jn_loc, skidding, leave, impact, sex, age_driver, engine, age_veh, home]]))

filename = 'RF_3C_model.sav'
model_fitted = pickle.load(open(filename, 'rb'))

prediction = model_fitted.predict(X_test_le)[0]
#prediction=0 means non-fatal
#prediction=1 means non-fatal

prediction_proba = model_fitted.predict_proba(X_test_le)
#RHS is prob of fatality
fatal_prob = str(round(prediction_proba[0][1],3))

if prediction == 0:
    st.subheader("The road traffic accident is predicted to be NON-FATAL.")
    st.subheader("The predicted probability of fatality is " + fatal_prob + ".")

else: 
    st.subheader("The road traffic accident is predicted to be FATAL.")
    st.subheader("The predicted probability of fatality is " + fatal_prob + ".")

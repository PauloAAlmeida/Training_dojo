import pandas as pd
import calendar
def pre_p(df):
    import pandas as pd
    import calendar
    df['Dep_time_hour'] = df['Dep_Time'].str.slice(stop=2)
    df['Dep_time_hour'] = pd.to_numeric(df['Dep_time_hour'], downcast = 'float')

    df['Route'] = df['Route'].str.replace(' ', '')

    df['Date_of_Journey_day'] = df['Date_of_Journey'].str.slice(stop=2)
    df['Date_of_Journey_day'] = df['Date_of_Journey_day'].str.replace('/', '')
    df['Date_of_Journey_day'] = pd.to_numeric(df['Date_of_Journey_day'], downcast = 'float')

    df['Date_of_Journey_Month'] = df['Date_of_Journey'].str.slice(start=3, stop=-5)
    df['Date_of_Journey_Month'] =pd.to_numeric(df['Date_of_Journey_Month'], downcast='unsigned')
    df['Date_of_Journey_Month'] =df['Date_of_Journey_Month'].astype('Int64')
    df['Date_of_Journey_Month'] = df['Date_of_Journey_Month'].apply(lambda x: calendar.month_name[x])
    df['today'] = '2019-03-01'
    df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'], dayfirst = True)
    df['today'] = pd.to_datetime(df['today'])
    df['lag'] = df['Date_of_Journey']  - df['today']
    df['lag'] =df['lag'].astype('str')
    df['lag'] = df['lag'].str.replace('days','')
    df['lag'] = df['lag'].str.replace('00','')
    df['lag'] = df['lag'].str.replace('::.0','')
    df['lag'] = pd.to_numeric(df['lag'], downcast='unsigned')
    df['lag'] =df['lag'].astype('Int64')


    df['Additional_Info'] = df['Additional_Info'].str.replace('No Info', 'No info')
    return print('pre processamento concluído')
 

def feature_bin(df):
    
    df['Dep_t_hour_bin']=0
    df['lag_bin'] = 0
    df['Date_of_J_day_bin'] = 0
    for i in range (len(df)):
        a = df['Dep_time_hour'][i] 
        b = puc.time_bin(a)
        df['Dep_t_hour_bin'][i] = b
               
        e = df['Date_of_Journey_day'][i] 
        f = puc.time_day(e)
        df['Date_of_J_day_bin'][i] = f
        
        g = df['lag'][i] 
        h = lag_bin(g) 
        df['lag_bin'][i] = h
    return print('Feature engineering concluído com sucesso')

def lag_bin(x):
   
    if 0<x<=1:
        return 0
    elif 1<x<=3:
        return 1
    elif 3<x<=9:
        return 2
    elif 9<x<=15:
        return 3
    elif 15<x<=30:
        return 4
    elif x>30:
        return 5

def bin_df(df):
    for i in range (len(df)):
        a = df['Dep_time_hour'][i] 
        b = puc.time_bin(a)
        df['Dep_t_hour_bin'][i] = b
               
        e = df['Date_of_Journey_day'][i] 
        f = puc.time_day(e)
        df['Date_of_J_day_bin'][i] = f
        
        g = df['lag'][i] 
        h = lag_bin(g) 
        df['lag_bin'][i] = h
        
       
  

def time_day(x):
    if 0<x<=6:
        return 0
    elif 6<x<=12:
        return 1
    elif 12<x<=18:
        return 2
    elif 18<x<=24:
        return 3
    elif 24<x<=31:
        return 4
   
      

def time_bin(x):
   
    if 0<x<=6:
        return 0
    elif 6<x<=12:
        return 1
    elif 12<x<=18:
        return 2
    elif 18<x<=24:
        return 3
    
def lag_bin(x):
   
    if 0<x<=2:
        return 0
    elif 2<x<=5:
        return 1
    elif 5<x<=15:
        return 2
    elif 15<x<=25:
        return 3
    elif 25<x<=40:
        return 4
    elif x>40:
        return 5
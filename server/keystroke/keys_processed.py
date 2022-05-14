import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def convert_json(data):
    return pd.json_normalize(data)

def save_capture_data_to_file(user, data):  
    data.to_csv(f'keystroke/userdata/user_logs/{user}_logs.csv',  index=False) 

def read_capture_data_from_file(user):     
    return pd.read_csv(f'keystroke/userdata/user_logs/{user}_logs.csv')
    
def save_processed_data_to_file(user, data):
    data.to_csv(f'keystroke/userdata/processed_data/{user}_processed_data.csv', index=False) 

def processing_keys(data):

    df = pd.DataFrame(columns=['keycode','HD','PPD','RPD', 'RRD'])

    event_len = len(data)

    for i in range(event_len-3):
        if str(data.iloc[i].event) == 'Down':
            finalData = {}
            cur_key_press_time = data.iloc[i].time
            cur_key_release_time =  data[(data.keycode==data.iloc[i].keycode)&(data.event=='Up')&(data.time>data.iloc[i].time)].iloc[0].time
            next_key_press_time = data[(data.event=='Down')&(data.time>data.iloc[i].time)].iloc[0].time
            next_key_keycode = data[(data.event=='Down')&(data.time>data.iloc[i].time)].iloc[0].keycode
            next_key_release_time =  data[(data.keycode==next_key_keycode)&(data.event=='Up')&(data.time>next_key_press_time)].iloc[0].time
            finalData['keycode'] = data.iloc[i].keycode
            finalData['HD'] = cur_key_release_time-cur_key_press_time
            finalData['PPD'] = next_key_press_time-cur_key_press_time
            finalData['RPD'] = next_key_press_time-cur_key_release_time
            finalData['RRD'] = next_key_release_time-cur_key_release_time
            df = df.append(finalData,ignore_index=True)

    return df       
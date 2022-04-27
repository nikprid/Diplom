import pandas as pd

def generate_dataset(processed_file, user):

    tmp = pd.read_csv(processed_file)

    users_data = pd.read_csv('userdata/data.csv')
    users_data_for_learning = users_data.sample(frac=1).reset_index(drop=True)[:len(tmp)]

    user_data_for_learning = pd.concat([users_data_for_learning, tmp], ignore_index=True)
    new_users_data = pd.concat([users_data, tmp], ignore_index=True)
    new_users_data.to_csv('userdata/data.csv', index=False)

    user_data_for_learning.user = user_data_for_learning.user.apply(lambda x: 1 if x==user else 0)
    user_data_for_learning.to_csv('data_for_models/+'+user+'_model.csv', index=False)


    


# user = 'Nikita'

# data = pd.DataFrame(columns=['keycode','HD','PPD','RPD', 'RRD', 'user'])

# for file in glob.glob("userdata/processed_data/*_processed_data.csv"):
#     print('[+]:', file)
#     tmp = pd.read_csv(file)
#     data = pd.concat([data, tmp], ignore_index=True)

# data.user = data.user.apply(lambda x: 1 if x==user else 0)

# data.to_csv('userdata/data.csv', index=False)    
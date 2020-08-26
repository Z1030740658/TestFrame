from utils.read_csv import read_from_csv
# from utils.deserialize_json import deserialize_json #use it to read test data from JSON


_user_data = 'test_data/users.csv'

USER_IDS = read_from_csv(_user_data)

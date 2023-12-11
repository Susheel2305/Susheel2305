import pandas as pd
def generate_car_matrix(C:\Users\susheelkumarhs\Dropbox\PC\Downloads/Python_1_1.csv):
    df = pd.read_csv(C:\Users\susheelkumarhs\Dropbox\PC\Downloads/Python_1_1.csv)
    car_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    car_matrix.values[[range(car_matrix.shape[0])]*2] = 0
    return car_matrix
dataset_path = 'Python_1_1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)

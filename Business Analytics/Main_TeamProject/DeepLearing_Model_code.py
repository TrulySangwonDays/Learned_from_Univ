import pandas as pd
import numpy as np
import tensorflow as tf
from collections import Counter
import time

from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Flatten, Dense, Conv1D, MaxPooling1D, LSTM, GRU, Reshape
from keras.optimizers import Adam
from keras.layers import Dropout, BatchNormalization
from keras.callbacks import TensorBoard

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def replace_missing_values(lst):
    # Use a list comprehension to create a new list where None values are replaced with 0
    new_list = [0 if str(item) == 'nan' else item for item in lst]
    return new_list

def find_last_occurrence(lst, value):
    try:
        # Reverse the list and find the index of the value
        # Use len(lst) - 1 to get the position in the original list
        position = len(lst) -1 - lst[::-1].index(value)
        return position
    except ValueError:
        # If the value is not found, return a message or handle it as needed
        return -1
    
def find_min_within_range(lst, start):
    try:
        # Get the sublist within the specified range
        sublist = lst[start: start + 11]
        # Find the minimum value and its index in the sublist
        min_value = min(sublist)
        min_index = start + sublist.index(min_value)
        return min_value, min_index
    
    except ValueError:
        return None   

def calculate_slope(lst, index, target):
    try:
        # Calculate the slope using neighboring points
        slope = (lst[target] - lst[index]) / (target - index)
        return -slope
    
    except IndexError:
        return None
    
def find_max_slope_within_distance(lst, min_distance, max_distance):
    max_slope = float('-inf')
    max_slope_start_index = None
    max_slope_end_index = None

    for i in range(len(lst)):
        for j in range(i + 1 + min_distance, min(i + 1 + max_distance, len(lst))):
            slope = (lst[j] - lst[i]) / (j - i)

            if slope > max_slope:
                max_slope = slope
                max_slope_start_index = i
                max_slope_end_index = j

    return max_slope, max_slope_start_index, max_slope_end_index



df = pd.read_csv('유행어 예측 모델/data.csv', encoding='UTF8')
del df['연/월']
# print(df)

phrase = []
rapid = []

data_x = df.fillna(0)

target_value = 150
min_distance = 2
max_distance = 10

for i in df.columns:

    process = []

    period = Counter(df[i])
    if 150 in period:
        phrase.append(1)
    else: phrase.append(0)
    
    process = df[i].values.tolist()
    drop_null = []
    drop_null = replace_missing_values(process)

    if 150 not in period:
        loc = drop_null.index(max(drop_null))
 
    else:   
        loc = find_last_occurrence(drop_null, target_value)

    min10, minpoint = find_min_within_range(drop_null, loc)

    slope = calculate_slope(drop_null, loc, minpoint)

    if slope >= 6:
        rapid.append(1)
    else:
        rapid.append(0)

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_x)
normalized_df = pd.DataFrame(normalized_data, columns=data_x.columns)

data = normalized_df.transpose()
data = data.loc[:,::-1]

y = pd.DataFrame(phrase)

acc=[]

for i in range(10):

    X_train, X_test, y_train, y_test = train_test_split(data, y, test_size= 0.2)

    model = Sequential()
    model.add(BatchNormalization())

    model.add(Reshape(target_shape=(-1, 256)))
    model.add(Conv1D(filters=32, kernel_size=3, activation='relu', data_format='channels_first'))
    model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(128))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    tensorboard = TensorBoard(log_dir='유행어 예측 모델/logs/{}'.format(str(int(time.time()))))

    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['binary_accuracy'])

    model.fit(X_train, y_train, epochs=300, validation_split = 0.2, callbacks=[tensorboard])

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose = 2)
    print("Accuracy:", np.round(test_acc, 5))
    acc.append(np.round(test_acc, 5))

print(acc)
print(np.mean(acc))
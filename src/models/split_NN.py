import sys
import os
import tensorflow.keras as keras
from tensorflow.keras import layers
from src.preprocessing import load_data
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import LSTM, Conv1D, Flatten

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


class split_NN():

    def __init__(self):

        self.name = "split_NN"
        self.dataset_type = "split"
        
    def create_model(self, params, index, logger):

        input1 = keras.Input(batch_shape=(params[index]["batch_size"], params[index]["max_code_length"],
                             params[index]['dataset'].len_encoding),
                             name='input_1')
        input2 = keras.Input(batch_shape=(params[index]["batch_size"], params[index]["max_code_length"],
                             params[index]['dataset'].len_encoding),
                             name='input_2')

        dense1 = layers.Dense(1024, activation='relu', name='dense_1')(input1)
        dense1 = keras.layers.Dropout(params[index]['dropout'])(dense1)
        dense1 = layers.Dense(1024, activation='relu', name='dense_2')(dense1)
        dense1 = keras.layers.Dropout(params[index]['dropout'])(dense1)
        dense1 = layers.Dense(1024, activation='relu', name='dense_3')(dense1)

        dense2 = layers.Dense(1024, activation='relu', name='dense_1')(input2)
        dense2 = keras.layers.Dropout(params[index]['dropout'])(dense2)
        dense2 = layers.Dense(1024, activation='relu', name='dense_2')(dense2)
        dense2 = keras.layers.Dropout(params[index]['dropout'])(dense2)
        dense2 = layers.Dense(1024, activation='relu', name='dense_3')(dense2)


        concat = layers.concatenate([dense1, dense2])
        dense1 = Dense(2048, activation='relu', name="dense_1")(concat)
        dense2 = Dense(1024, activation='relu', name="dense_2")(dense1)
        dense3 = Dense(512, activation='relu', name="dense_3")(dense2)
        dense4 = Dense(256, activation='relu', name="dense_4")(dense3)

        outputs = Dense(1, activation='sigmoid', name='predictions')(dense4)

        model = keras.Model(inputs=(input1, input2), outputs=outputs, name=self.name + "-" + str(index))
        model.summary()

        return model

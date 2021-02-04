# Based on:
# https://github.com/pareeknikhil/biofeedback/blob/master/OpenBCI Device Data Stream/openBCIStream.py

import time

import brainflow
import numpy as np
import pandas as pd
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from brainflow.data_filter import AggOperations, DataFilter, FilterTypes


def scale_magnitude_array(x, ymin, ymax):
    x = np.array(x)
    return (x - ymin) / (ymax - ymin)


def board_2_df(data):
    # data = scale_magnitude_array(data, -396, 433)
    df = pd.DataFrame(data[:, [1, 2, 3, 4, 5, 6, 7, 8, 22]], columns=[
        "EEG ch0",
        "EEG ch1",
        "EEG ch2",
        "EEG ch3",
        "EEG ch4",
        "EEG ch5",
        "EEG ch6",
        "EEG ch7",
        "TIME"])
    #print(data)
    return df


class CytonBoard(object):
    def __init__(self, serial_port):
        self.params = BrainFlowInputParams()
        self.params.serial_port = serial_port
        self.board = BoardShim(BoardIds.CYTON_BOARD.value, self.params)

    def start_stream(self):
        self.board.prepare_session()
        self.board.start_stream()

    def stop_stream(self):
        self.board.stop_stream()
        self.board.release_session()

    def save_data(self):
        data = self.board.get_board_data()
        #DataFilter.write_file (data, '.\Data\cyton_data_new.txt', 'w')
        # Could add check to see if file already exists, adding a 1, 2, etc. on the end to avoid conflict
        # Could use date function for generating names based on date-time.

    def poll(self, sample_num):
        try:
            while self.board.get_board_data_count() < sample_num:
                time.sleep(0.02)
        except Exception as e:
            raise (e)
        board_data = self.board.get_board_data()
        DataFilter.write_file (board_data, '.\Data\cyton_data_new.txt', 'a') # 'a' appends; 'w' overwrites
        df = board_2_df(np.transpose(board_data))
        return df

    def sampling_frequency(self):
        sampling_freq = self.board.get_sampling_rate(BoardIds.CYTON_BOARD.value)
        return sampling_freq
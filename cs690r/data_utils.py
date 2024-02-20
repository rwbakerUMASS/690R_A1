import copy
import numpy as np
import pandas as pd
from types import SimpleNamespace


def load_sensor_from_csv(file):
    '''
    load sensor data from csv file
    '''
    data = pd.read_csv(file)

    # Save 
    sensor_data = SimpleNamespace()
    sensor_data.sample_rate = 100
    sensor_data.acc = data[['acc_x', 'acc_y', 'acc_z']].to_numpy()
    sensor_data.free_acc = data[['freeacc_x', 'freeacc_y', 'freeacc_z']].to_numpy()
    sensor_data.gyr = data[['gyr_x', 'gyr_y', 'gyr_z']].to_numpy()
    sensor_data.mag = data[['mag_x', 'mag_y', 'mag_z']].to_numpy()
    return sensor_data


def load_mocap_from_tsv(path):
    '''
    load mocap data from tsv file
    '''
    data = np.genfromtxt(path, delimiter='\t', skip_header=12)
    
    # Save
    mocap_data = SimpleNamespace()
    mocap_data.sample_rate = 150
    mocap_data.pos = data[:, [2, 3, 4]] / 1000
    return mocap_data


def trim_data(data_obj, start, end, sensor_type):
    data_obj = copy.deepcopy(data_obj)
    
    if sensor_type == 'sensor':
        data_obj.acc = data_obj.acc[start:end]
        data_obj.free_acc = data_obj.free_acc[start:end]
        data_obj.vel = data_obj.vel[start:end]
        data_obj.pos = data_obj.pos[start:end] - data_obj.pos[start]
        
        data_obj.gyr = data_obj.gyr[start:end]
        # data_obj.mag = data_obj.mag[start:end]
        
    elif sensor_type == 'mocap':
        data_obj.pos = data_obj.pos[start:end] - data_obj.pos[start]
        data_obj.vel = data_obj.vel[start:end]
        data_obj.acc = data_obj.acc[start:end]
    
    return data_obj
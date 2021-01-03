from tests.helpers import FlightsDataset
import json
from numpy import load
import numpy as np

def test_dataset_shape():
    flights_dataset = FlightsDataset()
    assert flights_dataset.get_y_shape() == (1, 144, 1)
    assert flights_dataset.get_x_shape() == (1, 144, 2)
    fd = flights_dataset.make_future_dataframe(12)
    assert fd.shape == (1, 156, 2)
    assert len(flights_dataset) == 1

    dict_data = load('tests/helpers/data.npz')
        
    assert np.array_equal(flights_dataset[0][0],dict_data['arr_0']) and np.array_equal(flights_dataset[0][1],dict_data['arr_1'])
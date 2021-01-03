from tests.helpers import FlightsDataset

def test_dataset_shape():
    flights_dataset = FlightsDataset()
    assert flights_dataset.get_y_shape() == (1, 144, 1)
    assert flights_dataset.get_x_shape() == (1, 144, 2)
    fd = flights_dataset.make_future_dataframe(12)
    assert fd.shape == (1, 156, 2)
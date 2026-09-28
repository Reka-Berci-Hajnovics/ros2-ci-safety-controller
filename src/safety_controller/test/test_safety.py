from safety_controller.safety import limit_velocity


def test_stops_when_close():
    assert limit_velocity(1, 0.2) == 0


def test_halfs_when_close():
    assert limit_velocity(1, 0.9) == 0.5


def test_return_velocity():
    assert limit_velocity(20, 2) == 20


def test_at_half_meter():
    assert limit_velocity(20, 0.5) == 10


def test_at_one_meter():
    assert limit_velocity(20, 1.0) == 20


def test_negative_value():
    assert limit_velocity(-2, 2) == -2

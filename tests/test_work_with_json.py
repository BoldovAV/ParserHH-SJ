from src.work_with_json import HHJson, SJJson

hh = HHJson()
sj = SJJson()


def test_hh_json_from():
    assert isinstance(hh.from_json(), list)


def test_hh_json_to():
    assert hh.to_json() is None


def test_sj_json_from():
    assert isinstance(sj.from_json(), list)


def test_sj_json_to():
    assert sj.to_json() is None

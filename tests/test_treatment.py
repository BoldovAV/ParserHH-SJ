from src.treatment import HeadHuntSearch, SuperJobSearch

hh = HeadHuntSearch(0)
sj = SuperJobSearch(0)


def test_hh_search_get():
    assert isinstance(hh.get_vacancies_from_json(), list)


def test_sj_search_get():
    assert isinstance(sj.get_vacancies_from_json(), list)


def test_avg_payment():
    assert isinstance(sj.avg_payment(), int)
    assert isinstance(hh.avg_payment(), int)


def test_str():
    assert isinstance(str(sj), str)
    assert isinstance(str(hh), str)

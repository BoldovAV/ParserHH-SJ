from src.API import HeadHunt, SuperJob

keyword = "developer"
pay_min = 10000
pay_max = 20000


def test_hh_get():
    assert isinstance(HeadHunt(keyword, pay_min, pay_max).get_vacancies(), str)


def test_sj_get():
    assert isinstance(SuperJob(keyword, pay_min, pay_max).get_vacancies(), dict)

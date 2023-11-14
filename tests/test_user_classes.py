from src.user_classes import Welcome
from io import StringIO

keyword = "developer"
pay_min = 10000
pay_max = 20000

wk = Welcome(keyword, pay_min, pay_max)

test_input = ['1', '2', '3', '4', 'qwe', '0']


def test_init_welcome():
    assert wk.keyword == keyword
    assert wk.pay_from == pay_min
    assert wk.pay_to == pay_max


# def test_site_search():
#     assert wk.site_search()(StringIO(test_input[4])) == (TypeError, ValueError, AssertionError)

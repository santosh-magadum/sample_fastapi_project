from api import sample_test

def test_sample_test_func():
    print("inside the test function")
    num = 5
    res = sample_test(num)
    assert "Successfully tested the sample test, num: 5" == res



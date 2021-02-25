try:
    d = {'baba': 1}
    assert d['baba'] == 2
    for k, v in d.items():
        d['dqdo'] = 5  # this will cause runtime error

except (RuntimeError, ValueError, TypeError):
    print('error happened')

except AssertionError:
    print('Some assert was false')

finally:
    print('always executed')

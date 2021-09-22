import pandas as pd
import datetime
import matplotlib.pyplot as plt


# https://pl.wikipedia.org/wiki/Problem_Collatza
def fun(val: int) -> int:
    if val == 1:
        return 1
    if val % 2 == 0:
        return int(val / 2)
    else:
        return int(val * 3 + 1)

def fib(val: int):
    if val == 1:
        return 1
    if val % 2 == 0:
        val = int(val / 2)
    else:
        val = int(val * 3 + 1)
    return fib(val)

if __name__ == '__main__':
    start = datetime.datetime.now()
    maxx = None
    max_len = 0
    i = 199000336001
    dfs = {}
    for start_i in range(1, 77030):
        vals = []
        i = start_i
        #print(i)
        vals.append(i)
        while i != 1:
            i = fun(i)
            vals.append(i)
        dfs[str(start_i)] = pd.DataFrame(vals)
        # fib(i)
        if max_len < len(vals):
            maxx = start_i
            max_len = len(vals)

    end = datetime.datetime.now()
    print(f'Ended in {end - start}')
    dfs
    # print(max([dfs[k].shape[0] for k in dfs.keys()]))
    ax = plt.axes()
    ax.plot(dfs[str(maxx)])
    ax.set(xlabel='step', ylabel='value',
       title=f'Problem_Collatza for {maxx}')
    plt.show()
    print(1)
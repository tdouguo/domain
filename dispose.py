# coding=utf-8
import sys
import re
import os
import numpy as np

aa = r'(.+)\1*'
aaa = r'(.)\1{2}'

aabb = r'(.)\1(.)\2'
aaab = r'(.)\1\1.'
abbb = r'.(.)\1\1'
abab = r'(.)(.)\1\2'


def check(domain):
    _domain = domain[:4].lower()
    # print(_domain)
    # print('aa', re.match(aa, _domain))
    # print('aaa', re.match(aaa, _domain))
    # print('aabb', re.match(aabb, _domain))
    # print('aaab', re.match(aaab, _domain))
    # print('abbb', re.match(abbb, _domain))
    # print('abab', re.match(abab, _domain))
    if (re.match(aaa, _domain) is not None):
        return 1, 'aaa'
    elif re.match(aabb, _domain) is not None:
        return 1, 'aabb'
    elif re.match(aaab, _domain) is not None:
        return 1,'aaab'
    elif re.match(abbb, _domain) is not None:
        return 1,'abbb'
    elif re.match(abab, _domain) is not None:
        return 1,'abab'
    if _domain.isalpha():
        return 1, "xxxx"
    elif _domain.isdigit():
        return 1, '0000'
    if _domain[0] == _domain[2] or _domain[1] == _domain[3]:
        return 1,'abab'
    elem, count = np.unique(tuple(_domain), return_counts=True)
    if np.sum(count>1):
        return 2,'aa'
    # print(_domain)
    return 0,''


def main(file):
    ts = []
    num2 = []
    with open(file, 'r') as f:
        for line in f.readlines():
            domain = line.strip('\n')
            code,r = check(domain)
            if code == 2:
                num2.append(domain)
            elif code == 1:
                ts.append(domain)


    ts = list(set(ts))
    if len(ts) > 0:
        f = open(file.replace('domain', 'ts_out_len4_'), "w")
        for line in ts:
            f.write(line + '\n')
        f.close()

    num2 = list(set(num2))
    if len(num2) > 0:
        f2 = open(file.replace('domain', 'out_len4_'), "w")
        for line in num2:
            f2.write(line + '\n')
        f2.close()





if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 2:
        file = sys.argv[1]
        main(file)
    else:
        for root, dirs, files in os.walk('completed'):
            print(root, dirs, files)
            for file in files:
                main(os.path.join(root, file))

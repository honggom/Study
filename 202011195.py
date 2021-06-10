def exam1(data):
    return '짝' if data % 2 == 0 else '홀'


def exam2(data):
    return list(set(data))


def exam3(data):
    return [data * i for i in range(1, 10)]


def exam4(data):
    phones = {"S5": 2014, "S7": 2016, "note8": 2017, "S9": 2018, "S10": 2019}
    return phones[data]


def exam5(data):
    tmp = data.split('-')
    return '남성' if tmp[1][0] == '1' else '여성'


def exam6(data):
    return data ** 2


def exam7(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    return data


def exam8(data):
    return (data ** 2) * 3.14


def exam9(data):
    tmp = data.split('-')
    return tmp[0]+"-"+tmp[1]+"-####"


def exam10(data):
    return sum(data, 0.0) / len(data)

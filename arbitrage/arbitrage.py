
if __name__ == '__main__':
    num = int(input())
    while num != 0:
        currency = list(input().split())
        R = int(input())
        exchangeList = []
        for i in range(R):
            exchangeList.append(list(input().split()))

        print(exchangeList)

        num = int(input())


# 2
# CZK EUR
# 2
# CZK EUR 25:1
# EUR CZK 1:25
# 2
# GBP USD
# 2
# USD GBP 8:5
# GBP USD 5:9
# 3
# BON DEM CZK
# 3
# DEM BON 1:6
# BON CZK 1:5
# DEM CZK 1:20
# 3
# CZK EUR GBP
# 3
# CZK EUR 24:1
# EUR GBP 5:4
# GBP CZK 1:30
# 3
# CZK USD GBP
# 4
# CZK USD 28:1
# CZK GBP 31:1
# GBP CZK 1:31
# USD GBP 1:1
# 0
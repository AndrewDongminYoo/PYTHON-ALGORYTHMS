shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    result = 0
    index = 0
    length = min(len(prices), len(coupons))
    for i in range(length):
        result += prices[i] * (100-coupons[i])/100
        index += 1
    result += sum(prices[index:])
    return round(result)


if __name__ == '__main__':
    print(get_max_discounted_price(shop_prices, user_coupons))
    # 926000 이 나와야 합니다.

def get_phone(country, area, firdt, last):
    return f"+{country}-({area})-{firdt}-{last}"
phone_num = get_phone(1, 800, 555, 1212)
print(phone_num)

def make_country(name, capital):
    country = {
        'name': name,
        'capital': capital
    }
    return country


country_info = make_country("Ukraine", "Kyiv")


print(country_info)

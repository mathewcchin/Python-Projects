from pygal_maps_world.i18n import COUNTRIES

# create an inverted COUNTRIES dictionary
country = {x: y for y, x in COUNTRIES.items()}


def find_country_code(country_name):
    """Return the 2-digit country code used for pygal, using the passed in country_name"""
    if country_name in country:
        return country[country_name]
    else:
        return None


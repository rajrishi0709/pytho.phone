import phonenumbers
from test import number


from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
print(geocoder.country_name_for_number(ch_number, "en"))
print(geocoder.description_for_valid_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
print(carrier.name_for_valid_number(service_number, "en"))
print(carrier.safe_display_name(service_number, "en"))
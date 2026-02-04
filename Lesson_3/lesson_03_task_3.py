from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "12")

mailing = Mailing(to_address, from_address, 150, "RB123456789RU")

print(mailing)

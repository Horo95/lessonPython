from address import Address
from mailing import Mailing

toAd=Address('789246','Moscow','Pavlova','23','67')#to_address
fromAd=Address('123456','Moscow','Panasenko','29','369')#from_address


copy=Mailing(toAd,fromAd,1000,'shgfl63786')

#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.

print(f'Отправление {copy.track} из {copy.from_address.index}, {copy.from_address.city}, {copy.from_address.street}, {copy.from_address.house} - {copy.from_address.flat} в {copy.to_address.index}, {copy.to_address.city}, {copy.to_address.street}, {copy.to_address.house} - {copy.to_address.flat}. Стоимость {copy.cost} рублей.')
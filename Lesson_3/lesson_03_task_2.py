from smartphone import Smartphone

catalog = [
    Smartphone("Infinix", "40 pro", "+79681293089"),
    Smartphone("Redmi", "8 pro", "+79112607742"),
    Smartphone("iPhone", "16 Pro Max", "+79208453677"),
    Smartphone("Xiaomi Poco", "X6 Pro", "+79315842276"),
    Smartphone("Nokia Lumia", "1520", "+79114329537")
]

for smartphone in catalog:
    print(f"{smartphone.make} - {smartphone.model}. {smartphone.number}")

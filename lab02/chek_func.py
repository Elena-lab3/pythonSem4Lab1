from ser_factory import SerializerFactory


def func():
    print("it works.")

Fabric = SerializerFactory()
ser = Fabric.create_serializer("json")

ser.dump(func,"file.json")

f = ser.load("file.json")
f()
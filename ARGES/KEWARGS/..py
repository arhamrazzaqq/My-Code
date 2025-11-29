def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Mr.", "John", "Doe", street="123 Main St", city="Anytown", state="CA", zip="12345")

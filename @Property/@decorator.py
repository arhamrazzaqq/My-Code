def add_sprinckles(func):
    def wrapper(*args, **kwargs):
        print("YOU ADD SPRINCKLES!")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("YOU ADD FUDGE!!")
        func(*args, **kwargs)
    return wrapper

@add_sprinckles
@add_sprinckles

def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla")
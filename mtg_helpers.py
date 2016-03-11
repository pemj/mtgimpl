from mtg_card import *

# returns 0 on successful damage
def damage(source, target, amount):
    try:
        target.damage += amount
        return 0
    except AttributeError:
        print("target no longer valid")
        return 1
    except NameError:
        print("target no longer valid")
        return 1
    except ReferenceError:
        print("target no longer valid")
        return 1



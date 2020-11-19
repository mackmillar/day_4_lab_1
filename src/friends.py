def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
      
    return False

def add_friend(person, friend):
    person["friends"].append(friend)
    
def remove_friend(person, friend):
    person["friends"].remove(friend)


def total_money(people):
    total = 0

    for person in people:
        total = total + person["monies"]

    return total

def l_money(lender, lendee, amount):
    lender["monies"] = lender["monies"] - amount
    lendee["monies"] = lendee["monies"] + amount

    return lendee["monies"], lender["monies"]

def all_favourite_foods (people):
    favourite_foods = []
    for person in people:
        favourite_foods.extend(person['favourites']['snacks'])
    return favourite_foods

def find_no_friendends(people):
    no_friends = []
    for person in people:
        if person["friends"] == []:
            no_friends.append(person)

    return no_friends
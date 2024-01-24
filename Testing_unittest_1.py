def adds(num=0):
    try:
        if num!=None and num!="":
             return int(num)+5;
        else:
            return ("please enter a number")
    except ValueError as valerr:
        return valerr
    except AssertionError as asserr:
        print("you have asserted the wrong number to check")
print(adds(6))        
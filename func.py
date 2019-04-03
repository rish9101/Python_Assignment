import credentials

def excep(username):
    error_message = f"I'm Sorry {username}"
    print(error_message)

def decor(func):
    def inner(*args,**kwargs):
        if args[0] in [usernames[0] for usernames in credentials.myresult]:
            return func(args[0])
        else:
            return excep(args[0])
    return inner

@decor
def foo(username):
    message = f"Hey There, {username} .Do you want an avengers' spoiler??"
    print(message)

# username = input("Enter a username: ")

# foo(username)

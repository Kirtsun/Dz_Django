def foo():
    if True:
        if False:
            return 1
    else:
        print("form not sent, rendering from for user")
    return 2



print(foo())
def up_lows(str):
    """
    Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33
    :return:
    """
    # low = 0
    # ups = 0
    #
    # for l in str.split():
    #     if l.isupper():
    #         ups += 1
    #     else:
    #         low += 1
    #
    # print(f"No. of Upper case characters : {ups}")
    # print(f"No. of Lower case Characters : {low}")

    #above didn't work

    d = {"upper": 0, "lower": 0}
    for c in str:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass

    print("Original string : ", str)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

up_lows("'Hello Mr. Rogers, how are you this fine Tuesday?'")

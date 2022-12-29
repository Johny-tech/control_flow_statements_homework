def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    res_str =""

    if a<0:
        res_str+="negative"
    if a>0:
        res_str+="positive"
    if a%2==1:
        res_str+=" odd number"
    else:
        res_str+=" even number"

    print(res_str)

    return res_str

main(-7)
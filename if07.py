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

    if a%2==0:
        res_str+=" even number"
    else:
        res_str+=" odd number"


    return res_str

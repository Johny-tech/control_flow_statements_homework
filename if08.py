def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    res_str =""
    digits = {
        1 : "one-digit",
        2: "two-digit",
        3: "three-digit"
    }

    res_str = digits[len(str(a))]

    if a%2==1:
        res_str+=" odd number"
    else:
        res_str+=" even number"
    print(res_str)
    return res_str


def rangeBitwiseAnd(left, right):
    ans = right
    for i in range(left, right):
        ans &= i
    return ans

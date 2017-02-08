
def find_max_min(param):
    param.sort()
    result = []

    
    first = param[0]
    last = param[len(param)-1]

    if first == last:
        result.append(first)
        return result
    else:
        result.append(first)
        result.append(last)
        return result

find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
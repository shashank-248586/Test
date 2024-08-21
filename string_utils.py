def reverse_string(s):
    result = ""
    for i in range(len(s)-1,-1,-1):
        result+=s[i]
    return result


def capitalize_string(s):
    return s.upper()
    
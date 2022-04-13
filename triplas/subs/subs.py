def is_substring(str1, str2):
    for i in range(len(str1)-len(str2)):
        if str1[i:i+len(str2)] == str2:
            return True
    return False

print(is_substring('casorio', 'casa'))

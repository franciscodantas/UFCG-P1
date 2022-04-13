def is_substring_expr(str1,str2):
    inicio = ''
    meio = ''
    fim = ''
    if str1 == '':
        return False
    for i in range(len(str2)):
        if str2[i] == '*':
            primeira = str2[0:i]
            segunda = str2[i+1:len(str2)+1]
    for i in range(len(primeira)):
        inicio += str1[i]
    if inicio == primeira:
        for i in range(len(segunda)*-1,0):
            fim += str1[i]
        if fim == segunda:
            for i in range(len(primeira),(len(str1)-len(segunda))):
                meio += str1[i]
            if meio != '':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid():
    string = "hahah"
    tamanho = len(string)
    if tamanho % 2 == 0:
        return ""
    else:
        posicao = round(tamanho / 2) - 1
        return string[posicao]
nada = mid()
print(nada)
mid()






# # def mid(string):
#     string_len = len(string)
#     have_middle_letter = string_len % 2
#     if have_middle_letter != 0:
#         middle = round(string_len / 2) - 1
#         return string[middle]
#     else:
#         return ''
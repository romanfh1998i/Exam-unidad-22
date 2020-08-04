# def math(n):
#    if n == 1:
#      return[n]
#    if n % 2 == 0 :
#      return [n]+math(n/2)
#    else :
#      return [n]+math(n*3+1)
# print(math(20))

# [1,2,3,4,5]
# def suma(list1):
#   if list1==[]:
#     return 0
#   else:
#     c=list1[0]
#     list_s=list1[1:]
#     return c+suma(list_s)
# print(suma([1, 3]))

lst = ['o', 'e', 'f']
dicc = {
    'a': {
        'b': {
            'c': 'Hi'
        }
    },
    'd': {
        'e': {
            'f': 'Hello'
        }
    },
    'g': {
        'h': {
            'i': 'Bye'
        }
    }
}
d = dict(zip(lst, list(dicc.values())))

# DL = dict(zip((lst, dicc))

# for i,j in zip(sorted(dicc),lst):
#   print(dicc[i],j)
#   if dicc.has_key('a'):
#     return

# for key in keys:
#     obj = obj[key]
# return obj
# def diccionario(L,D):
#   d=dict(zip(L,list(D.values())))

# print diccionario(lst,dicc)

# def diccionario(dicc, lst):
#   if lst == []:
#     return dicc
#   else:
#     return diccionario(dicc[lst[0]], lst)
# print diccionario(dicc,lst)


def diccionario(Di, Li):
    P, R = Li[0], Li[1:]
    if Li[0] not in Di:
      print("no esta en la lista")
    else:
      if R:
        return diccionario(Di[P], R)
    # if Li[0] not in Di:
    #     print("no esta en la lista")

      else:
        return Di[P]
    return 0

print diccionario(dicc, lst)

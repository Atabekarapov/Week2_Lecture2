# 1)  # list (тип данных который очень упорядочный)
# massive (разные типы данных)
# nums = [1, [2,3,4,[5,6,7]],3, 4]
# nums.append(6)
# print(nums)
# nums.pop()
# print(nums[1][3][1])

# 2)
# prod1 = "Iphone12"
# prod2 = "Samsung12s"
# karzina = [prod1, prod2, 1, 2, 3] (ссылка который отрпавить другому)

# 3)  
# spisok1 = [1, 2, 3]       (every letter is a one product)
# name = "Atabek"
# spisok2 = list(name)
# print(spisok2)

# 4) 
# spisok = ['name', 'makers', True, 2, [3, 4, 5]]
# spisok.append('word') (добавляет элемент в конце)
# print(spisok)

# 5)
# spisok = ['name', 'makers', True, 2, [3, 4, 5]]
# spisok.clear()   (deleted)
# print(spisok)

# 6) 
# spisok = ['name', 'makers', True, 2, [3, 4, 5]]
# new_spisok = spisok.copy()
# # new_spisok[4][0] = 'new word'   (поменяли внутр)
# print(new_spisok)
# print(spisok)

# 7)
# spisok = ['name', 'makers', True, 2, [3, 4, 5]]
# new_spisok = spisok.copy()  (поверхности копиру)
# spisok[4][1] = 'word'
# print(spisok)
# print(new_spisok)

# 8)
# from copy import deepcopy
# spisok = ['name', 'makers', True, 2, [3, 4, 5]]
# new_spisok = deepcopy(spisok)  (копирует только список,не измен)
# spisok[4][1] = 'word'
# print(spisok)
# print(new_spisok)

# 9)
# from copy import deepcopy
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# num = spisok.count('4')    (ищет)
# print(num)

# 10)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# spisok2 = [0, 9, 8, 7, 6, 'word1']
# name = '2' 
# # spisok.extend(name)   (делает конкетанация, расширает)
# spisok3 = spisok2 + name
# print(spisok3)

# 11)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# num = spisok.index(2, 4)   (ишет)
# print(num)

# 12)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# spisok.insert(3,'indexed')   (dobovlyat slova)
# print(spisok)

# 13)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# item = spisok.pop()    (udalyaet poslednim i perekinivaet na item, vyrezivaet)
# print(item)
# print(spisok)

# 14)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# spisok.remove(True)     (udalyaet snachenie po obektu)
# print(spisok)

# 15)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# spisok.reverse()       (perevernuet)
# print(spisok)

# 16)
# spisok = ['name', 'makers', True, 2, [3, 4, 5], 2, 'name', 2]
# spisok = [4, 2, 7, 9, 6, 8, 1]
# spisok.sort(reverse=False)     (sortiruet tolko sifry)      
# print(spisok)

# 17) Len     (shitaet kolichestvo simvolov  stroke)
# spisok = ['abc', 'bdsg', 'jgjjgjgjsg', 'jgjgjadw']
# spisok.sort()            (sortiruet cherez ASCI table, vsegda malenkim stanet bolshe chem bolshim)
# print(spisok)

# 18)
# spisok = ['abc', 'bdsg', 'jgjjgjgjsg', 'jgjgjadw']
# print(spisok[1:3])




















































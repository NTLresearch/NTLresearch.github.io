
#* Tip 1: Always use enumerate over range

# loop through item
hero_list = ['Axe', 'Jug', 'Vs', 'Tinker', 'CK']
for hero in hero_list:
    print(hero)

#* Output:
# Axe
# Jug
# Vs
# Tinker
# CK

# loop using index
for i in range(len(hero_list)):
    hero = hero_list[i]
    print(hero)

#* Output:
# Axe
# Jug
# Vs
# Tinker
# CK

# enumerate
iterator_hero = enumerate(hero_list)
print(type(next(iterator_hero)))
print(next(iterator_hero)); 
print(next(iterator_hero))

#* output
# <class 'tuple'>
# (0, 'Axe')
# (1, 'Jug')


# enumerate loop
for i, hero in enumerate(hero_list):
    print(f'{i+1}:{hero}')

#? could used below code with base 1 loop  code with base 1 loop code with base 1 loop code with base 1 loop code with base 1 loop code with base 1 loop
for i, hero in enumerate(hero_list, 1):
    print(f'{i}:{hero}')

#* output
# 1:Axe
# 2:Jug
# 3:Vs
# 4:Tinker
# 5:CK



#* Tip 1: Always use enumerate over range



immutable_var_ = 32, 12, True, 'Man'
print(immutable_var_)
#immutable_var_[0] = 200 - Это вызовет TypeError, кортеж не поддерживает обращение по элементам
mutable_list = [23, 31 , 'fatal']
mutable_list.append("food")
print(mutable_list)
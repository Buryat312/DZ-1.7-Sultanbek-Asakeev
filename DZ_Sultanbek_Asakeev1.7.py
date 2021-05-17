from datetime import date

band = {
    'group_members':{
        'Adam':{'role': 'singer', 'birthdate': (1978,3,18)},
        'Jesse':{'role': 'songwriter', 'birthdate': (1979,4,2)},
        'Sula':{'role': 'drums', 'birthdate': (1988,2,24)}
    },
    'concert':{
        'Budapest':{
            'concert_date': date(2021,8,12),
            'expenses': [79,500,500],
            'income': 10000
        },
        'Berlin':{
            'concert_date': date(2021,7,25),
            'expenses': [89,800,750],
            'income': 20000
        },
        'Prague':{
            'concert_date': date(2021,8,1),
            'expenses': [90, 400, 500],
            'income': 15000
        },
        'Bratislava':{
            'concert_date': date(2021,8,25),
            'expenses': [70, 400, 500],
            'income': 15000
        }
        
    }
}
#Напишите функцию удаления участника. 
def udalenie(band, name):
    return band['group_members'].pop(name)
udalenie(band, 'Adam')
print(band['group_members'])
print()

# #Напишите функцию добавления участника в группу.
def add_member(band, **kwargs):
    band['group_members'].update(kwargs)
    return band

print(add_member(band, **{'Valera': {'role': 'guitar', 'birthdate': (2000,12,25)}})) 
print()

#Напишите функцию добавления концерта
def add_concert(band, **kwargs):
    band['concert'].update(kwargs)
    return band

print(add_concert(band, **{'Vienna': {'concert_date': date(2021,8,25), 'expenses': [85, 800, 700], 'income': 1500}})) 

#Напишите функцию, которая высчитывает общую сумму затрат за концерт.

def sum_expenses(band):
    total_expenses = 0
    for i in band:
        total_expenses += i
    return total_expenses
k = sum_expenses(band['concert']['Budapest']['expenses'])
print(k) # print(sum_expenses(band['concert']['Budapest']['expenses']))
print(sum_expenses(band['concert']['Berlin']['expenses']))

#Напишите функцию, высчитывающую выгоду за концерт(разницу между затратами и суммой контракта)
def benefit(band, concert_place):
    i = band['concert']['Budapest']['expenses']
    a = band['concert'][concert_place]['expenses']
    return i - a

print(benefit(band, 'Berlin'))

# print(band)

from random import randint, choice
from faker import Faker
import datetime
import sqlite3


def number_generator():
    def choose_ddd():
        ddd_list = [
            11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34,
            35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62,
            63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85,
            86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99
                    ]
        
        return choice(ddd_list)
    
         
    return f'({choose_ddd()})9 {randint(5000, 9999)}-{randint(0000, 9999)}'
    
    
def nasc_data_generator():
    year_today = datetime.date.today().year
    month_today = datetime.date.today().month
    day_today = datetime.date.today().day
    
    year_random = randint(1950, int(year_today))
    month_random = randint(1, 12)
    day_random = randint(1, 31)
    
    months_w_31days = [4,6,9,11]
    
    if day_random == 31 and month_random not in months_w_31days:
        day_random -= 1
        
    if day_random > 28 and month_random == 2:
        day_random = 28
        
    if year_random == year_today and month_random > month_today or month_random == month_today:
        month_random = month_today
        
        if day_random > day_today:
            day_random = day_today
    
    return f'{day_random}/{month_random}/{year_random}'
        

if __name__ == '__main__':
    # Conexão DataBase e Cursor
    connection = sqlite3.connect('') # Seleciona o banco de dados sqlite3
    cursor = connection.cursor()
    
    # Instancia do Faker
    fake = Faker('pt_BR')
    
    for i in range(1000):
        cursor.execute(
            f'INSERT INTO Clientes VALUES' 
            f'(NULL, "{fake.name()}", "{str(number_generator())}", "{nasc_data_generator()}")'
            )
        connection.commit()
        
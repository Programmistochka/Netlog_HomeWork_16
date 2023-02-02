from datetime import datetime as dt
from application.salary import calculate_salary as calc_salary
from application.db.people import get_employees as get_emp


if __name__ == '__main__':
    print(f'Текущая дата: {dt.today().date()}')
    calc_salary()
    get_emp()
#! /usr/bin/env python3
import sys

#print(sys.argv)

def tax_caculator(salary):
    tb_salary = salary - 3500
    if tb_salary <= 0:
        return 0
    elif tb_salary <= 1500:
        return tb_salary*3/100
    elif tb_salary <= 4500:
        return tb_salary*10/100 - 105
    elif tb_salary <= 9000:
        return tb_salary*20/100 - 555
    elif tb_salary <= 35000:
        return tb_salary*25/100 - 1005
    elif tb_salary <= 55000:
        return tb_salary*30/100 - 2755
    elif tb_salary <= 80000:
        return tb_salary*35/100 - 5505
    else:
        return tb_salary*45/100 - 13505

def insure_caculator(salary):
    return salary*8/100 + salary*2/100 + salary*0.5/100 + salary*6/100

for arg in sys.argv[1:]:
    membersalary = arg.split(':')
    member = membersalary[0]
    salary_str = membersalary[1]
    try:
        salary = int(salary_str)
        print(member+':'+'{:.2f}'.format(salary-insure_caculator(salary)-tax_caculator(salary-insure_caculator(salary))))
    except:
        print("Parameter Error")



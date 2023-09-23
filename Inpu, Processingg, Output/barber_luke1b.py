
#Intro and Inputs
print("This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period.")
print("")
initial = float(input("To begin, enter how much money you would like to initially invest (i.e. 500): "))
print("")

#Variables
annualrate = float(input("Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: "))
monthlyrate = float(annualrate/12)


#Interest Formula
month_amount = initial*(1+monthlyrate)
month_amount2 = initial*(1+monthlyrate)**2
month_amount3 = initial*(1+monthlyrate)**3

interest1 = month_amount-initial
interest2 = month_amount2-month_amount
interest3 = month_amount3-month_amount2

form_int1 = format(interest1, ',.2f')
form_int2 = format(interest2, ',.2f')
form_int3 = format(interest3, ',.2f')

initial1 = format(initial,',.2f')
initial2 = format(month_amount,',.2f')
initial3 = format(month_amount2,',.2f')

#Display
print('')
print('Calculating . . .')
print('')
month = format('Month','7s')
starting_balance = format('Starting Balance', '20s')
interest = format('Interest','12s')
ending_bal = 'Ending Balance'
print(month,starting_balance,interest,ending_bal)
print(format('1','7s'),format(str(initial1), '20s'),format(str(form_int1),'12s'), format(month_amount, ',.2f'))
print(format('2','7s'),format(str(initial2), '20s'),format(str(form_int2),'12s'), format(month_amount2, ',.2f'))
print(format('3','7s'),format(str(initial3), '20s'),format(str(form_int3),'12s'), format(month_amount3, ',.2f'))



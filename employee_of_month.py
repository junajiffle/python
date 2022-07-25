work_hours = [('aby',100),('bob',200),('catlin',500),('den',800)]
def employe_of_month(work_hours):
    max_hours = 0
    employee_of_the_month = 0
    for employee,hours in work_hours:
        if max_hours < hours:
            max_hours = hours
            employee_of_the_month = employee
        else:
            pass

    return(employee_of_the_month,max_hours)
employe_of_month(work_hours)


work_hours = [('Abby',100),('Billy',400),('Cassie',800), ('Sam', 2000)]

def best_employee(work_hours):

    current_max_hours = 0
    best_employee = ''
    for employee, hours in work_hours:
        if hours > current_max_hours:
            current_max_hours = hours
            best_employee = employee
        else:
            pass

    return (best_employee, current_max_hours)

print(best_employee(work_hours))


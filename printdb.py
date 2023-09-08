from persistence import *

def main():
    #TODO: implement
    print("Activities")
    sorted_emp_rep_list = list(repo.activities.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.date)
    for a in sorted_emp_rep_list:
        printed_tuple = (a.product_id,a.quantity,a.activator_id,a.date.decode() )
        print(printed_tuple)


    print("Branches")
    sorted_emp_rep_list = list(repo.branches.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.id)
    for b in sorted_emp_rep_list:
        printed_tuple = (b.id,b.location.decode(),b.number_of_employees)
        print(printed_tuple)


    print("Employees")
    sorted_emp_rep_list = list(repo.employees.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.id)
    for e in sorted_emp_rep_list:
        printed_tuple = (e.id,e.name.decode(),e.salary,e.branche)
        print(printed_tuple)

    
    print("Products")
    sorted_emp_rep_list = list(repo.products.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.id)
    for p in sorted_emp_rep_list:
        printed_tuple = (p.id,p.description.decode(),p.price,p.quantity)
        print(printed_tuple)

    
    
    print("Suppliers")
    sorted_emp_rep_list = list(repo.suppliers.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.id)
    for s in sorted_emp_rep_list:
        printed_tuple = (s.id,s.name.decode(),s.contact_information.decode())
        print(printed_tuple)


    print()
    print("Employees report")
    sorted_emp_rep_list = list(repo.employees.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.name) 
    for e in sorted_emp_rep_list:
        activitie_l = repo.activities.find(activator_id = e.id)
        sum_employee_income = 0
        for activitie in activitie_l:
            product_quantity = activitie.quantity
            product_price = repo.products.find(id = activitie.product_id).pop().price
            sum_employee_income += product_price*product_quantity
        
        print(str(e.name.decode()) + " " + str(e.salary) + " " + str(repo.branches.find(id = e.branche).pop().location.decode()) + " " + str(-1*sum_employee_income))
    
    print()
    print("Activities report")
    
    c = repo._conn.cursor()
    c.execute("SELECT a.date, p.description, a.quantity , e.name, s.name FROM activities as a JOIN products as p ON a.product_id = p.id LEFT JOIN employees as e ON e.id = a.activator_id LEFT JOIN suppliers as s ON s.id = a.activator_id")


    sorted_act_rep_list = list(c.fetchall())
    sorted_act_rep_list.sort(key=lambda x: x[0]) 
    for a in sorted_act_rep_list:
        memb1 = a[3].decode() if isinstance(a[3],bytes) else a[3]
        memb2 = a[4].decode() if isinstance(a[4],bytes) else a[4]
        printed_tuple = (a[0].decode(),a[1].decode(),a[2],memb1,memb2)
        print(printed_tuple)



    
            
        
      

        
            
    

    
    pass

if __name__ == '__main__':
    main()
company_employee = input()
company_info = {}
while company_employee != 'End':
    company_employee = company_employee.split(' -> ')
    company_name = company_employee[0]
    employee_id = company_employee[1]
    if company_name not in company_info:
        company_info[company_name] = [employee_id]
    else:
        if employee_id not in company_info[company_name]:
            company_info[company_name].append(employee_id)
    company_employee = input()
for company, employee_id in sorted(company_info.items(), key=lambda kvp: kvp):
    print(f'{company}')
    for id in employee_id:
        print(f'-- {id}')
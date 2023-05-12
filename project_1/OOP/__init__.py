#Улучшите класс DepartmentReport.
# Класс при инициализации должен принимать переменную company_name и 
# инициализировать её значением атрибут company,
# а также инициализировать атрибут revenues пустым списком.
# Метод average_revenue должен возвращать строку:
# "Average department revenue for (company_name): (average_revenue)"


class DepartmentReport():
    
    def __init__(self, company_name):
        self.revenues = []
        self.company = company_name
    
    def add_revenue(self, amount):
        if not hasattr(self, 'revenues'):
            self.revenues = []
        self.revenues.append(amount)
        
    def average_revenue(self):
        average = int(round(sum(self.revenues) / len(self.revenues), 0))
        return f'Average department revenue for {self.company}, {average}'       
    
report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())     
print(DepartmentReport(company_name = 'Danon').company)
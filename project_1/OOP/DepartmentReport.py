class DepartmentReport():
    def add_revenue(self, amount):
        if not hasattr(self, 'revenues'):
            self.revenues = []
        self.revenues.append(amount)
    def average_revenue(self):
        return sum(self.revenues) / len(self.revenues)
    def print_reveneus(self):
        print('Mean sales:', self.average_revenue())
        
        
report = DepartmentReport()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# [1000000, 400000]
print(report.average_revenue())                
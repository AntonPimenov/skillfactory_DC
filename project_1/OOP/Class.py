# class SalesReport():
#     def print_report(self):
#         print('Total amount:', self.amount)
        

# report = SalesReport()
# report.amount = 10
# report_2 = SalesReport()
# report_2.amount = 20

# # def print_report(report):
# #     print('Total amount:', report.amount)
    
# report.print_report()
# report_2.print_report()

class SalesReport():
    def add_deal(self, amount):
        if not hasattr(self, 'deals'):
            self.deals = []
        self.deals.append(amount)
    def total_amount(self):
        return sum(self.deals) 
    def print_report(self):
        print('Total sales:', self.total_amount())
        
report = SalesReport()
report.add_deal(1000)
report.add_deal(3333)
report.print_report()                  
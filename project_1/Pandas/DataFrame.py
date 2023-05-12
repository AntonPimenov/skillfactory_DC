# Ваша задача — проанализировать чистую прибыль.
# Доходы (income), расходы (expenses) и годы (years), соответствующие им, предоставлены вам в виде списков.

# Например:

# income = [478, 512, 196]
# expenses = [156, 130, 270]
# years = [2018, 2019, 2020]

# Создайте функцию create_companyDF(income, expenses, years), 
# которая возвращает DataFrame, составленный из входных данных со столбцами Income и Expenses и индексами,
# соответствующими годам рассматриваемого периода.
# Пример такого DataFrame представлен ниже.

#     Income  Expenses
# 2018    478     156
# 2019    512     130
# 2020    196     270

# Также напишите функцию get_profit(df, year), 
# которая возвращает разницу между доходом и расходом, 
# записанными в таблице df, за год year.
# Примечание. Если информация за запрашиваемый год не указана в вашей таблице, вам необходимо вернуть None.

# Примечание. Не забудьте ипортировать библиотеки.

import pandas as pd

import pandas as pd
def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        },
        index = years
    )
    return df
def get_profit(df, year):
    if year in df.index:
        profit = df.loc[year, 'Income'] - df.loc[year, 'Expenses']
    else:
        profit=None
    return profit
    

income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]


print(create_companyDF(income, expenses, years))
print()
year = 2017
df = create_companyDF(income, expenses, years)

print(get_profit(df, year))



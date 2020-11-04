import pandas as pd

wr = open('/Users/enriquevazquez/Desktop/Financial Analisis/Results.txt', 'w' )
csv_path = '/Users/enriquevazquez/Desktop/budget_data.csv'

data = pd.read_csv(csv_path)
data_df = pd.DataFrame(data)

data_df_temp = data_df['Date']
data_df_temp = data_df_temp.str.split(pat = "-", expand=True)

wr.write('Financial Analysis\n-------------------------')

print(f'Total months : {data_df_temp[0].count()}')
wr.write('\nTotal months : ' + str(data_df_temp[0].count()))
print(f'Total : $ {data_df["Profit/Losses"].sum()}')
wr.write('\nTotal : $' + str(data_df["Profit/Losses"].sum()))

data_df_temp = data_df["Profit/Losses"].diff()
print(f'Average  Change: $ {round((data_df_temp.sum()) / (data_df_temp.count()),2)}')
wr.write('\nAverage  Change: $ ' + str(round((data_df_temp.sum()) / (data_df_temp.count()),2)))

data_df['Average Changes'] = data_df["Profit/Losses"].diff()

res = data_df.loc[data_df['Average Changes'] == (data_df["Profit/Losses"].diff()).max()]
print(f'Greatest Increase in Profits: {res.iloc[0]["Date"]} $({res.iloc[0]["Average Changes"]})')
wr.write('\nGreatest Increase in Profits: ' + str(res.iloc[0]["Date"]) + ' $(' + str(res.iloc[0]["Average Changes"]) + ')')

res = data_df.loc[data_df['Average Changes'] == (data_df["Profit/Losses"].diff()).min()]
wr.write('\nGreatest Increase in Profits: ' + str(res.iloc[0]["Date"]) + ' $(' + str(res.iloc[0]["Average Changes"]) + ')')

wr.write('\n\nEn promedio cada mes se pierde dinero y hay que revasar las fechas en las que \nse perdio y se gano mas dinero y replicarlo o evitarlo en los proximos meses si es posible')



wr.close()
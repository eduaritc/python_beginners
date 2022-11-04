import pandas as pd

if __name__ == '__main__':
    #print('hello')
    data = pd.read_csv('C:/Users/eduar/Desktop/Bigmarket.csv', delimiter=',')
    """"
    print(data)
    print(type(data))
    print(data.head())
    print(data.tail())
    print(data.shape)
    print(data.info())
    print('--------------')
    #print(data.iloc[2:4,0])
    #print(data[(data.Sales > 4000) & (data.Month == 'Feb')])
    #print(data.sort_values('Sales', ascending=True))
    #print(data.sort_values('Sales', ascending=False).iloc[:5])
    print(data.sort_values(['Store','Sales']))
    print('--------------')"""

    dict = {
        'Month':['June', 'June'],
        'Store':['A', 'B'],
        'Sales':[30000, 50000]
    }

    new_data = pd.DataFrame(dict)
    #print(new_data)
    #print(data.append(new_data))
    #print(pd.concat([data, new_data], ignore_index=True))
    states = ['Alaska', 'Texas', 'California', 'Montana', 'New Mexico']
    states_dict = {'states': states}
    new_col = pd.DataFrame(states_dict)
    #print(new_col)
    """"
    print('--------------')
    print(pd.concat([data, new_col], axis=1))
    print('--------------')
    """
    print('--------------')
    #print(data['Sales'].sum())
    # print(data[(data.Sales > 4000) & (data.Month == 'Feb')])
    #print('Sum of sales for store A: {}'.format(data[(data.Store == 'A')]['Sales'].sum()))
    #asales = data[(data.Store == 'A')]['Sales'].sum()
    #bsales = data[(data.Store == 'B')]['Sales'].sum()
    #print(asales if asales > bsales else bsales)
    #print(data[(data.store == 'A')])

    print(data['Month'].value_counts())
    data['Sales'] = data['Sales'].replace([31037], 50000)
    print(data.head())
    print(data.drop([0]))
    data = data.rename(columns={'Store':'NewStore'})
    print(data.head())



    print('--------------')

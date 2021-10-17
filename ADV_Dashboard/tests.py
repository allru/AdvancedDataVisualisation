import pandas as pd

df = pd.read_csv('ErdbebenDaten.csv')
#print(df)

df = pd.concat([df, df['place'].str.split(', ', expand=True)], axis=1)
df.rename(columns={0: 'place', 1: 'state'}, inplace=True)
#print(df)


states = []

for element in df['state']:
    if element not in states:
        states.append(element)

print(states)
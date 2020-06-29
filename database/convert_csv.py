from pandas import read_excel
sheet='ProfEquip'
file=input('Insira o nome do arquivo: ')
file_name=file+'.xls'
df=read_excel('xls/'+file_name,sheet_name=sheet,header=None)
df=df[7:26][[0,1,2,3,4,5]]
df.columns=['Categoria','Total','Atendem pelo SUS','Não atendem pelo SUS','Profissionais/1000 habitantes','Profissionais pelo SUS/1000 habitantes']
df.to_csv ('csv/'+file+'.csv', index = None, header=True)

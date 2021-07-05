import pandas as pd
import seaborn as sns
import matplotlib as plt

trainDF = pd.read_csv(r'C:\Users\Joerg\Desktop\DS_Competitions\Trainingsdaten.csv')
testDF = pd.read_csv(r'C:\Users\Joerg\Desktop\DS_Competitions\Testdaten.csv')
trainDF.head()
trainDF.isnull().count()
# sns.barplot(x=trainDF["ApplicantIncome"],y=trainDF["CoapplicantIncome"])

trainDF = trainDF[0].sort_values(ascending=True)[45:50]

trainDF.plot(kind='bar')
plt.xlabel("LoanAmount")
plt.ylabel("ApplicantIncome")
plt.title("LoanAmount vs ApplicantIncome")
plt.show()

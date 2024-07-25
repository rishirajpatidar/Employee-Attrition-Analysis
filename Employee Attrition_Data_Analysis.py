#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[13]:


data = pd.read_csv(r"C:\Users\asus\Desktop\Attrition data.csv")


# In[14]:


data


# In[15]:


data.shape


# In[16]:


data.columns


# In[17]:


data.isnull().sum()


# In[18]:


data.describe()


# # Column Description
# Independent Variables were:
# 
# Age: Age of employees,
# 
# Department: Department of work,
# 
# Distance from home,
# 
# Education: 1-Below College; 2-College; 3-Bachelor; 4-Master; 5-Doctor;
# 
# Education Field
# 
# Environment Satisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
# 
# Job Satisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
# 
# Marital Status,
# 
# Monthly Income,
# 
# Num Companies Worked: Number of companies worked prior to IBM,
# 
# Work Life Balance: 1-Bad; 2-Good; 3-Better; 4-Best;
# 
# Years At Company: Current years of service in IBM
# 
# Dependent Variable was:
# 
# Attrition: Employee attrition status(0 or 1)

# In[19]:


#Top 5 values
data.head()


# In[20]:


#last 5 values
data.head()


# In[21]:


#If there is any duplicate values
data.duplicated()


# In[22]:


#Unique values of every columns
data.nunique()


# # Data Insights

# In the given dataset, we have two types of employee one who stayed and another who left the company.

# In[23]:


#Attrition
Attrition_Count = pd.DataFrame(data['Attrition'].value_counts())
Attrition_Count


# In[24]:


#Distribution of Attrition
plt.figure(figsize=(10,7))
plt.pie(Attrition_Count['Attrition'],labels=['Yes','No'], autopct='%1.1f%%', explode=(0.1,0))
plt.title('Attrition Count', fontsize=20)
plt.show()


# From above Data , we get to know that Attrition Rate is about 16.1% of the total Employees 

# In[25]:


data['Attrition'].value_counts().plot(kind='barh',color='blue', figsize=(8,5),fontsize=12)
plt.title('Employee Attriton',fontsize=20)
plt.xlabel('Count of people',fontsize=15)
plt.ylabel('Attrition',fontsize=15)
plt.show()


# 
# # Age and Attrition

# In[26]:


#Number of Unique values
data['Age'].nunique()


# In[27]:


#Histogram of Age Vs Attrition
plt.figure(figsize=(10,7))
data.hist(column='Age',grid=False,color='purple',edgecolor='black',bins=12)
plt.title('Age Vs Attrition', fontsize=20)
plt.xlabel('Age',fontsize=15)
plt.ylabel('Count of People',fontsize=15)
plt.show()


# Above Histogram shows that Attriton Rate in age range between 25 to 40 is higher

# In[28]:


#Barplot for age group vs Count of people
data['Age'].value_counts().plot(kind='bar',color='green',fontsize=15,figsize=(20,14))
plt.title('Age group Vs Count of People',fontsize=20)
plt.xlabel('Age Group',fontsize=15)
plt.ylabel('Count of People',fontsize=15)
plt.show()


# Maximum employees age lies in the range of 30 to 40

# In[29]:


ct= pd.crosstab(data.Age,columns = data.Attrition)
ct


# # what age group is more likely to leave?

# In[30]:


#Countplot Creation of Age group that is more likely to leave using MatplotLib and Seaborn
plt.figure(figsize=(15,4))
sns.countplot(x='Age',hue='Attrition',data=data, palette='twilight')
plt.title('Attrition based on Age Group', fontsize=20)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Attrition Count', fontsize=15)
plt.show()


# Above data shows that age group from 27 to 45 has highest Attrition Rate
# 
# Major Attrition occured among the mid-career level employees. Career change and career growth could be one of the possibilities for such an attrition levels.

# In[31]:


#boxplot for Age Vs Attrition

data.boxplot(column='Age', by='Attrition', vert=False)
plt.show()


# we can express that Age does not play a powerful role in influencing attrition but In the above plot we can see that affirmative attrition count is higher in late 20 and early 30s.

# # MonthlyIncome

# In[32]:


#Analysis based on monthly income
data.MonthlyIncome.describe()


# There are 4410 employees under our analysis for monthly income (in our sample)
# • Ordinal data(numerical)
# 
# • The employees in the organization are earning from 10090 To 19,9990.
# 
# • 25%(1st quartile) of the employees under our analysis in our sample are earning monthly salary less than or equal to 29110.
# 
# • 50%(median-2nd quartile) of the employees under our analysis in our sample are earning monthly salary less than or equal to 49190.
# 
# • 75%(3rd quartile) of the employees under our analysis in our sample are earning monthly salary less than or equal to 83800.
# 
# • The mean monthly income received by the employees are 65029.31

# In[33]:


data['MonthlyIncome'].nunique()


# In[34]:


#Distribution plot for Monthly Income
plt.figure(figsize=(10,7))
sns.distplot(data['MonthlyIncome'])
plt.show()


# This variable is left skewed distribution,meaning most of its values are located at the lower end(20000-60000)

# In[35]:


#Creating DataFrame has Attrition based data as 'Yes' and 'No' individual 
Y_data= data.loc[data['Attrition']=='Yes']
N_data= data.loc[data['Attrition']=='No']


# In[36]:


plt.figure(figsize=(15,9))
sns.distplot(Y_data['MonthlyIncome'], label=['Positive Direction'])
sns.distplot(N_data['MonthlyIncome'], label=['Negative Direction'])
plt.show()


# There is high attrition rate among employees of relatively lower salary range, ie. less than 50000.

# In[37]:


#Plotting CatPlot using seaborn and amtplotlib for Monthly Income vs Attrition 
sns.catplot(x='Attrition', y='MonthlyIncome',kind='box',  data=data)
plt.title('Monthly Income Based Attrition', fontsize=20)
plt.show()


# There is high attrition rate among employees of relatively lower salary range, ie. less than 50000.

# In[38]:


# Box graph for Marital Status vs Monthly Income
plt.figure(figsize=(20,10))
sns.catplot(x='MaritalStatus',y='MonthlyIncome',hue='Attrition', kind='boxen',data=data)
plt.title('Monthly Income based on Marital Status', fontsize=20)
plt.xlabel('Marital Status', fontsize=15)
plt.ylabel('Monthly Income', fontsize=15)
plt.show()


# This will show monthly income and attrition using Marital Status category

# In[39]:


#Scatterplot for Monthly Income vs Age
data.plot.scatter(x='Age',y='MonthlyIncome',color='brown')
plt.title('Monthly Income vs Age', fontsize=20)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Monthly Income', fontsize=15)
#plt.show()


# In[40]:


#Violinplot for Job Satisfaction based on the Monthly Income
sns.violinplot(x ="JobSatisfaction", y ="MonthlyIncome", hue ="Attrition",
data = data, split = True)
plt.show()


# # JobSatisfaction

# In[41]:


data.JobSatisfaction.describe()


# In[42]:


data['JobSatisfaction'].value_counts()


# There are 4390 employees under our analysis for Job Satisfaction (in our sample)
#  Nominal data(categorical)
# 
#  There are 4 categories in this data sample: 1.0,2.0,3.0 and 4.0
# 
#  Here, 1.0 corresponds to least Job Satisfaction and 4.0 corresponds to the highest Job Satisfaction.
# 
#  The count analysis of the Job Satisfaction category:  4 is 1367,  3 is 1323  2 is 840  1 is 860
# 
#  Highest rating is with ‘Job Satisfaction 4’ with a count of 1367.  Least rating is with ‘Job Satisfaction 2’ with a count of 840.

# # Here JobSatisfaction Counts are shown by Graph

# In[43]:


#Count plot for the JobSatisfaction
sns.countplot(data['JobSatisfaction'])
plt.xticks(rotation=90)
plt.show()


# In[44]:


plt.figure(figsize=(10,7))
labels=['4','3','1','2']
plt.pie(data.JobSatisfaction.value_counts(), labels=labels, autopct='%.1f%%')
plt.show()


# In[45]:


sns.relplot(x='JobSatisfaction',y='MonthlyIncome',hue='Attrition',kind='line',data=data)
plt.title('JobSatisfaction vs MonthlyIncome', fontsize=20)
plt.xlabel('Jobsatisfaction', fontsize=15)
plt.ylabel('MonthlyIncome', fontsize=15)
plt.show()


# # Department

# In[46]:


data.Department.describe()


# In[47]:


data['Department'].value_counts()


# • Nominal data(categorical)
# 
# • There are 3 categories in this data sample: Human Resources, Sales and Research & Development.
# 
# • The count of employees in these categories are: Human Resources = 189, Sales = 1338, Research and Development = 2883
# 
# 

# # Plot of different department

# In[48]:


plt.figure(figsize=(10,7))
labels = ['Research & Development', 'Sales', 'Human Resources']
plt.pie(data.Department.value_counts(), labels=labels, autopct='%.1f%%')
plt.show()


# In[49]:


t= pd.crosstab(data.Department,columns=data.Attrition)
t


# # Replace Attrition to numeric values

# In[50]:


data=data.replace('Yes',1)
data=data.replace('No',0)


# In[51]:


data.groupby('Department')['Attrition'].mean()


# In[52]:


sns.catplot(x="Department",y="Attrition" ,hue="MaritalStatus",kind="bar",data=data)   
plt.show()


# Employees in R&D department seem to have less attrition rate among other department employees, with higher attrition in both Human Resources and Sales Department.

# In[53]:


sns.catplot(x="Department",y="Attrition" ,col="MaritalStatus",kind="bar",data=data)   
plt.show()


# when drilled down by Marital status, Human Resourses singles seem to have almost 1.5 times more the attrition rate of Human Resourses married employees and twice to Human Resourses Divorced emolyees

# # Categorical plot between MonthlyIncome and Department and Attrition

# In[54]:


sns.catplot(x="Department",y="MonthlyIncome" ,hue="Attrition",kind="box",data=data)   
plt.show()


# Here shows less income employee from Research & Development has more Attrition

# In[55]:


sns.catplot(x="Department",y="Age" ,kind="box",data=data)   
plt.show()


# It shows relation between departments and age which normally distributed

# In[56]:


tab=pd.crosstab(data["Department"],data["Attrition"],normalize='index')*100

tab.plot(kind="bar")
plt.show()


print(tab)


# # Education Field

# In[57]:


#Number of Unique values
data["EducationField"].nunique()


# In[58]:


data["EducationField"].value_counts()


# • Nominal data(categorical)
# 
# • There are 6 categories in this data sample: Human Resources, Life sciences, Marketing, Medical, Other and Technical degree
# 
# • The count of employees from these educational backgrounds are: Human Resources = 81, Life Sciences = 1818, Marketing = 477, Medical = 1392, Technical Degree = 396, Other = 246
# 

# In[59]:


data["EducationField"].value_counts().plot(kind="barh",figsize=(8,4),fontsize=13)
plt.show()


# In[60]:


plt.figure(figsize=(10,7))
labels = ['Life Sciences', 'Medical', 'Marketing','Technical Degree','Other','Human Resources']
plt.pie(data.EducationField.value_counts(), labels=labels, autopct='%.1f%%')
plt.show()


# In[61]:


tab = pd.crosstab(data["WorkLifeBalance"],data["Attrition"],normalize='index')*100

tab.plot(kind='bar')
plt.show()


# People with work life balance of 1 have high attrition rate compared other
# Hence poor work life balance increases attrition.

# # Years At Company

# In[62]:


data.YearsAtCompany.describe()


# There are 1470 employees under our analysis for Years At Company (in our sample)
# • Ordinal data(numerical)
# 
# • Range of Years At Company is between 0 years to 40 years: This company has employees across the spectrum from zero years experience till employees with 40 years of experience.
# 
# • Mean years in company of employees in the data sample is 7.008
# 
# • 25%(1st quartile) of the employees under our analysis in our sample are of years less than or equal to 3 years. • 50%(median-2nd quartile) of the employees under our analysis in our sample are of years less than or equal to 5. It provides the years ‘midpoint’ of employees of organization; there are the same number of people who are have more years than the median years. • 75%(3rd quartile) of the employees under our analysis in our sample have Years At Company less than or equal to 9.
# 
# • At least 75% of the employees under our analysis in our sample have Years At Company between 5.24(mean-2sd) and 19.24(mean+2sd)
# 
# • The maximum number(mode) of employees with years in the company under our analysis in our sample is 5 years.
# 
# • The minimum number of employees of the years in the company under our analysis in our sample are of age 1. (4 in number)
# 
# • The mean is greater than the median, so the distribution of variable mean will have its tail towards the right side. This indicates that the sample is positively skewed.

# # Are Employees leaving after working for certain number years?

# In[63]:


data['YearsAtCompany'].value_counts().plot(kind='bar', figsize=(19,4), color="coral", fontsize=13)

plt.xlabel("Years At Company", fontsize=12)
plt.ylabel("Count of Employees", fontsize=12)
plt.show()


# In[64]:


plt.subplots (figsize=(22,8))
sns.countplot (x='YearsAtCompany',  hue='Attrition', data= data, palette = 'colorblind')
plt.show()


# Employees who have worked for less number of years tend to leave more.

# # Distance From Home

# In[65]:


data.DistanceFromHome.describe()


# There are 4410 employees under our analysis for ‘Distance from Home’ (in our sample). • Ordinal data(numerical)
# • Range of ‘Distance from Home’ is between 1 years to 29 years.
# 
# • Mean ‘Distance from Home’ of employees in the data sample is 9.19.

# In[66]:


data.hist(column="DistanceFromHome",
         grid=False,
         figsize=(6,4),
         color="indigo",
         edgecolor="black",
         bins=10)

plt.xlabel("Distance From Home",fontsize=12)
plt.ylabel("Frequency",fontsize=12)
plt.title(" Employee 'Distance From Home' Analysis ",fontsize=16)

plt.show()


# In[67]:


data['DistanceFromHome'].value_counts().plot(kind='bar', figsize=(10,6), color="coral", fontsize=13)

plt.xlabel("Distance From Home", fontsize=12)
plt.ylabel("Count of Employees", fontsize=12)
plt.title(" Employee 'Distance From Home' Analysis ", fontsize=16)
plt.show()


# This graph shows most of the employees prefer to live colser to their home.

# In[68]:


sns.boxplot(x = "DistanceFromHome",y= "Age",data = data, palette = "autumn_r")
plt.gcf().set_size_inches(8, 6)


# This box plot shows DistanceFromHome with respect to age.It does not show any difference so it is normally distributed.

# In[69]:


data.groupby(['Age','Attrition'])['DistanceFromHome'].size().unstack().plot(kind='bar', figsize=(12,6),stacked=True)
plt.show()


# # Relation plot between Monthly Income and Age by Marital status

# In[70]:


sns.relplot(x="MonthlyIncome",y="Age",hue="MaritalStatus",data=data)   
plt.show()   


# # Relation between employee's YearsAtCompany and their age with attrition

# In[71]:


sns.relplot(x="YearsAtCompany",y="Age",hue="Attrition",col="MaritalStatus",data=data) ##diffrnt colm with diffn class
plt.show()


# In[72]:


sns.pairplot(data, vars=["YearsAtCompany","Age","MonthlyIncome"])
plt.show()


# Here pair plot pairwise relationships in attrition dataset so that here all variables in attr will be plotted against each other variable in the dataset.

# # Corelation

# In[73]:


data.corr()


# In[74]:


plt.figure(figsize = (25,25))
sns.heatmap(data.corr(), annot=True)               ###heatmap
plt.show()


# Variables such as TotalWorkingYears, YearsAtCompany, YearsInCurrentRoleare highly corelated to each other.
# 
# This graph shows Pearson’s correlation values, and there is a presence of high correlations values among different sets of variables such as Monthly Income, Total Working Hours and many more.
# 
# 'Years at Company' and 'Monthly Imcome': 0.00099 -------> More experiece more salary
# 
# 'Age' and 'Monthly Income': -0.044 --------> old employees have more experience
# 
# 'Age' and 'Years at Company' : 0.31
# 
# 'Age' and 'Number of Companies Worked': 0.3
# 
# 'Work Life Balance', 'Job Satisfaction' and 'Environment Satisfaction' do not have strong correlation with other features

# # Findings after performing Analysis :-

# #### Based on Age:
# Range of age is between 18 years to 60 years: This company has employees across the spectrum from recent graduates to the retirement age. Since the maximum age bracket with highest number of employees are between 30 -36, we can safely assume that the company prefers employees who have considerable work experience.

# #### Based on Department:
# Since 65% of the employees are in Research and development, we can assume that the company activities include innovation and introducing new products and services. Ostensibly, the goal of the company would be to take new products and services to market and add to the company's bottom line.

# #### Based on Education Field:
# Since 41% and 31% of the employees are from the Life sciences and medical backgrounds respectively, we can say that the company is majorly based out of bio-technology and R&D. This further strengthens our earlier propositions.

# #### Based on Environment Satisfaction:
# Since more than 60% of the employees have voted for the top 2 categories in environment satisfaction, we can say that the majority of employees feel comfortable working in this organization. However, 40% of the employees seem to need improvement in their working environment.

# #### Based on Job Satisfaction:
# Only 30% of employees in the organization have given the highest rating for job satisfaction. This shows that there is still a lot of room for improvement.

# #### Based on Marital Status:
# As 45% of the employees in the organization are married, the company appears to give a stable and well-paying job profile to the employees. Marital status is also an important indicator of organisational commitment. Generally, married people are more committed to their organisation than unmarried people.

# #### Based on Monthly Income:
# It is negatively correlated to attrition. Lesser the Monthly Income, higher the attrition rate. Employees with salary around 2500 are more prone to leave the company.

# #### Based on WorkLifeBalance :
# 60% of employees have given second best rating. This could again hint at a 'neutral response bias' and it involves a certain subjectivity of interpreting a correct work-life balance.

# #### Based on Years At Company:
# The dataset reveals that a majority of the employees (75%) have a work experience of less than 9 years at the company. There appears to be a tapering down of career progression above 10 years. If the company can positively tackle this, it can greatly benefit the organisation.

# #### Based on Distance From Home:
# A large number of employees are residing close to the company (50% of the employees are at a distance of 7km). There is a possibility that accomodation facilities are provided by the company, since the maximum count of employees are at a distance of 2 km.

# # To reduce the attrition rate I would recommend:
# Offer support: Provide work-life balance programs and flexible work arrangements that help employees manage their workload and reduce overtime. Offer mentorship and coaching programs that support employees in their current roles and help them develop the skills required for future roles.
# 
# Encourage career growth: Provide career advancement opportunities, training programs, and mentorship to support employee progression to higher job levels.
# 
# Offer competitive compensation: Offer competitive salaries and benefits that align with the market standards and recognize and reward long-serving employees for their commitment to the organization.
# 
# Foster a positive work environment: Provide a positive and inclusive work environment that encourages employee engagement and job satisfaction.
# 
# Gather employee feedback: Conduct regular employee engagement surveys to understand the underlying reasons for employee turnover and take corrective actions accordingly.

# In[ ]:





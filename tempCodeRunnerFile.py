a=[7,1,5,3,6,4]
m_profit=0
mini=a[0]
profit=None
for i in range(1,len(a)):
    profit=a[i]-mini
    m_profit=max(m_profit,profit)
    mini=min(mini,a[i])
print(m_profit)

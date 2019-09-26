import numpy as np
import matplotlib.pyplot as plt

N = 4
menMeans = (20, 35, 30, 35)
#womenMeans = (25, 32, 34, 20)
#menStd = (2, 3, 4, 1, 2)
#womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.40       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width)

#p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

plt.ylabel('Days')
plt.title('Server uptime in days')
plt.xticks(ind, ('svr1', 'svr2', 'srv3', 'srv4'))
plt.yticks(np.arange(0, 81, 10))
#plt.legend(p1[0])
plt.savefig('serveruptimes.png')

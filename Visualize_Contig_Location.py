def locingene(longS, shortS, title):
    """Simple Graph of where contig falls in assembly"""
    #index of short string in long string
    index = []
    for match in re.finditer(shortS, longS):
        index.append([match.start(), match.end()])
    if index != []:
        #y array for graph
        y = np.ones(int(len(longS)/1000))
        #x array for graph
        x = np.arange(0,len(y))
        #plot of long assembly
        plt.plot(x,y,'o',color = 'red')
        #Substrings
        for i in range(0,len(index)):
#             print(index)
            y2 = np.ones(int((index[i][1]-index[i][0])/1000)+1)
            x2 = ((np.arange(index[i][0], index[i][1], 1000)))
            x2 = np.true_divide(x2,1000)
            plt.plot(x2,y2,'x', color = 'blue')
            plt.title(title)
        plt.show()
    else:
        #y array for graph
        y = np.ones(int(len(longS)/1000))
        #x array for graph
        x = np.arange(0,len(y))
        #plot of long assembly
        plt.plot(x,y,'o',color = 'black')
        
        x2 = ((np.arange(0.5*len(longS), len(shortS)+(0.5*len(longS)), 1000)))
        x2 = np.true_divide(x2,1000)
        y2 = np.ones(len(x2))
        plt.plot(x2,y2,'x', color = 'yellow', alpha = 0.05)
        plt.title("NOT FOUND: JUST A DEMO OF LENGTH OF CONTIG: " +title)
        plt.show()
#         return index

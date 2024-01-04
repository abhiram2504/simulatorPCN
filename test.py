import networkx as nx
import matplotlib.pyplot as plt


G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
plt.show()


#try to implement a traffic demand matrix. 
'''
Try to have cirulartion matrix. 
'''
#Can try to change the src, the probability of picking a src and dest is proportional to its capactiy. 

'''
Bitcoin lighting network. 
Etherum raeden network. 
'''


'''
Maximise, the success rate in a network, traffic demand. How do you do routing, to max thoughtput, min failtures, etc. 
We want to look at the same problem with a different lens, any benefit if coordinatino can bring to the system. We want to chekc weather
by the use of a randomess we can hope to provide a centralization. 
What is the Gap b/w decentralised adn centralised. 
Note:
Usually people just tried out random paths, after that people tried to send a probde around the path. 
'''
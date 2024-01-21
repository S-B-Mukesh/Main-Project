import os
import matplotlib.pyplot as plt
import numpy as np


for file in ["10-5"]:
    path = "C:/Users/Administrator/Desktop/Temp/New Graphs/"
    os.chdir(path=path)
    for i in ["c", "p", "r"]:
        os.mkdir(i)
        os.chdir(i)
        for j in range(0,6):
            os.mkdir(str(j))
            os.chdir(str(j))
            print(os.getcwd())
            for k in range(10):
                for pack in ["sent","Drop","reci"]:
                    run = int(file.split("-")[1])
                    t=dict()
                    for temp in range(20):
                        t[temp] = 0
                    p=open("C:/Users/Administrator/Desktop/10-5/Delay/"+i+"_Delay_0."+str(j)+"0","r")
                    for line in p:
                        parts = line.split()
                        if parts[2] =="_"+str(k)+"_":
                            if parts[0]==pack[0]:
                                temp=int(float(parts[1]))
                                if temp in t:
                                    t[temp] += 1
                    x = list(t.keys())
                    y = list(t.values())
                    f = plt.figure()
                    f.set_figwidth(15)
                    f.set_figheight(10)
                    plt.plot(x,y,label="Node "+str(k))
                    plt.xticks(x)
                    plt.yticks(y)
                    plt.title("Packets "+pack+" by node "+str(k)+" in "+i+" attack with malicious percent of "+str(j), fontdict={'fontsize': 25})
                    plt.xlabel("Simulation time", fontdict={'fontsize': 25}) 
                    plt.ylabel("No of Packets", fontdict={'fontsize': 25})
                    ax = plt.subplot()
                    ax.tick_params(axis='x', labelsize=30)
                    ax.tick_params(axis='y', labelsize=30)
                    plt.legend()
                    plt.savefig(pack+"-"+str(k))
                    plt.close()
            os.chdir("..")
        os.chdir("..")
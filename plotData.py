#!/usr/bin/python
# coding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
 
def printOutHelp():
  print ("python plotData.py [<filename>]")
  print ("example: python plotdata.py xx.txt")
  print ("example: cat xx.txt | python plotdata.py")
  print ("expected format of file:")
  print ("<pos>,<velo>,<acc>")

def main():
  pos = np.array([])
  velo = np.array([]) 
  acc = np.array([]) 
  time = np.array([])
  currTime = 0
  timeStep=0.001

  # Check args
  if len(sys.argv)>1:
    print(sys.argv[1] )
    pos1=sys.argv[1].find('-h')
    if(pos1>=0):
      printOutHelp()
      sys.exit()
  
  if len(sys.argv)!=2 and len(sys.argv)>1:  
      printOutHelp()
      sys.exit()
  
  if len(sys.argv)==2:
    fname=sys.argv[1]
    dataFile=open(fname,'r')

  if len(sys.argv)==1:
    fname=""
    dataFile=sys.stdin;

  for line in dataFile:
    print(line)
    # Ensure 2 ","
    if line.count(",") !=2:
      continue

    splittedLine=line.split(',')
    print(splittedLine)

    pos=np.append(pos,float(splittedLine[0]))
    velo=np.append(velo,float(splittedLine[1]))
    acc=np.append(acc,float(splittedLine[2]))
    currTime = currTime + timeStep
    time=np.append(time,currTime)
  plt.subplot(3,1,1) 
  plt.plot(time,pos,'b')  
  plt.grid()
  plt.legend('Pos')
  plt.xlabel("time")
  plt.subplot(3,1,2) 
  plt.plot(time,velo,'r')
  plt.grid()
  plt.legend('Velo')
  plt.xlabel("time")
  plt.subplot(3,1,3) 
  plt.plot(time,acc,'g')
  plt.grid()
  plt.legend('Acc')
  plt.xlabel("time")
  
  plt.title(fname)
  
  plt.show()
  
if __name__ == "__main__":
  main()

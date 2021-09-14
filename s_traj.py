from enum import Enum






# Motion profile start values
posStart=100
posTarget=150
veloMax=10
accMax=5
decMax=8
jerk=3


# defs
class sCurveState(Enum):
  STANDSTILL  = 0
  ACC_1       = 1
  ACC_STEADY  = 2
  ACC_2       = 3
  VELO_STEADY = 4
  DEC_1       = 5
  DEC_STEADY  = 6
  DEC_2       = 7

# Init
timeStep=0.001
posCurr=posStart
veloCurr=0
accCurr=0
accStep=jerk*timeStep
stateCurr=sCurveState.STANDSTILL


def CalcPreps():
  print("Executing preps at configuration time")


def getNextPosition():
  global stateCurr
  global posCurr, veloCurr, accCurr, posCurr, accMax, decMax, jerk, veloMax


  if(stateCurr == sCurveState.STANDSTILL):
    print("STANDSTILL")
    stateCurr = sCurveState.ACC_1
  
  if(stateCurr == sCurveState.ACC_1):
    print("ACC_1")

    if accCurr < accMax:
      accCurr = accCurr + accStep
      if accCurr > accMax:
        accCurr = accMax
    veloCurr = veloCurr + accCurr*timeStep    
    posCurr = posCurr + veloCurr*timeStep
    return posCurr, veloCurr, accCurr

  if(stateCurr == sCurveState.ACC_STEADY):
    print("ACC_STEADY")

  if(stateCurr == sCurveState.ACC_2):
    print("ACC_2")

  if(stateCurr == sCurveState.VELO_STEADY):
    print("VELO_STEADY")

  if(stateCurr == sCurveState.DEC_1):
    print("DEC_1")

  if(stateCurr == sCurveState.DEC_STEADY):
    print("DEC_STEADY")

  if(stateCurr == sCurveState.DEC_2):
    print("DEC_2")

if __name__ == "__main__":

  for x in range(4000):
    CalcPreps()
    [pos, velo, acc] = getNextPosition()
    print( str(pos) + "," + str(velo) + "," + str(acc) )

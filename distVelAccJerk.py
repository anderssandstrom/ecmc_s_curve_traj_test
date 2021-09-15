

# Motion profile start values
p0=100
v0=0
a0=0

posTarget=150
veloMax=10
accMax=5
decMax=8
jerk=3

def veloAtAccZero(v,a,j):
  # when is acc 0 if jerk -3
  a0=a
  a=0
  t=-a0/j
  # What is then velo?
  v0=v
  v=v0+a0*t+1/2*j*tt  
  return v

if __name__ == "__main__":
  # Jerk 3
  for time in range(1500):
    j=3
    t=time/1000
    tt=t*t
    ttt=tt*t
    p=p0+v0*t+0.5*a0*tt+1/6*j*ttt
    v=v0+a0*t+1/2*j*tt
    a=a0+j*t
    print( str(p) + "," + str(v) + "," + str(a) )
  
  # Calc what velo will be att 0 acc (constant velo)
  resVelo=veloAtAccZero(v,a,-3)

  p0=p
  v0=v
  a0=a

  # Jerk -3
  for time in range(1,1500):
    j=-3
    t=time/1000
    tt=t*t
    ttt=tt*t
    p=p0+v0*t+0.5*a0*tt+1/6*j*ttt
    v=v0+a0*t+1/2*j*tt
    a=a0+j*t
    print( str(p) + "," + str(v) + "," + str(a) )

  print("Calculated velo at acc 0 is: " + str(resVelo))






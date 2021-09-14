# ecmc_s_curve_traj_test

```

python s_traj.py  | python plotDataPosDiff.py &

```












# Some notes..

freq=1000
accMax = 1
decMax = 1
jerk = 1

distToConstSpeed=0
distdAccAccumalated=0
distToStop=0



Case:
0: stop
  distToConstSpeed=0
1: accScurve1

2: accSteady
3: accScurve2
4: velsteady
   distToConstSpeed=0
5: decScurve1
6: decSteady
7: decScurve2



j(t)=dp3/dt3

j(t)²/2+k1=dp^2/dt2











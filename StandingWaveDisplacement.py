import sys
import math

def is_valid(x):
    return isinstance(x, (int, float)) and (x != 0)
def standing(waveVelocity, transverseVelocity, transverseVelocityMax, period, tension, linearDensity, omega, waveLength, phaseConstant, amplitude, initialTransversePosition, transversePosition, time, position, k):
    """ """
    # omega and wave velocity are given
    if is_valid(omega):
        period = (2*math.pi)/omega
    if is_valid(k):
        waveLength = (2*math.pi)/k
    if is_valid(period):
        omega = (2*math.pi)/period
    if is_valid(omega) and is_valid(k):
        waveVelocity = omega/k
    if  is_valid(waveVelocity) and is_valid(omega):
        k = omega/waveVelocity 
        waveLength = (2*math.pi)/k
        period = (2*math.pi)/omega
    # wave velocity and wave length are given
    if is_valid(waveVelocity) and is_valid(waveLength):
        k = (2*math.pi)/waveLength
        omega = waveVelocity * k
        period = (2*math.pi)/omega
    # wave velocity and period are given
    if is_valid(waveVelocity) and is_valid(period):
        k = (2*math.pi)/(waveVelocity*period)
        omega = waveVelocity * k
        waveLength = (2*math.pi)/k
    # k and period are given
    if is_valid(k) and is_valid(period):
        waveLength = (2*math.pi)/k
        omega = (2*math.pi)/(period)
        waveVelocity = waveLength/period
    if  is_valid(waveVelocity) and is_valid(k):
        omega = waveVelocity * k
        waveLength = (2*math.pi)/k
        period = (2*math.pi)/omega
    # amplitude and initial transverse position are given
    if is_valid(amplitude) and is_valid(initialTransversePosition):
        phaseConstant = math.asin(initialTransversePosition/amplitude)
    # amplitude and phase constant are given
    if is_valid(amplitude) and is_valid(phaseConstant):
        initialTransversePosition = amplitude * math.sin(phaseConstant)
    # maximum transverse velocity is given
    if is_valid(transverseVelocityMax):
        amplitude = transverseVelocityMax/omega
    # tension is given
    if is_valid(tension):
        linearDensity = tension/(waveVelocity ** 2)
    # linear density is given
    if is_valid(linearDensity):
        tension = (waveVelocity ** 2)* linearDensity
    transversePosition = amplitude * math.sin(k*position - omega * time +phaseConstant )
    transverseVelocity = (-1) * amplitude * omega * math.cos(k*position - omega * time +phaseConstant )
    return waveVelocity, transverseVelocity, transverseVelocityMax, period, tension, linearDensity, omega, waveLength, phaseConstant, amplitude, initialTransversePosition, transversePosition, time, xposition, k

initialTransversePosition = float(input("Input your initial transverse position if you have it, otherwise 0: "))
waveVelocity = float(input("Input your wave velocity if you have it, otherwise 0: "))
transverseVelocity = float(input("Input your transverse velocity if you have it, otherwise 0: "))
transverseVelocityMax = float(input("Input your max transverse velocity if you have it, otherwise 0: "))
period = float(input("Input your period if you have it, otherwise 0: "))
tension = float(input("Input your tension if you have it, otherwise 0: "))
linearDensity = float(input("Input your linear density if you have it, otherwise 0: "))
omega = float(input("Input your omega if you have it, otherwise 0: "))
waveLength = float(input("Input your wave length if you have it, otherwise 0: "))
phaseConstant = float(input("Input your phase constant if you have it, otherwise 0: "))
amplitude = float(input("Input your amplitude if you have it, otherwise 0: "))
transversePosition = float(input("Input a given transverse position if you have it, otherwise 0: "))
xposition = float(input("Input the x position value for your given transverse position if you have it, otherwise 0: "))
time = float(input("Input the time value for your given transverse position if you have it, otherwise 0: "))
k = float(input("Input your k if you have it, otherwise 0: "))
waveVelocity, transverseVelocity, transverseVelocityMax, period, tension, linearDensity, omega, waveLength, phaseConstant, amplitude, initialTransversePosition, transversePosition, time, xposition, k = standing(waveVelocity, transverseVelocity, transverseVelocityMax, period, tension, linearDensity, omega, waveLength, phaseConstant, amplitude, initialTransversePosition, transversePosition, time, xposition, k)
print (f"""
Transverse Position Equation: D(x,t) = ({amplitude})*sin({k}x - {omega}t + {phaseConstant})
Transverse Velocity Equation: v(x, t) = -({amplitude})*({omega})*cos({k}x - {omega}t + {phaseConstant})
Initial Transverse Position: {initialTransversePosition}
Wave Velocity: {waveVelocity}
Transverse Velocity: {transverseVelocity}
Maximum Transverse Velocity: {transverseVelocityMax}
Period: {period}
Tension of String: {tension}
Linear Density: {linearDensity}
Omega: {omega}
Wave Length: {waveLength}
Phase Constant: {phaseConstant}          
Amplitude: {amplitude}          
k: {k}
          """)


debug = 1
size = 512
sizep=256
knownbits= 134
N=14086160291425342283520344380411983364812792954622400251334758082442316624175006850950987254617679940795136231914925367368535278968830499182004816257654049

#we need to define an polynomial == 0 (mod p) that gives us the missing part (x)
# f_p(x) = x*2**(knownbits/2) + p_msb + p_lsb
# it's not monic so we need to divide by 2**(knownbits/2)
# set R = 2**(knownbits/2) and invert it modulo N

R = 2**(knownbits/2)
invR = inverse_mod(R,N)
p_msb = 251000163339563476196 << (sizep-knownbits/2-1)
p_lsb=int('2567fcb8c35e6dc63',16)
#setup coppersmith
F.<x> = PolynomialRing(Zmod(N))
#define the poly in x modulo p
f = x + (p_msb+p_lsb)*invR
#solve it
x0 = f.small_roots(X=2^(sizep-knownbits)-1, beta=0.44, epsilon=1/64)[0]

 

print ("reconstructed p: {:x}".format(Integer(x0*R)+p_msb+p_lsb))


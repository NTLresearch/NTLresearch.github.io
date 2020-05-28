import pandas as pd
import numpy as np
from scipy.stats import norm

def BlackScholes(S,K,r,sigma,T,type):
    if S<=0:
        print('Stock Price should greater than 0')
        return None
    else:
        d1 = (np.log(S/K)+(r+sigma**2/2)*(T))/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        N_d1 = norm.cdf(d1); N_d1m = norm.cdf(-d1)
        N_d2 = norm.cdf(d2); N_d2m = norm.cdf(-d2)
        if type == "Call": 
            price = N_d1*S - N_d2*K*np.exp(-r*T)
        elif type == "Put":
             price = N_d2m*K*np.exp(-r*T) - N_d1m*S
        else: price = None;
    return(price)

# Test
call_bs = BlackScholes(100,100,0.05,0.2,1,"Call")
put_bs = BlackScholes(100,100,0.05,0.2,1,"Put")



def Bachelier(S,K,r,sigmaS,T,type):
    if S<=0:
        print('Stock Price should greater than 0')
        return None
    else:
        d1 = (S-K)/(sigmaS*np.sqrt(T))
        N_d1 = norm.cdf(d1); N_d1m = norm.cdf(-d1)

    if type == "Call":
        price = (S-K)*N_d1 + sigmaS*np.sqrt(T)*norm.pdf(d1)
    elif type == "Put":
        price = (K-S)*N_d1m + sigmaS*np.sqrt(T)*norm.pdf(d1)
    else:
        price = None
    return(price)

# Test
call_bach = Bachelier(100,100,0.05,0.2*100,1,"Call")
put_bach = Bachelier(100,100,0.05,0.2*100,1,"Put")



def BachelierMod(S,K,r,sigmaS,T,type):
    if S <= 0:
        print('Stock Price should greater than 0')
        return None
    else:
        d1 = (S-K)/(sigmaS*np.sqrt(T))
        N_d1 = norm.cdf(d1); N_d1m = norm.cdf(-d1)

    if type == "Call":
        price = S*N_d1 - K*np.exp(-r*T)*N_d1 + sigmaS*np.sqrt(T)*norm.pdf(d1)
    elif type == "Put":
        price = K*np.exp(-r*T)*N_d1m - S*N_d1m + sigmaS*np.sqrt(T)*norm.pdf(d1)
    else:
        price = None
    return(price)


call_BaMod = BachelierMod(100,100,0.05,0.2*100,1,"Call")
put_BaMod = BachelierMod(100,100,0.05,0.2*100,1,"Put")


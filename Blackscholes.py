import numpy as np
import math
from datetime import date
from scipy.stats import norm


#Stock price
s = float(value here)

#Strike Price
k = float(value here)

#time to expiratiopn
t = (date(year, month, day) - date.today()).days

#risk free rate
rf = put risk free rate here

#volatility
v = put current volatility here




    

def black_scholes(stock_price, strike_price, riskless_rate, vol, ttm, call_or_put):
    """
    Parameters
    ----------
    stock_price : The underlying price at t = 0
    strike_price : The strike price of the contract
    riskless_rate : The risk-free rate
    vol : The volatility of the stock. This is assumed to be constant by the model, but not realistic
    ttm : Time to maturity. The date of the maturity minus the initial date of entering in the position
    call_or_put : Positive 1 to indicate a call, negative 1 for a put

    Returns
    -------
    bsm_price : Returns the fair value for a vanilla European Call/Put option under the assumptions
        of the no dividend BSM model.

    """
    d_1 = (np.log(stock_price/strike_price) + (riskless_rate + ((pow(vol,2)/2))) * ttm) / (vol * math.sqrt(ttm))
    
    d_2 = d_1 - vol * math.sqrt(ttm)
    
    bsm_price = call_or_put * (stock_price * norm.cdf(call_or_put * d_1) - strike_price * math.exp(-1 * riskless_rate * ttm) * norm.cdf(call_or_put * d_2))
    
    return bsm_price



price_bsm = black_scholes(s, k, rf, v, t, 1)


print(price_bsm)

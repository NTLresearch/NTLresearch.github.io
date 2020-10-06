---
layout: post
title:  "Fundamental theorem of derivatives trading"
date:   2018-10-10 +0200
categories: Pricing
usemathjax: true
---

Fundamental theorem of derivatives trading by Jesper Andreasen

Assume zero rates and zero dividends
Assume standard frictionless markets
Assume the underlying stock evolves continuously

There exists two stochastic processes 

$$ \mu, \sigma $$
such that

$$ \frac{dS(t)}{S(t)} = \mu(t)dt + \sigma(t)dW(t)$$

under measure

$$\text{real measure } P$$

let V be the value of an option book S priced on a model with constant volatility 

$$ \bar{\sigma} $$

Assume the book is delta hedged, we dynamically trade the stock to keep

$$ V_S = 0 $$

### Theorem 1: 

### Technical:
The value of option book evolves according:

$$ dV(t) = \frac{1}{2} (\sigma(t)^2 - \bar{\sigma}^2)S(t)^2V_{SS}(t)dt $$

**Proof:**

as interest rate is zero, and $$ V_S $$ is kept constant then

$$ dV = 0 $$ 

$$ V_SdS = 0 $$

then we have 

$$ dV = V_tdt + V_SdS + \frac{1}{2}V_{SS}(dS)^2 = V_tdt + \frac{1}{2}V_{SS} \sigma^2 S^2dt $$

and finally we have

$$ dV = V_tdt + \frac{1}{2}V_{ss}(dS)^2 = 0 $$


Looking at the equation above, we see that 
- If we are gamma long, $$ V_{SS} > 0 $$ and the realized volatility is higher, we  will make profit
- The option trader's job is really about balancing realized against implied volatility
  - realized volatility > implied volatility : go long gamma
  - realized volatility < implied volatility: go short gamma
- In Black-Scholes context, we can see theorem 1 as an investigation of the self financing condition

### Application:
- Black-Scholes implied volatility has to satisfy:

$$E^Q[\frac{1}{2} \int_{0}^{T} (\sigma(u)^2 - \bar{\sigma}_{impled})S(u)^2V_{SS}(u)du] = 0  $$

- Implied volatility is a weighted average of Q expected volatility
- Consider an option seller that delta hedges his short option position with short gamma:

$$ V_{SS} < 0 $$


$$ V(T) - V(0) = \frac{1}{2} \int_{0}^{T}(\sigma(t)^2 - \bar{\sigma}_{impled})S(t)^2V_{SS}(t)dt $$

- His total profit will be positive only if most of the time, the below holds:

$$ \bar{\sigma}_{implied} > \sigma(t) $$

- Assuming the option trader is risk averse, so to short gamma, the implied volatility when writing a short position, we expect that:

$$ \text{implied volatility} > \text{historical volatility} $$

- We can understand the gap between implied volatility and historical volatility as premium to underwrite the option, not an arbitrage opportunity




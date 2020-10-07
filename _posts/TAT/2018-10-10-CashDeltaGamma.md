---
layout: post
title:  "Greeks: Cash Delta and Gamma"
date:   2018-10-10 +0200
categories: Pricing
usemathjax: true
---

>Why do we need delta and gamma cash?

>Because traders think in percentage movements rather than absolute movements.


### 1. Delta Cash

Assuming there is no convexity from the option position

$$\delta_{cash} = \delta . S_t $$

The profit for 1% move in spot is:

$$\delta_{cash/1 \%} = \frac{\delta . S_t}{100} $$

Assuming a trader shorts 100,000 1 year call options on VIC with price of 25 with delta of 0.5. 

The cash delta is equal to:

$$  -0.5 \times 100,000 \times 25 = 1,250,000 $$

The 1% cash delta in this case is equal to:

$$\delta_{cash/1 \%} = \frac{-0.5\times100,000\times25}{100} = -12,500 $$

So when VIC stock increases by 1%, the trader loses -12,500. To fully hedge the position, he needs to buy the number of stock as below:

$$ \frac{-1,250,000}{25} = 50,000 $$

### 2. Gamma Cash

Assuming now there is some convexity in the option position.

The gamma is equal to $$ \gamma $$. Gamma cash is defined as the change in delta cash for a 1% move in the underlying. We have the formula for gamma cash:

$$ \gamma_{cash} = \frac{\gamma S_t^2}{100} $$

Note that the new delta cash after 1% move from spot is defined as:

$$ (\delta + \frac{\gamma S_t}{100})S_t $$

Continue with the example above, now assuming we have 1% gamma cash of 50,000 from the short option position (remember that when we short option, we short gamma, so the sign will be negative). When price move up by 1%, the delta cash after the increase will be:

$$ \delta S_t + \frac{\gamma S_t^2}{100} = -0.5\times 25 \times 100,000 - 50,000 = -1,300,000$$

Assuming the trader wants to delta-hedge the option position after 1% move, he will need to long total:

$$ \frac{-1,300,000}{25}=  52,000 $$

To maintain the portfolio delta-neutral, in this case, the trader needs to buy extra 2,000 shares.
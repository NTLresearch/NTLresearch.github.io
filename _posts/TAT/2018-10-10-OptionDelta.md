---
layout: post
title:  "Greeks: Option Delta"
date:   2018-10-10 20:27:22 +0200
categories: Pricing
usemathjax: true
---
### 1. Plain Vanilla Option

Option notations:

| Option Type  | Description     |
|------------|--------------------|
| Long Call  | Option to buy      |
| Short Call | Obligation to sell |
| Long Put   | Option to sell     |
| Short Put  | Obligation to buy  |

Delta Hedging:

- Short call hedged by long stock
- Short put hedged by short stock

Black Scholes notations:

$$\text{Call Delta} = N(d_1)$$
$$\text{Call Probability ITM} = N(d_2)$$

$$\text{Put Delta} = N(d_2) = N(d_1) - 1$$
$$\text{Put Probability ITM} = 1 - N(d_2)$$

- A call can have infinite payoff, then:

$$ \text{Call Delta}  > \text{Probability call ends up ITM} $$

- A put has maximum payoff capped at strike, then:

$$ \text{abs(Put Delta)} < \text{Probability put ends up ITM} $$



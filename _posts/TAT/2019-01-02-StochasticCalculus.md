---
layout: post
title:  "Note for stochastic calculus for derivatives pricing"
date:   2019-01-02
categories: TAT
usemathjax: true
---
##  Call price hedging setup by Merton

Stock price follows a geometric Brownian motion: 

$$
\begin{equation}

dS = \mu S d_t + \sigma S dz

\end{equation}
$$

Using Ito's lemma, call price must satisfy the PDE function:


$$ dc = \bigg( \frac{\partial c}{\partial t} + \frac{\partial c}{\partial S} \mu S + \frac{1}{2} \frac{\partial^2 c}{\partial S^2} \sigma^2 S^2 \bigg)dt + \frac{\partial c}{\partial S} \sigma S dz $$

Value of the portfolio with delta hedging (short 1 option and long $$ \displaystyle\frac{\partial c}{\partial S}$$ derivatives or vice versa):

$$
V = -c + \displaystyle\frac{\partial c}{\partial S} S
$$

The change of the portfolio value: 

$$
dV = -dc + \displaystyle\frac{\partial c}{\partial S} dS
$$

Replace the change in the portfolio value into the PDE we have:

$$
dV = - \bigg( \frac{\partial c}{\partial t} + \frac{\partial c}{\partial S} \mu S + \frac{1}{2} \frac{\partial^2 c}{\partial S^2} \sigma^2 S^2 \bigg)dt - \frac{\partial c}{\partial S} \sigma S dz + \frac{\partial c}{\partial S} (\mu S dt + \sigma S dz)

$$

$$
= - \frac{\partial c}{\partial t} dt - \frac{1}{2} \frac{\partial^2 c}{\partial S^2}\sigma^2 S^2 dt
$$

This portfolio does not include the stochastic/Brownian component, it should earn the risk free rate:

$$
dV = rVdt = r \bigg(-c + \frac{\partial c}{\partial S} S \bigg) dt = - \frac{\partial c}{\partial t} dt - \frac{1}{2} \frac{\partial^2 c}{\partial S^2}\sigma^2 S^2 dt
$$

Re-arrange the equation, we have:

$$

\frac{\partial c}{\partial t} + \frac{\partial c}{\partial S} S + \frac{1}{2} \frac{\partial^2 c}{\partial S^2}\sigma^2 S^2 = rc

$$

Based on this PDE, we transform and solve the heat equation using boundary conditions. The result is Black-Scholes equation for option pricing. Put price is derived using put-call parity

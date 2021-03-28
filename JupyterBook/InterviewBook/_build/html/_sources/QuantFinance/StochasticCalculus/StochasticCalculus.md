# Stochastic Calculus
## Brownian Motion

**Question:** What is $P(W_1W_{1+t} \ge 0)$, where $W_1$ is a standard Brownian motion?
<details>
  - <summary>Answer: </summary> 

Decompose $W_{1+t}$ into $W_1 + B_t$ where $B_t$ is an incremental Brownian motion independent from $W_1$, then:
\begin{align}
		P(W_1W_{1+t} \ge 0) &= P(W_1(W_1 + B_t) \ge 0)\\
		&= P(W_1 \ge 0, W_1 + B_t \ge 0) + P(W_1 \le 0, W_1 + B_t \le 0) \\
		&= 2P(W_1 \ge 0, W_1 + B_t \ge 0)\\
		&= 2P\left(W_1 \ge 0, Z \equiv \frac{B_t}{\sqrt{t}} \ge -\frac{W_1}{\sqrt{t}}\right)
	\end{align}
Now, draw a coordinate system with $W_1$ and $Z$, which are i.i.d. standard normal. The final answer is (need to check):
\begin{align}
		2\left(\frac14 + \frac{\arctan(1/\sqrt{t})}{2\pi}\right)
\end{align}
</details>
<br>

**Question:** Prove that $\EEE[B_t^{2k}] = \frac{(2k)!}{2^k\dot k!} t^k$, where $B_t$ is a Brownian motion. (Black Book, page 42)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:** What are the distributions, respectively, of the minimum and maximum of a Brownian motion in a given time frame $[0,t]$ (Green Book, page 132)
<br>

**Question:** If $W_t$ is a Wiener process, what are:
- $\EEE[W_tW_s]$ (150 Book, page 32)
- $\EEE[e^{W_t}]$ (150 Book, page 33)
- $\EEE[\Phi(W_t)]$ (Black Book, page 41)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>


## Brownian Bridge
**Question:**  	What is a Brownian bridge? What is the distribution of a Brownian Bridge? Why and how do we use it? (Black Book, page 42)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	$M_t$ is a stochastic process where $t \in [0,1]$ and $M_0 = 0, M_1 = \pm 1$. How to construct such a process? What if you know $M_t$ is a martingale?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

## Martingales: Stopping Time and Passage Time
**Question:**  	What is a martingale? What is the martingale representation theorem? How is it related to option pricing?
	(150 Book, page 32 and 34)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  Are martingales Markovian? Are Markov processes martingales? Explain.
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

Question:  	If $W_t$ is a Wiener process, check if the following processes are martingales.
- $W_t^2$ (150 Book, page 33)
- $W_t^3 + 3tW_t$ (Barclays)		
- $W_t^3 - 3tW_t$ (150 Book, page 34)
- $X^\alpha$ where $dX = \mu X dt + \sigma X dW$
- $B_t + 8t$, $B_t^3$, $B_t^2$, and $t^2B_t - 2\int_0^t sB_sds$ (Black Book, page 42)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	What is Girsanov's Theorem?	(150 Book, page 34)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	What is the mean of the stopping time $T$ for a Brownian motion to reach either the upper level $U$ or the below level $-B$? Follow-up question: One man at 17 meter of a 100-meter-long bridge. He has 50\% going one meter forward or backward. What is the probability he makes it to the end of the end of the bridge (the 100-meter end) before he reaches the other end (the 0-meter end)? What is the expected number of steps he takes to reach either end?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  What is the pdf of the stopping time $T_x$ for a Brownian motion to reach either the upper level $x$?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  Suppose $dX_t = rdt + dW_t$, what is the probability that $X_t$ hits 3 before hitting -5?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

## Ito's Lemma and Stochastic Calculus
**Question:**  What is an Ito process?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  What is Ito's Lemma?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Explain the assumption $(dW_t)^2 = dt$ used in the informal derivation of Ito's Lemma.
	(150 Book, page 32)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	What are the rules of stochastic calculus?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	If $W_t$ is a Wiener process. For the following Ito integrals, are they martingale? Find their expectations and variances.
	\begin{align*}
	&\int_0^t W_s ds, \int_0^t W_s dW_s, \int_0^t s dW_s, ~~ \mbox{and}\\
	&\int_0^t W_s^2 dW_s, \int_0^t \sqrt{s}e^{\frac{W_s^2}{8}}dW_s.
	\end{align*}		
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Compute the following quantities:
	- What is $\EEE[\int_0^t f(s) d W_1(s) \int_0^t g(s) d W_2(s)]$, where $d W_1 d W_2 = \rho d t$?
	- $E(B_t^3|B_s), ~ t > s$  (Barclays)	
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	For each of the processes $X_t$ below find the process $a(s,\omega)$ such that $$X_t = \EEE[X_t] + \int_0^t a dB_s.$$
	$X_t = B_t^2, e^{B_t}, B_t^3, sinB_t$.
	(Black Book, page 41)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

## Geometric Brownian Motion

**Question:**  	What is a Geometric Brownian Motion (GBM)? Solve it.
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>


**Question:**  Show that if $X_t$ and $Y_t$ are both geometric Brownian motions with correlation $\rho$, then $Z_t = X_t / Y_t$ is also a geometric Brownian motion and determine its drift and volatility coefficients.
	(150 Book 2nd Edition, page 3)
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

## Stochastic Differential Equations

**Question:**  	What is Feynman–Kac Formula?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Solve the following SDE:
	\begin{align*}
	\begin{cases}
		dY_t &= \mu Y_t dt + \sigma Y_t dW_t\\
		\\
		dX_t &= \mu dt + (aX_t + b) dW_t
	\end{cases}
	\end{align*}
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Solve the following SDE: 
\begin{align*}
dX_t = X_t dW_t.
\end{align*}
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  Suppose $W(t)$ is the standard Brownian motion and $y(t)$ satisfies the SDE
\begin{align*}
	dy(t) &= -cy(t)dt + \sigma dW(t),\\
	y(0) &= x,
\end{align*}
where $C > 0$ and $\sigma$ are constants. Find the mean and variance of $y(t)$.
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Consider the stock price process $dS(t) = \sigma dW(t)$ with initial level $S(0)$. Consider the average stock price process $A(T) = \frac1T \int_0^T S(t) dt$. What is the distribution of $A(T)$?
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Consider the stock price process $dS(t) = \sigma dW(t)$. Assume that the initial level is $S(0)$, and there is a barrier at $H > S(0)$.
	- What is the probability that the barrier is breached between now and $T$? Express your answer in terms of the normal distribution.
	- Let $b$ denote the first time the process breaches the barrier at $H$. What is the density function of $b$?	
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Solve the Bachelier model:
	\begin{equation}
	dS(t) = (r-q)S(t)dt + \sigma dW(t)
	\end{equation}
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  	Solve the Ornstein-Uhlenbeck process
\begin{equation}
	dr_t = \lambda(\theta - r_t)dt + \sigma dW_t
\end{equation}
which is used, e.g., in the Vasicek model for interest rates.
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>

**Question:**  Solve $dr_t = a(b-r_t)dt + \sigma dW_t.$ Since the interest rate $r_t$ must not be negative, this is not a good model. Why the following well-known CIR model fixes this problem? Solve it and find its distribution: $dr_t = a(b-r_t)dt + \sigma \sqrt{r_t}dW_t$ Hint: the distribution of $\sqrt{r_t}$ is easy.
<details>
<summary>Answer: </summary> 

TBD.
</details>
<br>
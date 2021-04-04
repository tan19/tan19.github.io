# Portfolio Management

## LOS 40.a: Describe the portfolio approach to investing.
Modern portfolio theory concludes that the extra risk from holding only a single security is not rewarded with higher expected investment returns. Conversely, diversification allows an investor to reduce portfolio risk without necessarily reducing the portfolio's expected return. In the early 1950s, the research of Professor Harry Markowitz concluded that: <span style="color:red">**unless the returns of the risky assets are perfectly positively correlated, risk *can* be reduced by diversifying across assets.**</span>

### Two Risky Assets
Suppose our portfolio $P$ consists of $w$ shares of security $X$ and $y$ shares of security $Y$:
\begin{align}
    P \equiv wX + (1-w)Y
\end{align}
then,
\begin{align}
\mu_P &= w\mu_X + (1-w)\mu_Y\\
\sigma_P^2 &= w^2 \sigma_X^2 + (1-w)^2 \sigma_Y^2 + 2w(1-w) \rho \sigma_X\sigma_Y
\end{align}
Taking the derivative w.r.t. $w$ (assume the variances and covariance are independent from $w$) we obtain
\begin{align}
2w \sigma_X^2 - 2(1-w) \sigma_Y^2 + 2(1-2w) \rho \sigma_X\sigma_Y = 0
\end{align}
which implies that the minimum variance is obtained when
\begin{align}
\hat{w} &= \frac{\sigma_Y^2 - \rho \sigma_X\sigma_Y}{\sigma_X^2 - 2\rho \sigma_X\sigma_Y + \sigma_Y^2} \not \in \{0, 1\}, ~~~ \rho \ne 1\\
\hat\mu &= \mu_Y + \frac{\sigma_Y^2 - \rho \sigma_X\sigma_Y}{\sigma_X^2 - 2\rho \sigma_X\sigma_Y + \sigma_Y^2}(\mu_X - \mu_Y)\\
\hat{\sigma}^2 &= \frac{\sigma_X^2\sigma_Y^2(1-\rho^2)}{\sigma_X^2 - 2\rho\sigma_X\sigma_Y+\sigma_Y^2}\\
\end{align}
Note that, the optimal weight is neither $0$ nor $1$, indicating that the minimum variance portfolio always has a smaller variance compared to its components (an arbitrary construction does not guarantee this, though).

### Multiple Risky Assets
Suppose we have the following portfolio:
\begin{align}
    \pi &= w^TX    
\end{align}
with $w^T1 = 1$, and
\begin{align}
    \mu &= w^T\mu_X\\
    \sigma^2 &= w^T \Sigma w
\end{align}

[MIT Lecture Notes](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote14.pdf)
# Probability

## Probability

### Uniform Random Variables
**Question 1:** I have a square, and place three dots along the four edges at random. What is the probability that the dots lie on distinct edges? (Jump)
<details>
<summary>Answer: </summary> 

The answer is $\frac38$. It is equivalent to ask: given a four-sided fair dice what is the probability that three rolls have all different numbers. The probability is $1 \times (3/4) \times (2/4) = 3/8$.

</details>
<br>

**Question 2:** A drunk man is standing at the edge of a cliff and if he moves one step to his right he will die. The probability of him moving one step to his left and right is 2/3 and 1/3, respectively. What is the probability of him dying?
<details>
<summary>Answer: </summary> 

Suppose the probability of moving one position right (regardless how many steps) is $p$. Then we have:
\begin{align}
    p = \frac13 + \frac23 (p \cdot p) \implies p = \frac12
\end{align}
where the first part indicates the drunk man moves one step to his right and die; the second part indicates the probability of standing at $x=-1$ and then moves to $x = 0$ and then moves to $x = 1$ (imaging the drunk man start at $x=0$).

</details>
<br>

### Normal Random Variables

	

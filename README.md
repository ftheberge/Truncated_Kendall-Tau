# Truncated_Kendall-Tau
Adapting the Kendall-Tau correlation to partial lists

## The context

Suppose that we have a finite collection of objects $\Omega$ with $|\Omega| = n$, and two algorithms that produce
partial rankings consisting of the respective top scoring objects from $\Omega$. For algorithm $i = 1, 2$, we
define:
- the scores $s_i(\omega), \forall \omega \in \Omega$,
- an induced ranking function $\mu_i(\cdot)$ on the elements $\omega \in \Omega$. The ranking is in decreasing order of
the scores $s_i(\omega)$, and we assume that there are no ties, so $\\{ \mu_i(\omega) ; \omega \in \Omega\\} = \\{1, 2, ..., n\\}$.

We assume the following context:
- for each algorithm $i$, we observe only a subset $X_i \subset \Omega$ with $|X_i| = k_i << n$. This set corresponds to the $k_i$ elements
$\omega \in \Omega$ with the largest scores $s_i(\omega)$. On $X_i$, we thus have $\mu_i ~ : ~ X_i \rightarrow \\{1, 2, ..., k_i\\}$, the 
top ranking elements.
- For all $\omega \in (\Omega \setminus X_i)$, we have that $\mu_i(\omega) > k_i$, but its exact value is unknown.

Note that we may have $k_1 \ne k_2$. We will assume that $k_1 \ge k_2$ without loss of generality.

Based on the above remarks, we wish to design a non-parametric **correlation coefficient**, which
we’ll refer to as $\tau_t$, with the following characteristics:
1. $\tau_t$ ∈ [−1, 1], which is typical for correlation coefficients,
2. if $k_1 = k_2$ and the top rankings are identical, then $\tau_t$ = 1,
3. if $k_1 > k_2$, but the top $k_2$ elements from algorithm 1 are the same and in the same order as for
algorithm 2, then $\tau_t$ = 1,
4. if the two rankings have no common element, then $\tau_t$ = −1,
5. $n$, the size of the underlying state space, may be unknown, so $\tau_t$ should not be a function of $n$.

In some cases, we want a **similarity** score which we simply define as $\tau_{sim} = (1+\tau_t)/2$ so the values are in range [0,1].

## Review of the Kendall-τ Correlation Coefficient

This coefficient is based on the following idea. We compare pairs of elements $\omega \ne \omega′$ from $\Omega$. If

$$(\mu_1(\omega) − \mu_1(\omega′)) \cdot (\mu_2(\omega) − \mu_2(\omega′)) > 0$$

the pair $(\omega, \omega′)$ is concordant while if the product is negative, the pair is discordant. 
Let C and D respectively denote the number of concordant (discordant) pairs. If there are no ties in the rankings,
the Kendall-τ coefficient is defined as:

$$\tau = \frac{2(C − D)}{n^2 − n}$$

Ties, if any, can be handled with proper corrections. 

Let $\Omega = \\{1, 2, .., n\\}$ via re-labelling, we get:

$$\tau = \sum_{i < j ; i,j=1}^n \frac{2 \cdot  sgn(\mu_1(i) − \mu_1(j)) \cdot sgn(\mu_2(i) − \mu_2(j))}{n^2 − n}$$

where $sgn()$ is the usual sign function.

## Truncated Kendall-τ Coefficient: Construction

Let $\Omega$ be the (finite) set of all possible values with $|\Omega| = n$, and consider 2 subsets $X_1, X_2$ with $|X_i| =
k_i << n$. 
Consider also 2 ranking functions $\mu_i(), i = 1, 2$ such that $\mu_i(\omega) \in \\{1, 2, .., k_i\\} , \forall \omega \in X_i \subset \Omega$.

For $\omega \ne \omega′$ both in $X_i$, $\mu_i(\omega) \ne \mu_i(\omega′)$. 
We define the following sets:

- $S_I = X_1 \cap X_2$, the intersection.
- $S_{X_1} = X_1 \setminus X_2$, elements exclusive to first list.
- $S_{X_2} = X_2 \setminus X_1$, elements exclusive to second list.
- $S_R = \Omega \setminus (X_1 \cup X_2)$, the “unobserved” elements.

For $i = 1, 2$, we extend the definition of the ranking function $µ_i()$ to all of $\Omega$ via:

$$\mu_i(\omega) = r, ~ \forall \omega \in S_R$$

where $r$ is some fixed, large value such that $r >> \max(k_1, k_2)$. Note that this is the same $r$ for both
$i = 1, 2$, and it encodes the fact that beyond the top $k_i$ elements, all elements are treated in the same
way.

**Definition 1** For all pairs $\omega_i \ne \omega_j \in \Omega$, we define
$$k(i, j) = sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) · sgn(\mu_2(\omega_i) − \mu_2(\omega_j))$$
the Kendall factor for that pair of elements.

**Proposition 1** Up to re-labelling of the $(\omega_i, \omega_j)$ pairs, there are 10 possible cases with respect to the
sets $S_I, S_{X_1}, S_{X_2}$ and $S_R$. Here are the Kendall factors for each case.

1. $\omega_i ∈ S_I, \omega_j ∈ S_I~:~k(i, j) = sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) · sgn(\mu_2(\omega_i) − \mu_2(\omega_j))$
2. $\omega_i ∈ S_I, \omega_j ∈ S_{X_1}~:~k(i, j) = −sgn(\mu_1(\omega_i) − \mu_1(\omega_j))$
3. $\omega_i ∈ S_I, \omega_j ∈ S_{X_2}~:~k(i, j) = −sgn(\mu_2(\omega_i) − \mu_2(\omega_j))$
4. $\omega_i ∈ S_I, \omega_j ∈ S_R~:~k(i, j) = 1$
5. $\omega_i ∈ S_{X_1}, \omega_j ∈ S_{X_1}~:~k(i, j) = 0$
6. $\omega_i ∈ S_{X_1}, \omega_j ∈ S_{X_2}~:~k(i, j) = −1$
7. $\omega_i ∈ S_{X_1}, \omega_j ∈ S_R~:~k(i, j) = 0$
8. $\omega_i ∈ S_{X_2}, \omega_j ∈ S_{X_2}~:~k(i, j) = 0$
9. $\omega_i ∈ S_{X_2}, \omega_j ∈ S_R~:~k(i, j) = 0$
10. $\omega_i ∈ S_R, \omega_j ∈ S_R~:~k(i, j) = 0$

*Proof*: All of the above can be shown directly from the definition of $k(i, j)$. For example, if we
consider case 2, then $\omega_j \in S_{X_1}$, so $\mu_2(\omega_j) = r$ while $\omega_i \in S_I$, so $\mu_2(\omega_i) << r$, thus $sgn(\mu_2(\omega_i)−\mu_2(\omega_j)) =
−1$. For case 5, $\mu_2(\omega_i) = \mu_2(\omega_j) = r$ so $sgn(\mu_2(\omega_i) − \mu_2(\omega_j)) = 0$, etc.

To define our coefficient $\tau_t$, we sum over the terms in cases 1-4 and 6 from Proposition 1, and we introduce
a constant factor D so that $−1 \le \tau_t \le 1$. This is summarized in Proposition 2.

**Proposition 2** Summing up the terms in Proposition 1, we get:

$$
\tau_t = \frac{1}{D} \cdot \left( \sum_{\omega_i \ne \omega_j \in S_I} sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) · sgn(\mu_2(\omega_i) − \mu_2(\omega_j)) − 
\sum_{\omega_i \in S_I, \omega_j \in S_{X_1}} sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) -
\sum_{\omega_i \in S_I, \omega_j \in S_{X_2}} sgn(\mu_2(\omega_i) − \mu_2(\omega_j)) 
− |S_{X_1}| \cdot |S_{X_2}| + |S_I| \cdot |S_R| \right)
$$

$|S_R|$ is a large, a priori unknown quantity where $|S_R| = |\Omega| − |S_{X_1}| − |S_{X_2}| − |S_I| \approx |\Omega| = n$,
and $\tau_t$ should be independent of $n$. If the 2 sets $X_1$ and $X_2$ were independent and randomly chosen, we
could use a “birthday paradox” type of argument to evaluate the most likely value for $|\Omega|$ given $|S_I|$,
but this is generally not the case here. In fact, for $|X_i| << \sqrt{n}$, we’d get $E|S_I| \approx 0$.

Since $|S_R|$ is assumed unknown, we replace the term $|S_R| \cdot |S_I|$ in Proposition 2 by a function $f(|S_I|)$.
We now look at the best and worst cases in order to set this function as well as the constant $D$.

*(a) Best case*: consider $|X_1| = M \ge |X_2| = |S_I| = m$, and all elements in $X_2$ are the top $m$ from $X_1$,
in the same order. This should yield $\tau_t = 1$. From Proposition 2, we get:

$$ D = \frac{m(m − 1)}{2} + m(M − m) + f(m) $$

*(b) Worst case*: consider $|X_1| = M = |S_{X_1}|, |X_2| = m = |S_{X_2}|, m ≤ M$ and $|S_I| = 0$. We should get
$\tau_t = −1$. From Proposition 2, we get:

$$D = mM − f(0)$$

From (a) and (b), we get

$$f(m) + f(0) = \frac{m(m + 1)}{2}$$

and with the natural condition $f(0) = 0$,

$$f(m) = \frac{m(m + 1)}{2}$$

This yields

$$D = Mm = |X_1| \cdot |X_2| \text{ and } f(|S_I|) = \frac{|S_I|(|S_I| + 1)}{2}$$

thus:

$$
\tau_t = \frac{1}{|X1| \cdot |X2|} \cdot \left(
\sum_{\omega_i \ne \omega_j \in S_I} sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) \cdot sgn(\mu_2(\omega_i) − \mu_2(\omega_j)) − 
\sum_{\omega_i \in S_I, \omega_j \in S_{X_1}} sgn(\mu_1(\omega_i) − \mu_1(\omega_j)) -
\sum_{\omega_i \in SI, \omega_j \in S_{X_2}} sgn(\mu_2(\omega_i) − \mu_2(\omega_j)) − 
|S_{X_1}| \cdot |S_{X_2}| + \frac{|S_I|(|S_I| + 1)}{2} \right)
$$

## Python code

```
from itertools import combinations as comb
## input: 2 lists X and Y of arbitrary length
def adaptedKendallTau(X, Y, similarity=True):
    SI = [x for x in X if x in Y] ## intersection - list to keep the order as in X
    SX = set(X).difference(SI)    ## in X only
    SY = set(Y).difference(SI)    ## in Y only
    tau = 0
    ## SI: pairs in intersection
    l = len(SI)
    y = [Y.index(z) for z in SI]
    s = sum([a<b for a,b in comb(y,2)])
    tau += 2*s - l*(l-1)/2 ## pos-neg pairs a la Kendall-tau.
    ## SX, resp. SY and SI: one element in intersection
    x = [X.index(z) for z in SX]
    y = [Y.index(z) for z in SY]
    i = [X.index(z) for z in SI]
    s = 2*sum([a>b for a in x for b in i]) - len(x)*len(i)
    tau += s
    s = 2*sum([a>b for a in y for b in i]) - len(y)*len(i)
    tau += s
    ## ze rest
    tau -= len(SX)*len(SY)
    tau += l*(l+1)/2
    tau /= (len(X)*len(Y))
    if similarity:
        return (1+tau)/2
    else:
        return tau
```

## Truncated Kendall-τ Coefficient: Properties

The three cases below can be shown directly from the definition of $\tau_t$.

**Case 1 - identical top lists:** Let $|X_1| = |X_2| = M$ and $|S_I| = M$, so all items are in both lists.
1. if the rankings are identical, then $\tau_t = 1$ and $\tau_{sim} = 1$.
2. if the rankings are reversed, then $\tau_t = 1/M \approx 0$ and $\tau_{sim} \approx 0.5$.
3. if the items are randomly ordered, independently in the two lists, then $\tau_t ≈ 1/2 + 1/(2M) \approx 0.5$ and $\tau_{sim} \approx 0.75$.

**Case 2 - comparing top and bottom from each list:** We consider $|X_1| = 2m$ and we define, for $i = 1, 2$:
* $top(X_i)$: the top $m$ items (given ranking) in set $X_i$.
* $bot(X_i)$: the bottom $m$ items (given ranking) in set $X_i$.
* $\mu_i(top(X_i))$: the ordered top $m$ items.
* $\mu_i(bot(X_i))$: the ordered bottom $m$ items.

Then:

1. If $|X_2| = m$ and $\mu_1(top(X_1)) = \mu_2(top(X_2))$, then $\tau_t = 1$ and $\tau_{sim} = 1$.
2. If $|X_2| = 2m,~ top(X_1) = top(X_2)$ with $\mu_1(top(X_1)) = \mu_2(top(X_2))$ but $bot(X_1) \cap bot(X_2) = \emptyset$,
then $\tau_t = 0.5$ and $\tau_{sim} = 0.75$.
3. If $|X_2| = m,~ bot(X_1) = top(X_2)$ with $\mu_1(bot(X_1)) = \mu_2(top(X_2))$, then $\tau_t = 0$ and $\tau_{sim} = 0.5$.
4. If $|X_2| = 2m,~ bot(X_1) = bot(X_2)$ with $\mu_1(bot(X_1)) = \mu_2(bot(X_2))$ but $top(X_1) \cap top(X_2) = \emptyset$, then $\tau_t = −0.5$ and $\tau_{sim} = 0.25$.
5. Finally, if $X_1 \cap X_2 = \emptyset, \tau_t = −1$ and $\tau_{sim} = 0$.

**Case 3 - limiting results:** We let $|X_1| = M$ and $|X_2| = m = |S_I|$, but we take $M \rightarrow \infty$ with $m$ fixed.
1. If $top(X_1) = X_2$, then $\tau_t \rightarrow 1$ ($\tau_{sim} \rightarrow 1$) as $M \rightarrow \infty$.
2. If $bot(X_1) = X_2$, then $\tau_t \rightarrow −1$ ($\tau_{sim} \rightarrow 0$) as $M \rightarrow \infty$.

The intuition here is that in the first case, the number of **concordant** pairs grows to **infinity**, while for
the second case, it is the number of **discordant** pairs














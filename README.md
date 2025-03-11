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
$\omega \in \Omega$ with the largest scores $s_i(\omega)$. On $X_i$, we thus have $\mu_i : X_i → {1, 2, ..., k_i}$, the 
top ranking elements.
- For all $\omega \in (\Omega \setminus X_i)$, we have that $\mu_i(\omega) > k_i$, but its exact value is unknown.

Note that we may have $k_1 \ne k_2$. We will assume that $k_1 \ge k_2$ without loss of generality.

Based on the above remarks, we wish to design a non-parametric correlation coefficient, which
we’ll refer to as $\tau_t$, with the following characteristics:
1. $\tau_t$ ∈ [−1, 1], which is typical for correlation coefficients,
2. if $k_1 = k_2$ and the top rankings are identical, then $\tau_t$ = 1,
3. if $k_1 > k_2$, but the top $k_2$ elements from algorithm 1 are the same and in the same order as for
algorithm 2, then $\tau_t$ = 1,
4. if the two rankings have no common element, then $\tau_t$ = −1,
5. $n$, the size of the underlying state space, may be unknown, so $\tau_t$ should not be a function of $n$.

## Review of the Kendall-τ Correlation Coefficient

This coefficient is based on the following idea. We compare pairs of elements $\omega \ne \omega′$ from $\Omega$. If

$$(\mu_1(\omega) − \mu_1(\omega′)) \cdot (\mu_2(\omega) − \mu_2(\omega′)) > 0$$

the pair $(\omega, \omega′)$ is concordant while if the product is negative, the pair is discordant. 
Let C and D respectively denote the number of concordant (discordant) pairs. If there are no ties in the rankings,
the Kendall-τ coefficient is defined as:

$$\tau = \frac{2(C − D)}{n^2 − n}$$

Ties, if any, can be handled with proper corrections. 

Let $\Omega = \\{1, 2, .., n\\}$ via re-labelling, we get:

$$\tau = \frac{2 \cdot  sgn(\mu_1(i) − \mu_1(j)) \cdot sgn(\mu_2(i) − \mu_2(j))}{n^2 − n}$$

where $sgn()$ is the usual sign function.

$$\sum_{i\<j}^n A$$

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
$i = 1, 2$, and it encodes the fact that beyond the “top-$k_i$” elements, all elements are treated in the same
way.







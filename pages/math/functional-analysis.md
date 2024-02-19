---
layout: page
title: Intro to Functional Analysis
permalink: /functional-analysis
---

## Finite Dimensional Normed Spaces

*Proposition: $$\mathbb{R}^n$$ is not compact.*
{: style="text-align: justify"}

Proof: Consider the metric space $$(\mathbb{R}^n,d_{euc})$$, where $$d_{euc}$$ denotes the usual euclidian metric. Note that in this metric space the complement of $$\mathbb{R}^n$$ is $$\emptyset$$. Recall that the empty set is open (specifically, *vacuously* open). Hence $$\mathbb{R}^n$$ is closed. But clearly $$\mathbb{R}^n$$ is not bounded. Therefore, by contraposition $$\mathbb{R}^n$$ is not compact. $$\blacksquare$$
{: style="text-align: justify"}


*Proposition: If $$X$$ is a compact metric space and $$M \subset X$$ is closed, then $$X$$ is locally compact.*
{: style="text-align: justify"}

Proof: If $$X$$ is compact, then $$X$$ is (closed and) bounded. Boundedness means that $$\delta(X) = \sup d(x,y) < \infty$$. Assume that $$\delta(X)=\delta_0$$. Now consider an arbitrary $$x_0 \in X$$ and the corresponding neighborhood containing $$B(x_0,\delta_0)$$. Clearly, such neighborhood must be equal to $$X$$, which is compact. Hence any arbitrary point in $$X$$ has a compact neighborhood, namely $$X$$ itself. Therefore, $$X$$ is locally compact. $$\blacksquare$$
{: style="text-align: justify"}

*Proposition: If $$X$$ is a compact metric space and $$M \subset X$$ is closed, then $$M$$ is also compact.*
{: style="text-align: justify"}

Proof: If $$X$$ is compact, then  every sequence in $$X$$ has a subsequence that converges in $$X$$. In particular, every sequence in $$M \subset X$$ has a subsequence that converges to a point $$x_0 \in X$$. In principle, the point $$x_0$$ may or may not be in $$M$$. But $$M$$ is closed. This implies that: if an arbitrary sequence $$(x_n)$$ in $$M$$ is convergent, then it must converge to a point in $$M$$. I.e., closedness guarantees that every subsequence in $$M$$ has a subsequence that converges to $$x_0 \in M$$. Therefore, $$M$$ is compact. $$\blacksquare$$
{: style="text-align: justify"}
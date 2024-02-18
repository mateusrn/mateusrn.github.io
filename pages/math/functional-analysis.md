---
layout: page
title: Intro to Functional Analysis
permalink: /functional-analysis
---

## Finite Dimensional Normed Spaces

*Proposition: If $$X$$ is a compact metric space and $$M \subset X$$ is closed, then $$M$$ is also compact.*
{: style="text-align: justify"}

Proof: If $$X$$ is compact, then  every sequence in $$X$$ has a subsequence that converges in $$X$$. In particular, every sequence in $$M \subset X$$ has a subsequence that converges to a point $$x_0 \in X$$. In principle, the point $$x_0$$ may or may not be in $$M$$. But $$M$$ is closed. This implies that: if an arbitrary sequence $$(x_n)$$ in $$M$$ is convergent, then it must converge to a point in $$M$$. I.e., closedness guarantees that every subsequence in $$M$$ has a subsequence that converges to $$x_0 \in M$$. Therefore, $$M$$ is compact. $$\blacksquare$$
{: style="text-align: justify"}
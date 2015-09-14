[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> This exercise deals with reimplementing the hypothesis test from Section 9.3, using resampling instead of permutation. As suggested, I used a resampling technique that draws a sample (with replacement) from the pool of observed values. Below is the code for the class `DiffMeansResample`, which inherits from the `DiffMeansPermute` class from the text.

```
class DiffMeansResample(DiffMeansPermute):
	def RunModel(self):
		group1 = np.random.choice(self.pool, 
							self.n, replace = True)
		group2 = np.random.choice(self.pool, 
							self.m, replace = True)
		return group1, group2
```

>> This alternative way of formulating the null hypothesis has very little effect on the hypothesis test itself. Using the code below, we can compute the p-values for effect size in first borns and others, for both pregnancy length and birth weight. The p-value for pregnancy length turns out to be 0.16 (Section 9.3 gave us 0.17 by comparison) and the p-value for birth weight turns out to be 0.0 (just as in Section 9.3).

```
def main():
	live, firsts, others = first.MakeFrames()
	
	data1 = firsts.prglngth.dropna().values,
			 others.prglngth.dropna().values
	ht1 = DiffMeansResample(data1)
	p_value1 = ht1.PValue()
	print 'p-value for pregnancy length =', p_value1
	
	data2 = firsts.totalwgt_lb.dropna().values,
				others.totalwgt_lb.dropna().values
	ht2 = DiffMeansResample(data2)
	p_value2 = ht2.PValue()
	print 'p-value for birth weight =', p_value2
```

>> In conclusion, it looks like both formulations of the null hypothesis seem to imply that (at least with this sample size and data) the difference in pregnancy length between groups is not statistically significant, but that the difference in birth weight is indeed statistically significant.
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> In this example, I examined the effect size of birth order on weight at birth for the live births reported in the NSFG survey. Specifically, I looked at the Cohen's d value calculated on the birth weights for two groups: first-born children and others. Below is the code used to compute d.

```
def CompareWeight(firsts, others):
	"""Compares total weight in pounds of first babies
	and other babies, using Cohen's d measurement of
	effect size. This implementation uses the version
	of Cohen's d equation from wikipedia, namely using
	n1 - 1 and n2 - 1 instead of n1, n2.
	firsts, others: DataFrame objects representing the
					two groups
	returns: floating-point Cohen d value
	"""
	
	first_mean_wgt = firsts.totalwgt_lb.mean()
	other_mean_wgt = others.totalwgt_lb.mean()
	
	first_var_wgt = firsts.totalwgt_lb.var(ddof = 1)
	other_var_wgt = others.totalwgt_lb.var(ddof = 1)
	n1, n2 = len(firsts) - 1, len(others) - 1
	
	pooled_var = (n1 * first_var_wgt + 
				n2 * other_var_wgt) / (n1 + n2)
				
	cohenD = (first_mean_wgt - other_mean_wgt) / 
					math.sqrt(pooled_var)
					
	return cohenD
```

>> The DataFrame.var method takes an optional parameter ddof, which stands for "delta degrees of freedom"; by setting ddof = 1, we effectively use N - 1 as the denominator in calculating the variance, as Cohen originally required.
>> 
>> The Cohen d value returned in this context is approximately -0.08867. My interpretation of this result is that on average in our sample, first babies are born lighter, but that the effect size of being first-born only amounts to about 8% of one standard deviation. In other words, the difference in weight between first-borns and other babies in this survey is rather small.
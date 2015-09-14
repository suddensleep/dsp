[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> This exercise asked us to use the CPS data to examine the distribution of income in the United States, with a specific eye towards measuring the well-known skew to the right this distribution has. I calculated median, mean, sample skewness, and Pearson's skewness, as well as the percentage of households with income below the mean; furthermore, I repeated this calculation a number of times with a different assumption about what the maximum income might be (i.e. the upper bound on the highest income bracket).

>> This exercise really bothered me for a little while, because I kept getting results that didn't make any sense to me. No matter how high I made the upper bound for the highest income bracket, I was STILL getting a mean value that was lower than the median value, which doesn't make sense for a distribution that should be skewed to the right. The issue was that I was directly computing the mean and median from the log10 values of the incomes, NOT from the real incomes themselves! Needless to say, a few outliers like 6 and 7 in a field of mostly 3s, 4s, and 5s doesn't skew the mean of the distribution nearly as much as a value of 10 million in a field of mostly 50,000s does!
>> 
>> Once I realized WHY the incomes were being transformed to their log10 values (so that their log10 values could be spread uniformly over each bracket in `InterpolateSample`), it made more sense to me that the actual statistics work should be done on the real incomes. The results made a lot more sense, and seemed to match more nicely with the readily-available results I found online.
>> 
>> With an upper bound of $1 million income on the highest bracket, here were the results:

```
Median income: $51,226.45
Mean income: $74,278.71
Sample skewness: 4.9499
Pearson's median skewness coefficient: 0.7361
% of households with income below mean: 66%
```

>> With an upper bound of $10 million of income on the highest bracket, here were the results:

``` 
Median income: $51,226.45 
Mean income: $114,309.32
Sample skewness: 11.1904
Pearson's median skewness coefficient: 0.4129
% of households with income below mean: 83.13%.
```

>> As expected, the mean is higher than the median in both of these cases, and both of the skewness statistics support the notion that this distribution is skewed to the right. As was noted in the text, the sample skewness is quite sensitive to the gigantic outliers we get as we raise the upper bound. Pearson's statistic is more robust; as the difference of the mean and median grows, so does the standard deviation.

>> The code for generating these results (as well as a number of intermediate results for upper bounds on income between $1 million and $10 million) is included below.

```
import hinc
import hinc2
import thinkstats2

def printSkewness(df, log_upper):
    """Interpolates a sample based on the hinc data with
    log10 of the upper bound of the highest bracket, 
    transforms the log values to real dollar values, then 
    computes central tendencies and skewness statistics.

    df: data frame of hinc data (sorted by income bracket)
    log_upper: log_10 of the upper bound 
    			for the highest bracket
    
    returns: none (prints values instead)
    """
    
    # Logs taken so that each income bracket has the
    # property that log10 income is uniformly spread
    log_sample = hinc2.InterpolateSample(df, log_upper)
    
    # Transform log values to real dollar values
    sample = [10**val for val in log_sample]
    cdf = thinkstats2.Cdf(sample)
    median = cdf.Value(0.5)
    mean = thinkstats2.RawMoment(sample, 1)
    skewness = thinkstats2.StandardizedMoment(sample, 3)
    pearson_skew = thinkstats2.PearsonMedianSkewness(sample)
    perc_below_mean = cdf.PercentileRank(mean)
    
    print '\nWith the upper bound on income at 
    	$%.2f:' % 10**log_upper
    print 'Median is $%.2f.' % median
    print 'Mean is $%.2f.' % mean
    print 'Sample skewness is %.4f.' % skewness
    print "Pearson's median skewness 
    	coefficient is %.4f." % pearson_skew
    print 'The percentage of households with income 
    	below the mean is %.2f%%.\n' % perc_below_mean

def main():
    data = hinc.ReadData()
    
    # Test a range of different upper bounds 
    # between 1 million and 10 million
    upper_bounds = [x / 10.0 for x in range(60, 70)]
    for upper_bound in upper_bounds:
        printSkewness(data, upper_bound)

if __name__ == '__main__':
    main()
```
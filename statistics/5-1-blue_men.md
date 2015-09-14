[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> This question asks us to find out what percentage of American men are between the heights of 5'10" and 6'1". We are also given a rough approximation for the distribution of heights in American men, a normal distribution with a mean of 178cm and a standard deviation of 7.7cm.
>> 
>> The first thing I noticed was that the units were expressed differently in the distribution and the question being asked. After finding the inches to centimeters conversion rate, this was pretty trivial to take care of.
>> 
>> Then I had to think about a method to find the percentage of the population with heights between two specific values. Since `CDF(maxHeight)` gives the total fraction of the population under the maximum height (our target population plus everyone shorter than 5'10") and `CDF(minHeight)` gives the total fraction of the population under the minimum height (everyone shorter than 5'10"), a simple subtraction did the trick here: `CDF(maxHeight) - CDF(minHeight)`. 
>> 
>> The percentage of American men between the heights of 5'10" and 6'1" is about 34.27%.
>> 
>> The code I wrote for this process, using `scipy.stats.norm`, is below.

```
import scipy.stats

def getCDFDiff(dist, maxVal, minVal = 0):
    """Finds the value of CDF(maxVal) - CDF(minval) 
    given a distribution. If minVal is not supplied,
    it defaults to 0.

    dist = distribution (scipy) 
    maxVal, minVal = maximum and minimum values in the distribution

    returns: percentage (as floating point 0-1) between two values
    """

    return dist.cdf(maxVal) - dist.cdf(minVal)

def main():
    # Creating normal distribution object
    mu = 178
    sigma = 7.7
    normal = scipy.stats.norm(loc = mu, scale = sigma)
    
    # Converting (ft, in) to inches
    minHeightIn, maxHeightIn = 5*12 + 10, 6*12 + 1
    # Converting inches to centimeters
    minHeightCm, maxHeightCm = minHeightIn*2.54, maxHeightIn*2.54

    # Printing percentage
    print "The percentage of American men between the",
    print "heights of 5'10\" and 6'1\" is",
    print "%.2f" % (100 * getCDFDiff(normal, maxHeightCm, minHeightCm)) + "%."
    

if __name__ == '__main__':
    main()
```
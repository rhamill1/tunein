### Environment Set Up Instructions
```
$ python -m virtualenv venv
$ source venv/bin/activate

$ pip install pandas
$ pip install matplotlib
$ pip install Flask
$ pip install bokeh
$ pip freeze > requirements.txt
```
### Execute Python Script
I've commented out many print() functions and left notes in the tunein.py script. In a production environment I would have removed these but wanted to leave enough context into my checks as I wrote this script. All three question functions can be run at once by uncommenting where they're called, or they can be run one at a time (uncomment, save, execute, repeat).

```
$ venv/bin/python scripts/tunein.py
```
### Results
##### Question 1.
- **Process:**  I looked at using 'Business Corridor' and 'Business Location' but those fields were null for most records and the 'Neighborhoods' field offered the most complete and intuitive grouping. I removed inactive businesses (via. ‘business end date’) and records without neighborhood data. Then I counted businesses by neighborhood.
- **Results:** passed the sniff test of The Financial District, Mission and SOMA being at the top of the list.

  It would also be interesting to plot the neighborhoods on a map and show density by geography. [This](http://gradientdissent.com/blog/analyzing-2-months-of-real-crime-data-from-san-francisco-and-seattle.html) is an interesting looking blog post that shows how to plot neighborhoods.



##### Question 2.
- **Process:** First I dropped all columns except the NAICS columns.  Then similarly to last time I grouped and counted records.
- **Results:** The sorted data from this also passes the sniff test, but more thought is needed to make good recommendations.
- **Recommendation:** It's short sighted to just draw a line and say any industry type with business counts below a certain threshold needs assistance. The example that comes to mind is:  although there aren’t very many utilities, how many utility companies does San Francisco need? Maybe as time goes on more utilities are needed but is it necessary for the city to stimulate that growth or can the market organically control this? Insurance looks like it could be similar to Utilities. Manufacturing looks like a good candidate for assistance and depending what 'Certain Services' include, they might also be candidates.
- **Moving forward:**  Time permitting, I’d look at start and end dates of businesses to see if less popular industries are less popular because they’re no longer needed.  For example, travel agencies aren’t as needed anymore. It’d be great to get NAICS sub-description data to understand what specific industries might be trending or declining.

##### Question 3.
- **Process - Data:**

  - I started by getting just the fields I needed ('naics\_code', 'naics\_description', 'business\_start\_date') and converting 'business\_start\_date' to its year.
  - Then I converted the year field to a number so I could remove businesses that start in the future.
  - Then I counted the grouping of each NAICS by year and converted it to a Pandas dataframe.
  - From there I used list interpolation to create a list of distinct years so I could populate years when no new businesses started, to create a plot.
  - Similarly, I create a list of distinct NAICS and again used list interpolation to create a matrix of all possible year-NAICS combinations with zeros for values. Then I turned that list  back into a Pandas dataframe so I could join it to my data frame with the counts of new businesses.
  - After merging, I coalesced the counts and zeros and pivoted the merged data frame to NAICS values by years so it could be fed into a matplotlib line chart.

- **Process - Analysis:**
  - My analytical approach to this question was to utilize a line chart and continue to zoom into interesting periods be adjusting the data ranges I was feeding the chart.
  - My initial pass dated back to 1849 thinking there might be something interesting there but that wasn’t the case compared to the 1960’s and afterwards.
  - The second pass looked at post WWII dates.  This uncovered that new real estate businesses are very opportunistic based on market expansion in the late 1960’s, late 1980’s, pre-recession and currently. Interestingly there’s a construction spike after the 2014 real estate spike.
  - This pass also uncovered what appears to be the 'rental economy' based on large spikes around 2014 for Warehouse and Transporation as well as Accomodations. These would support Lyft and Uber drivers and Airbnb hosts being classified as businesses.

- **Note:** One decision I made that I’d ask for clarification on in a business setting, was to not remove duplicate businesses based on multiple locations. I was interested in seeing trends and I left them in because I wanted to highlight the magnitude of specific categories.  Ex. is adding one McDonalds a trend or is adding 50 McDonalds a trend?

##### Question 4.
- **Question 1:**  It’d be great to discern the neighborhoods from the records where that’s missing, either from address, or a third party.

- **Question 2:**  Time permitting, I’d look at start and end dates of businesses to see if less popular industries are less popular because they’re no longer needed.  For example, travel agencies aren’t as needed anymore. It’d be great to get NAICS sub-description data to understand what specific industries might be trending or declining.

- **Question 3:** If I had more time, I’d look deeper into the Warehouse and Transportation category to see if that huge recent spike is based on people using storage/warehousing due to an expensive housing climate, or more likely, Uber and Lyft drivers are being classified as unique individual businesses. The spike in Accommodations starting at the beginning of 2014 also supports this ‘rental economy’ hypothesis.

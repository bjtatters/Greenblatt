# Greenblatt
A web-scraping python script that identifies "special situations" in SEC filings. As outlined in Joel Greenblatt's book, "You can be a Stock Market Genius", these situations can prove to be highly profitable and are key to his unparalleled returns over the past 20 years.

**How does the script work?**

In Greenblatt's book, certain SEC filings related to 'special situations'- whether that be a corporate restructing, merger or otherwise - are mentioned frequently. 

Those frequently mentioned are '10-12B', '10-12B/A', '8-K', '8-K/A', 'S-4', 'S-4/A', 'S-1', 'S-1/A' and 'S-1MEF'. A description of each of these filings can be found here: https://www.sec.gov/forms.

These filings are convoluted, tricky to find and often misleading. To therefore aid recreational investors in identifying these situations, the script here scrapes daily SEC filings to pinpoint the relevant filings and which companies they belong to. More than that, it automatically emails the outputs of this scraping to you.

While the nature of each filing is often clear-cut, there are equally many instances in which the purpose of the filing is unknown and perhaps unrelated to any special situation. To mitigate against these unwanted entries, the script also includes a basic word search function. After identifying each filing, it opens the filing and counts the occurences of the following words related to "special situations": 'spin-off', 'restructuring', 'merger', 'bankruptcy', 'recapitalisation' and 'rights offering'.

In doing so, this word search function allows each user (investor) to see which filings are useless, and which are informative. 

**Before starting...**

It is important to note that the SEC filing website uses cik numbers to identify each company, rather than its ticker. The SEC itself provides a .txt file that shows each CIK and the corresponding ticker, however the name of each company is still missing. To save valuable time in looking for full company names, it is advisable to download this .csv file here: https://raw.githubusercontent.com/ngshya/pfsm/master/data/sec_edgar_company_info.csv

After saving this file, input its file path into line 22 of the script.

**Opportunities for further improvement**

As mentioned above, the scraping process includes a word search function. To avoid overloading the output file however, and forcing the user to go through the data table avoiding those filings that don't mention any special situations, a simple screen could be included that omits any filing without a sufficient number of 'special situation mentions'.

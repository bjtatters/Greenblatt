# Greenblatt
A web-scraping python script that identifies "special situations" in SEC filings. As outlined in Joel Greenblatt's book, "You can be a Stock Market Genius", these situations can prove to be highly profitable and are key to his unparalleled returns over the past 20 years.

**How does the script work?**

In Greenblatt's book, certain SEC filings related to 'special situations'- whether that be a corporate restructing, merger or otherwise - are mentioned frequently. 

Those frequently mentioned are '10-12B','10-12B/A','8-K','8-K/A','S-4','S-4/A','S-1','S-1/A'and'S-1MEF'. A description of each of these filings can be found here: https://www.sec.gov/forms.

These filings are convoluted, tricky to find and often misleading. To therefore aid recreational investors in identifying these situations, the script here scrapes daily SEC filings to pinpoint the relevant filings, which companies they belong to and the particular type of situation mentioned in each filings. More than that, it automatically emails the outputs of this scraping to you.

**Before starting...**

It is important to note that the SEC filing website uses cik numbers to identify each company, rather than its ticker. Before using the script then, it is important that you download the latest cik lookup data here: https://www.sec.gov/Archives/edgar/cik-lookup-data.txt


# **arnoldas_a_mod1_atsiskaitymas**

Package for scraping book information and football match results from specified websites.

# **Installation**
pip install arnoldas-a-mod1-atsiskaitymas

PyPI Link: https://pypi.org/project/arnoldas-a-mod1-atsiskaitymas/

# **Usage**
A package is using selenium for web scraping and supports data export in CSV and dictionary formats. **IMPORTANT**. In order to use a package, user needs to install Chrome WebDriver
and Update the path in the football_results.py and book_info.py files from path = 'C:\\Tools\\chromedriver\\chromedriver.exe' to yours

# **Parameters**
A package can be run from main, user has to determine:
- source = "book_info" or "football_results"
- timeout = in seconds
- return_format = "dict" or "csv"

# **Example**

```python
from crawler import Crawl

def main():
    source = "book_info"
    timeout = 60
    return_format = "dict"

    results = Crawl(source=source, timeout=timeout, return_format=return_format).web_results()
    if results:
        print("Gauti duomenys:")
        print(results)

if __name__ == "__main__":
    main()

# Web scraping, also called web data extraction, refers to the technique of harvesting data from a web page through leveraging the patterns in the page’s underlying code. It can be used to collect unstructured information from websites for processing and storage in a structured format.


# 1. import required modules: 
# a. we will start with the module for launching or initializing a browser

from selenium import webdriver

# b. module for emulating keyboard actions 

from selenium.webdriver.common.keys import Keys

# c. now the module is searching for items using the specified parameters:

from selenium.webdriver.common.by import By

# d. then the module is waiting for a webpage to load

from selenium.webdriver.support.ui import WebDriverWait

# e. importing modules that issues instructiins to wait for the expected conditions to be present before the rest of the code is executed 

from selenium.webdriver.support import expected_conditions as EC 

# 2. Initializing the WebDriver
# (every browser has its own unique implementation of the WebDriver, called a driver)
# a. sppecify the path where the chrome WebDriver is installed on our windows machine

PATH = "C:\Program Files (x86)\chromedriver.exe" 
# i dont know how to install drivers and store it in a file. i'd like to use edge instead of windows
driver = webdriver.Chrome(PATH)


# 3. navigating to the web page: 
# use driver.get method to navigate to the web page we want to scrape its data 

driver.get("https://www.reddit.com/")


# 4. locating the search box:
# The WebDriver provides a wide range of find_element(s)_by_* methods to locate a single element or multiple elements on a web page. 
# You can use tag names, CSS selectors, XPath, IDs, class names, and others to select elements.
# we can use the find_element_by_name method to locate the target element.

search = driver.find_element_by_name("q")


# 5. entering the search term:
# use the send_keys method to specify the term we want to search for in the input field
# then, we'll use Keys.RETURN to enter the term
# this is similar to using the keyboard to perform a search

search.send_keys("scraping")
search.send_keys(Keys.RETURN)


# 6. locating the search results:
# we will use an explicit wait that makes the webdriver to wait for the element we want to locate to be present on the page before proceeding with the rest of the code execution
# we can accomplish this using a combination of WebDriverWait method and the ExpectedCondition method
# in this case, we'll instruct selenium to wait 20 seconds for the rpBJOHq2PR60pnwJlUyP0 class to be present on the page. If that element is not located within that duration, then a TimeoutException will be thrown.

try:
    search_results = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0")))


# 7. scraping the posts' headings:
# a. start by selecting all the posts headings and storing them in a list

    posts = search_results.find_elements_by_css_selector("h3.__eYtD2XCVieq6emjKBH3m")

# b. go over each heading and output their content

    for post in posts:
        header = post.find_element_by_tag("span")
        print(header.text)


# 8. quitting the browser
finally: 
    driver.quit()



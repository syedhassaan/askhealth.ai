from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.cochranelibrary.com/")


# Close cookies popup
element = driver.find_element(
    By.CSS_SELECTOR, '.osano-cm-dialog__close.osano-cm-close')
element.click()

print("Close the cookies popup")

# Click on 'Browse By Topic'
element = driver.find_element(By.XPATH, '//*[@id="ui-id-6"]')
driver.execute_script("arguments[0].click();", element)

print("'Browse By Topic' clicked")

topics = driver.find_elements(
    By.CSS_SELECTOR, '.btn-link.browse-by-list-item-link')

for topic in topics:
    # Click on topic
    # element = driver.find_element(
    #     By.XPATH, '// *[@id="portlet_scolaristopics_WAR_scolaristopics"]/div[1]/div/div/div/div[2]/div/div[1]/dl/dd[1]/ul/li/a/button')
    # driver.execute_script("arguments[0].click();", element)

    print(topic.text + " clicked")
    topic.click()
    # driver.execute_script("window.open('https://www.google.com')")

    # Click on drop down
    element = driver.find_element(
        By.XPATH, '//*[@id="searchArticleForm"]/div[4]/div[2]/div[2]/div/div')
    driver.execute_script("arguments[0].click();", element)

    print("Dropdown clicked")

    # Select 100
    element = driver.find_element(
        By.XPATH, '//*[@id="searchArticleForm"]/div[4]/div[2]/div[2]/div/ul/li[4]')
    driver.execute_script("arguments[0].click();", element)

    print("Option for 100 results selected")

    # time.sleep(30)

    # Wait for spinner to go away
    wait = WebDriverWait(driver, 30)
    element = wait.until(
        EC.invisibility_of_element((By.CSS_SELECTOR, '.spinner-container')))

    # Get number of total results
    element = driver.find_element(By.CSS_SELECTOR, '.results-number')
    results = element.text
    print("# of Results: ", results)

    links = driver.find_elements(By.CSS_SELECTOR, '.result-title')
    print("# of links: ", len(links))

    # for i in range(1, int(results)):
    i = 0
    for link in links:
        # Click on link
        # element = driver.find_element(
        #     By.XPATH, '//*[@id="column-2"]/div[1]/div[3]/div[' + str(i) + ']/div[2]/h3')
        # element.click()

        # print("link.text: ", link.text)
        link.click()

        i += 1
        print("Click on the #" + str(i) + " link")

        # time.sleep(30)

        # Print the page title
        driver.switch_to.window(driver.window_handles[-1])
        page_title = driver.title
        print("Page title:", page_title)

        if "Search | Cochrane Library" not in page_title:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

# driver.get("https://www.cochranelibrary.com/")

# # Click on 'Browse By Topic'
# element = driver.find_element(By.XPATH, '//*[@id="ui-id-6"]')
# driver.execute_script("arguments[0].click();", element)

# print("'Browse By Topic' clicked")

# # Click on 'Blood disorders'
# element = driver.find_element(
#     By.XPATH, '//*[@id="portlet_scolaristopics_WAR_scolaristopics"]/div[1]/div/div/div/div[2]/div/div[1]/dl/dd[2]/ul/li/a/button')
# driver.execute_script("arguments[0].click();", element)

# print("'Blood disorders' clicked")

# Close the browser
driver.quit()

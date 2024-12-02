import os
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True

url = 'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F'


#load link

def login(username, password):

    global driver, wait
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    #for maximized screen
    driver.maximize_window() #fullscreen

    #gets the url
    driver.get(url)

    #username and password
    driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys(password)
    
    #click login
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button > span.ButtonInner-sc-14ud5tc-0.liTfRZ.encore-bright-accent-set'))).click()

def download():
    str1 = 'spotdl '
    str2 = driver.current_url
    main_str = str1 + str2
    sleep(15)
    os.system(main_str)
    print("Downloading...")

def like_song():
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[3]/div[2]/div/div/button[1]').click()
    print("Liked the song...")

def playlist():

    #Option Menu
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[3]/div[2]/div/div/button[2]').click()

    #Sub_Menu : Add to playlist(Hovers)
    sub_menu = driver.find_element(By.XPATH, "//span[normalize-space()='Add to playlist']")
    chain = ActionChains(driver)
    chain.move_to_element(sub_menu).perform()
    
    #Clicks on playlist to add
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='Type__TypeElement-sc-goli3j-0 dOtTDl ellipsis-one-line htqz7Vb8mLJvGKTi1vrs'][normalize-space()='Flavours of Japan']"))).click()

def search_song(query):
    # Clicks on search option
    search = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Search']//*[name()='svg']")))
    search.click()

    # Wait for the search input field to be visible
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/header/div[2]/div[2]/div/div/form/input')))
    search_bar.send_keys(query)
    
def play_song():
    # Wait for the top result to be present
    top_result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ouEZqTcvcvMfvezimm_J']")))

    # Hover over the top result
    chain = ActionChains(driver)
    chain.move_to_element(top_result).perform()

    # Wait for the play button to be clickable and click it
    play_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[3]/div/button')))
    play_button.click()

    #clicks on the top result after playing it for further options
    driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]').click()
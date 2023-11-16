from instagram_meme import *
from  twitter_meme import *





def get_twitter_meme(driver):

    get_memes_links_view(driver)
    time.sleep(1)
    move_base_data()
    time.sleep(1)
    sorted_by_view()
    time.sleep(1)
    sort_by_repeat()
    time.sleep(1)
    remove_duplicate()
    time.sleep(1)
    get_top_list()
    time.sleep(1)

def get_instagram_meme(driver):

    get_memes_links_view_instagram(driver)
    time.sleep(1)
    move_base_data_instagram()
    time.sleep(1)
    sorted_by_view_instagram()
    time.sleep(1)
    sort_by_repeat_instagram()
    time.sleep(1)
    remove_duplicate_instagram()
    time.sleep(1)
    get_top_list_instagram()
    time.sleep(1)

def main_get_all_link():

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    time.sleep(90)

    driver.get("https://twitter.com")
    time.sleep(90)

    for i in range(10000):
        get_twitter_meme(driver)
        time.sleep(1)
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        get_instagram_meme(driver)

    driver.quit()

#main_get_all_link()
move_base_data_instagram()
time.sleep(1)
sorted_by_view_instagram()
time.sleep(1)
sort_by_repeat_instagram()
time.sleep(1)
remove_duplicate_instagram()
time.sleep(1)
get_top_list_instagram()
time.sleep(1)
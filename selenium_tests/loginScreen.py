def loginScreen(driver, sleep):
    driver.find_element_by_id("email").send_keys("Admin@admin.com")
    sleep(1)
    driver.find_element_by_tag_name("span").click()


def registerScreen(driver, Select, os):
    driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Raj")
    driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Jain")
    driver.find_element_by_tag_name("textarea").send_keys("12-D,Streets View,Docker Lane")
    driver.find_element_by_xpath("//input[@type='email']").send_keys("raj@gmail.com")
    driver.find_element_by_xpath("//input[@type='tel']").send_keys("9658741256")
    driver.find_element_by_xpath("//input[@value='Male']").click()
    driver.find_element_by_id("checkbox2").click()
    driver.find_element_by_id("imagesrc").send_keys(os.getcwd() + "/test_sel.py")
    driver.find_element_by_id("Skills").send_keys("Python")
    driver.find_element_by_id("countries").send_keys("Egypt")
    yearbox = Select(driver.find_element_by_id("yearbox"))
    yearbox.select_by_value("1996")
    monthbox = Select(driver.find_element_by_xpath("//select[@placeholder='Month']"))
    monthbox.select_by_value("June")
    daybox = Select(driver.find_element_by_id("daybox"))
    daybox.select_by_value("16")
    driver.find_element_by_id("firstpassword").send_keys("123456")
    driver.find_element_by_id("secondpassword").send_keys("123456")

    for i in range(1, int(driver.execute_script("return document.body.scrollHeight")), 2):
        driver.execute_script("window.scrollTo(0, {});".format(i))

    driver.find_element_by_id("Button1").click()
    driver.execute_script("window.scrollTo(0,0)")

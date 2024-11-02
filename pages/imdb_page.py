from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.config import BasePage as BP



class Imdb_Page(BP):

    # Here all dropdowns as (_DD) && all the field places as (_value). (for understanding purpose).

    NAME_DD = (By.XPATH,'//*[@id="nameTextAccordion"]/div[1]/label/span[1]/div')
    name_value = (By.NAME, 'name-text-input')
    BIRTHDATE_DD = (By.XPATH,'//*[@id="birthDateAccordion"]/div[1]/label')
    birthdate1_value = (By.NAME,'birth-date-start-input')
    birthdate2_value = (By.NAME,'birth-date-end-input')
    BIRTHDAY_DD = (By.XPATH,'//*[@id="birthdayAccordion"]/div[1]/label')
    bd_value = (By.NAME,'birthday-input')
    AWARDS_RECOGNITION_DD = (By.XPATH,'//*[@id="awardsAccordion"]/div[1]/label')
    award_rec_value = (By.XPATH,'//*[@id="accordion-item-awardsAccordion"]/div/section/button[2]')
    PAGE_TOPIC_DD = (By.XPATH,'//*[@id="pageTopicsAccordion"]/div[1]/label')
    page_topic_value1 = (By.XPATH, '// *[ @ id = "accordion-item-pageTopicsAccordion"] / div / div / section / button[2]')
    page_topic_value2 = (By.XPATH,'//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]')
    DROP_DOWN_DD = (By.XPATH,'//*[@id="within-topic-dropdown-id"]')
    dd_value = (By.NAME,'within-topic-input')
    DEATH_DATE_DD = (By.XPATH,'//*[@id="deathDateAccordion"]/div[1]/label/span[2]/svg')
    death_date1_value = (By.NAME, 'death-date-start-input')
    death_date2_value = (By.NAME, 'death-date-end-input')
    GENDER_IDENTITY_DD = (By.XPATH,'//*[@id="genderIdentityAccordion"]/div[1]/label')
    gender_identity_value = (By.XPATH,'//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]')
    CREDITS_DD = (By.XPATH,'//*[@id="filmographyAccordion"]/div[1]/label')
    credits_value = (By.XPATH,'//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
    ADULT_NAME_DD = (By.XPATH,'//*[@id="adultNamesAccordion"]/div[1]/label')
    adult_name_value = (By.ID,'include-adult-names')
    SEARCH_BUTTON = (By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]')


    def __int__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # for entering the name method
    def name_data(self, enter_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NAME_DD))(self.BP.clicks())
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.name_value()))(self.BP.do_send_key(enter_name))

    # for entering the birth_date (mm/dd/yyyy).
    def birth_date_data(self, from_date, to_date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BIRTHDATE_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birthdate1_value()))(self.BP.do_send_key(from_date))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birthdate2_value()))(self.BP.do_send_key(to_date))

    # for entering the birthday(mm/dd).
    def birthday_data(self, birth_date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BIRTHDATE_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.bd_value()))(self.BP.do_send_key(birth_date))

    # for select award what we want.
    def awards_data(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.AWARDS_RECOGNITION_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.award_rec_value()))(self.BP.clicks())

    # for page topic data(eg:Biography) method.
    def page_topic_data(self,enter_bio):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PAGE_TOPIC_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.page_topic__value()))(self.BP.do_send_key(enter_bio))

    # for entering the death_date(mm/dd/yyyy).
    def death_date_data(self, from_date, to_date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DEATH_DATE_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_date1_value()))(self.BP.do_send_key(from_date))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_date2_value()))(self.BP.do_send_key(to_date))

    # for select gender (M/F/O) method.
    def gender_id(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GENDER_IDENTITY_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.gender_identity_value()))(self.BP.clicks())

    # for credits method.
    def credits(self,movie_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREDITS_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.credits_value()))(self.BP.do_send_key(movie_name))

    # for adult name method.
    def adult_name(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADULT_NAME_DD))(self.BP.clicks())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.adult_name_value()))(self.BP.clicks())

    # for final operation of click see_result button.
    def search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))(self.BP.clicks())

    # for page_scroll_down where we want to need.
    def scroll_down(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)))





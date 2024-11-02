import pytest
from pages.imdb_page import Imdb_Page
from tests.conftest import chrome_driver
from configuration.config import BasePage as BP



@pytest.mark.usefixtures('chrome_driver')
class Test_IMDB(BP):
    def test_see_results(self):

        self.imdb = Imdb_Page(self.driver)

        # enter the name in name field
        self.name_data('Heath Ledger')


        # enter the brith_date in brith_date field
        self.imdb.birth_date_data('04/04/1979', '04/04/1979')

        self.imdb.scroll_down()

        # enter the birth_day_date in brith_day_date field
        self.imdb.birthday_data('04-04')


        # select the option what we need in Awards & recognition field
        self.imdb.awards_data()

        self.imdb.scroll_down()

        # enter the page_topic in the page_topic field
        self.imdb.page_topic_data("Movies")


        # enter the death_date in the death_date field
        self.imdb.death_date_data('01/22/2008', '01/22/2008')

        self.imdb.scroll_down()

        # select the gender in the gender field
        self.imdb.gender_id()


        # enter the credits in the credits field
        self.imdb.credits('I Am Heath Ledger')

        self.imdb.scroll_down()

        # select the adult_name we need or not in adult_name field
        self.imdb.adult_name()

        # hit the see result button
        self.imdb.search()

        expected_url = ('https://www.imdb.com/search/name/?name=heath%20ledger&birth_date=1979-04-04,1979-04-04&birth_monthday=04-04'
                        '&groups=oscar_best_actor_nominees&has=bio&bio=Movies&death_date=2008-01-22,2008-01-22&'
                        'gender=male&roles=tt6739646&adult=include')


        assert self.driver.current_url == expected_url, "Somthing Went Wrong"


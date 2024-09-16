import re
from playwright.sync_api import Page, expect


class LoginForm:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginForm()
        return cls.instance

    def set_context(self, context):
        self.context = context
        self.page = context.page

    URL = "https://login.posit.cloud"

    # Selectors
    INPUT_EMAIL = "input[name='email']"  # CSS selector
    INPUT_PASSWORD = "input[name='password']"  # CSS selector
    CONTINUE_BUTTON = "text=Continue"  # Searching by text content
    LOGIN_BUTTON = "//button[@type='submit']"  # XPath selector
    POSIT_CLOUD_LINK = "a.cloud"  # CSS selector

    def load(self):
        self.page.goto(self.URL)

    def set_username(self, phrase):
        self.page.locator(self.INPUT_EMAIL).fill(phrase)

    def click_continue_button(self):
        self.page.locator(self.CONTINUE_BUTTON).click()

    def click_login_button(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def set_password(self, phrase):
        self.page.locator(self.INPUT_PASSWORD).fill(phrase)

    def select_Posit_Cloud(self):
        self.page.locator(self.POSIT_CLOUD_LINK).click()

    def login(self, username, password):
        self.load()
        self.set_username(username)
        self.click_continue_button()
        self.set_password(password)
        self.click_login_button()
        self.select_Posit_Cloud()


login_form = LoginForm.get_instance()

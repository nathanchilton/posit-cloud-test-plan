import re
import time
from playwright.sync_api import Page, expect


class YourWorkspace:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = YourWorkspace()
        return cls.instance

    def set_context(self, context):
        self.context = context
        self.page = context.page

    BASE_URL = "https://posit.cloud"

    # Selectors
    NEW_SPACE_BUTTON = "div.navMenu button.newSpace"  # CSS selector
    NEW_PROJECT_BUTTON = "button[title='New Project']"  # CSS selector
    NEW_RSTUDIO_PROJECT_BUTTON = "button.newRStudioProject"  # CSS selector
    PROJECT_NAME = "button.projectTitle"  # CSS selector
    RSTUDIO_CONSOLE = "div#rstudio_workbench_panel_console"  # CSS selector
    RSTUDIO_PROJECT_FILE = "div[title='project.Rproj']"

    def load(self):
        self.page.goto(self.BASE_URL)

    def ide_iframe(self):
        return self.page.frame_locator("iframe#contentIFrame")

    def get_account_id(self):

        link_with_account_id = self.page.locator(
            "//a[contains(@href, '/accounts/')]"
        ).first

        href_attribute = link_with_account_id.get_attribute("href")
        m = re.search("/accounts/(\\d+)/", href_attribute)
        if not m:
            raise Exception("Account ID was not found in the DOM!")
        return m.group(1)

    def open_accounts_spaces_page(self):
        self.page.goto(f"{self.BASE_URL}/accounts/{self.get_account_id()}/spaces")

    def get_spaces_count(self):
        spaces_count_element = self.page.locator("div.sectionTitleDetails")
        expect(spaces_count_element).to_be_visible()

        # Apparently, this counter briefly shows 0, even when spaces do exist.
        # So, we will give it a little bit of time to check first.
        # If there is an API we could use for this, instead of using the frontend, let's use that instead.
        time.sleep(2)

        spaces_count = int(
            re.search("(\d+)", spaces_count_element.text_content()).group(1)
        )
        return spaces_count

    def delete_existing_space(self):
        if self.get_spaces_count() > 0:
            # TODO: Instead of using the browser interface, we could send a DELETE request like this:
            # https://api.posit.cloud/v1/spaces/485315?project_cleanup=delete

            self.page.locator("button#spaceDetailsDeleteSpaceButton").click()

            # Find prompt that asks if the user is "absolutely sure"
            absolutely_sure_message = self.page.get_by_text(
                re.compile(".*If you are absolutely sure.*")
            ).text_content()

            # Use a regular expression to extract the message that the user is instructed to type
            text_to_type = re.search('.*"([^"]+)".*', absolutely_sure_message).group(1)

            # Type in the requested text and click the Delete button
            self.page.locator("input#deleteSpaceTest").fill(text_to_type)
            self.page.locator("button#deleteSpaceSubmit").click()

    def click_new_space_button(self):
        self.page.locator(self.NEW_SPACE_BUTTON).click()

    def click_new_project_button(self):
        self.page.locator(self.NEW_PROJECT_BUTTON).click()

    def click_new_rstudio_project_button(self):
        self.page.locator(self.NEW_RSTUDIO_PROJECT_BUTTON).click()

    def project_name(self):
        return self.page.locator(self.PROJECT_NAME)

    def rstudio_console(self):
        return self.ide_iframe().locator(self.RSTUDIO_CONSOLE)

    def rstudio_project_file(self):
        return self.ide_iframe().locator(self.RSTUDIO_PROJECT_FILE)


your_workspace = YourWorkspace.get_instance()

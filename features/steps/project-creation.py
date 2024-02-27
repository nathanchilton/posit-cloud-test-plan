from behave import step
from playwright.sync_api import expect
from pages.login_form import login_form
from pages.your_workspace import your_workspace


@step('a Cloud Free user is on the "{page_name}" page')
def step_impl(context, page_name):
    if not page_name == "Your Workspace":
        raise Exception(
            f"Support has not been implemented for navigating to the '{page_name}' page."
        )

    login_form.set_context(context)
    login_form.login(context.USERNAME, context.PASSWORD)
    print("breakpoint")


@step("any previously-created space has been deleted")
def step_impl(context):
    your_workspace.set_context(context)
    your_workspace.open_accounts_spaces_page()
    your_workspace.delete_existing_space()


@step("the user creates a new space")
def step_impl(context):
    # click the New Space button
    your_workspace.click_new_space_button()
    # Use faker to generate a new space name
    context.new_space_name = context.fake.first_name()

    # type name into "input#name"
    context.page.locator("input#name").fill(context.new_space_name)

    # click "Create" button
    context.page.locator("dialog button[type='submit']").click()


@step("the user creates a New RStudio Project")
def step_impl(context):
    your_workspace.click_new_project_button()
    your_workspace.click_new_rstudio_project_button()


@step('a "{message}" message should appear temporarily')
def step_impl(context, message):
    message_element = context.page.locator(f"//*[contains(text(), '{message}')]")

    # Wait for message to appear
    expect(message_element).to_be_visible(timeout=10_000)

    # Wait for message to disappear
    expect(message_element).not_to_be_visible(timeout=60_000)


@step("a new RStudio project should load in the browser")
def step_impl(context):
    expect(your_workspace.rstudio_project_file()).to_be_visible(timeout=30_000)


@step('the project should be named "{project_name}"')
def step_impl(context, project_name):
    expect(your_workspace.project_name()).to_have_text(project_name)


@step("the rStudio console should be visible")
def step_impl(context):
    expect(your_workspace.rstudio_console()).to_be_visible()

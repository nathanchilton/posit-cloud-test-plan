# Test Plan for posit.cloud

This is an example of a manual test plan for posit.cloud, using Gherkin scenarios.

This project demonstrates a possible manual test plan for the [posit.cloud](https://posit.cloud/) web application, which could be executed in roughly 15 minutes.  It also contains one automated test, which can be executed using the instructions in this README file.  The automated test uses a Python-based framework ([Behave](https://behave.readthedocs.io/en/latest/)) and utilizes [Playwright](https://playwright.dev/python/) for browser automation.

## Manual Test Plan

The manual test plan is a series of `Scenarios` in a collection of `Feature` files, located in the `features` directory.  Each scenario could be run independently, but they are also written in such a way that there is a fairly smooth flow when executing the scenarios in the order they are presented, starting with `1-account-creation.feature` and ending with `6-current-user-menu.feature`, executing the scenarios in each file from top to bottom.

Testing the RStudio IDE within the Project interface was out-of-scope for this test plan.  Also, this test plan prioritizes speed, with a goal of completion within 15 minutes.  As such, a more comprehensive test plan should be considered, with attention focused on specific areas of risk, prior to any release.

## Executing the Automated Test

As a demonstration, the first scenario in `3-project-creation.feature` has been automated.

### Prerequisites

- Python 3 installed on macOS, Ubuntu Linux, or Windows
- Ensure that the `python` and `pip` commands are linked to Python 3
  - Depending on your system's configuration, you _may_ need to use `python3` and `pip3` instead of `python` and `pip`

### Installation

1. Clone this repository.

   ``` bash
   git clone git@github.com:nathanchilton/posit-cloud-test-plan.git
   cd posit-cloud-test-plan
   ```

2. Create an `env.json` file in the root of this project directory, with valid credentials for a "Cloud Free" posit.cloud account.

   The file should look like this, but contain real credentials:

   ``` JSON
      {
          "USERNAME": "username@example.com",
          "PASSWORD": "vszUd_LOL-Th1S1SN0TMyP@$$w0RDxxx!"
      }
    ```

3. Create a Python virtual environment using venv:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    Windows:

    ```bash
    venv\Scripts\activate
    ```

5. Ensure that `pip` is installed:

    ```bash
    python -m ensurepip --upgrade
    ```

6. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

7. Install the required browsers for Playwright:

    ```bash
    playwright install
    ```

### Running Tests

To execute the automated `Scenario`, we just need to tell `behave` to run all tests tagged with `@automated`:

``` bash
behave -t @automated
```

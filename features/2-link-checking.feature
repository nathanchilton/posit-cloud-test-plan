Feature: Space Creation

    Background:
        Given a Cloud Free user is on the "Your Workspace" page

    Scenario: Checking "Learn" section of Sidebar
        When user clicks the "Guide" link in the "Learn Navigation Menu"
        Then the Posit Cloud Guide guide should appear to load successfully
        And the appropriate sections of the guideNav should be highlighted as the user scrolls down the page

        When user clicks the "What's New" link in the "Learn Navigation Menu"
        Then the "What's New" content should appear to load successfully
        And the appropriate sections of the guideNav should be highlighted as the user scrolls down the page

        When user clicks the "Recipes" link in the "Learn Navigation Menu"
        Then the "Posit Recipes" content should appear to load successfully
        When the user clicks the "Read a CSV file (.csv)" link
        Then the "Read a CSV file (.csv)" content should appear to load successfully

    Scenario: Checking the "Info" section of the sidebar
        When user clicks the "Plans & Pricing" link in the "Info" menu section
        Then the Plan Table should be displayed
        And clicking each of the plans in the "Plan Navigation Menu" should display information about that plan





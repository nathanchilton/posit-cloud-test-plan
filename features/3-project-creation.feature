Feature: Project Creation

    Background:
        Given a Cloud Free user is on the "Your Workspace" page

    @automated
    Scenario: Creating a new space and a new RStudio project
        Given any previously-created space has been deleted
        When the user creates a new space
        And the user creates a New RStudio Project
        Then a "Deploying Project" message should appear temporarily
        Then a new RStudio project should load in the browser
        And the project should be named "Untitled Project"
        And the rStudio console should be visible

    Scenario: Creating a New Project from Template: "R Markdown Document Publishing with RStudio"
        When the user creates a new project using the "R Markdown Document Publishing with RStudio" template
        Then a new project should load in the browser
        And the project should be named "Untitled Project"

    Scenario: Creating a New Project from Template: "Data Analysis in Python with pandas"
        When the user creates a new project using the "Data Analysis in Python with pandas" template
        Then a modal dialog should explain that "Jupyter projects are currently in beta and are not available in Cloud Free or Cloud Student accounts."

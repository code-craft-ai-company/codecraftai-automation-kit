# Personality
AI Agents working in this repository should refer to themselves as an agent named 'AutomationX'.

# Rules
- Look in the '<repository>/specs' folder for specification files that help to steer development work
- Look in the '<repository>/userguide' folder for files containing standards and conventions
- Look in the '<repository>/prompts' folder for pre-build prompts
- Files inside the .venv folder should not be modified, they are modified by the setup scripts

# Project Overview
This folder contains the source code for the Automation Mojo 'Automation Kit' project.  The 'Automation Kit' repository serves as a template repository
that companies and organizations can utilize to get test automation projects off the ground and headed in a great direction very rapidly.

# Testing Conventions
The 'AutomationKit' includes both the 'testbase' and 'testplus' test frameworks.


# Code Naming Conventions
The code naming conventions of this repository follows the [Automation Mojo Python Naming Conventions](userguide/10-02-naming-conventions.rst)

# Code Structure
The code structure of this repository follows the [Automation Mojo Python Code Structure Standards](userguide/10-01-code-organization.rst)

Remember to make the test hierarchy match the source hierarchy when adding test files.  For example:

File to test: 'source/packages/automojo/interop/protocols/dns/dnsquestion.py'
Test file location: 'source/testroots/automojo/interop/protocols/dns/test_dnsquestion.py'

# Coding Standards
The code in this repository is meant to be utilized by testing tools and test frameworks.  Therefore, the code must prioritize:

*  debuggability over performance
*  readability over conciseness

For all the code in this repository, follow the coding standards specified at [Coding Standards](userguide/10-00-coding-standards.rst)

# Pack Management
This project utilizes python poetry for package management.  The dependencies are updated with the command:

```
    poetry update --no-cache
```

# Writing Tests

A 'testbase' and 'testplus' test take the form of a function with a 'test_' prefix like so:

```
def test_something():
    return
```

If a test raises an AssertionError, then it checked something and the check failed.  That is a Failure.  If the test raises any other exception, then the test framework treats that as an Error much like the 'unittest' framework does.

You can create resource factories.

```
@testbase.register.resource_factory()
def create_landscape(constraints={}) -> Generator[Landscape, None, None]:
    """
        Creates the global :class:`Landscape` instance.

        :param constraints: Optional dictionary of constraints used while constructing the Landscape.

        :returns: A generator yielding the Landscape object.
    """
    lscape = LandscapeSingleton()
    yield lscape
```

You can create resources using the factories in a scope in the test tree.  Resources have scope for every test below where they are declared.

```
testbase.originate.parameter(create_landscape, identifier='lscape')
```

To use a resource in a descendant test scope, just reference it by name in the test function signature like:

```
def test_use_landscape(lscape: Landscape):

    blah = lscape.get_something()
    testbase.assert_equal(blah is not None, True)
    return

```

The test tree should only contain resource origination declarations and tests.  It should not contain factories unless the usage of the factory is very isolated.  It is preferable to place factories in a folder such as a factory that creates the AutomationPodSimple object might be located at 'source/testroots/automojo/testshared/factories/automationpods/automationpodsimple.py'

# Evaluating Test Results
There is a machine processable JSOS stream file in the output folder.

"*outputfolder*/testrun_results_stream.jsos"

JSOS (JSON Object Stream) consists of a stream of JSON objects seperated by the the ASCII record seperator character.  When a
test starts it writes a preview to the stream.  The test preview has a 'result' equal to 'UNSET'.  Example Preview:

```
{
    "name": "automojo.tests.singlehost.interop.protocols.dns.test_dnsaddress#test_write_passes_address",
    "monikers": [],
    "pivots": {},
    "instance": "abb868e4-ce97-4bae-b0af-715da0d61d92",
    "parent": "5aad244e-41dc-438f-97a6-bd8365cccdd2",
    "rtype": "TEST",
    "result": "UNSET",
    "start": "2025-07-15T22:07:03.275239",
    "stop": ""
}
```

When a test finishes it writes a result to the stream.  A test result will always have a 'detail' attribute. Example Result:

```
{
    "name": "automojo.tests.singlehost.interop.protocols.dns.test_dnsaddress#test_write_passes_address",
    "monikers": [],
    "pivots": {},
    "instance": "abb868e4-ce97-4bae-b0af-715da0d61d92",
    "parent": "5aad244e-41dc-438f-97a6-bd8365cccdd2",
    "rtype": "TEST",
    "result": "PASSED",
    "start": "2025-07-15T22:07:03.275239",
    "stop": "2025-07-15T22:07:03.276034",
    "detail": {
        "errors": [],
        "failures": [],
        "warnings": []
    }
}
```

# Environment Setup

## Codex Container Setup
When work is being done on this repository using the Codex web environment.  Use the script 'development/setup-agent-container' as the setup script for Codex containers.


# Environment Setup
When checking out the code for this repository in order to test changes, agents must:

* run the 'repository-setup/rehome-repository' script.  It creates a needed '.env' file.
* run the 'development/setup-envrionment' script in order to create the virtual environment.

# Change Recommendations
Before making a recommendation to change a file.  Make sure you have the latest version of the file.


# Project Specific Rules


# Pull Request Guidelines


# Packaging
Currently, this package is utilized using a reference to the github repository.  It is currently not published.

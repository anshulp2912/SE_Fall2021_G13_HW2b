# HELLO!! WELCOME TO CONTRIBUTING TO CALCULATOR :)
## Thanks for being here and taking your time to contribute.  <br>
The following is a set of guidelines for contributing to "Calculator" and its packages, which are hosted in the [SE_Fall2021_G13_HW2b](https://github.com/anshulp2912/SE_Fall2021_G13_HW2b) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request. <br>
## Table of Contents
[Code of Conduct](https://github.com/anshulp2912/SE_Fall2021_G13_HW2b/blob/main/CODE_OF_CONDUCT.md) <br>
[How can I Contribute](https://github.com/anshulp2912/SE_Fall2021_G13_HW2b/blob/main/CONTRIBUTING.md#how-can-i-contribute)

## Code of Conduct
This project and everyone participating in it is governed by the [Code of Conduct](https://github.com/anshulp2912/SE_Fall2021_G13_HW2b/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to anshulp2912@gmail.com.
## How can I Contribute
#### Reporting Bugs 
This section gives detailed information on how to report bugs. Reporting a bug will help the community and maintainers of the repository. <br>
Before reporting any bug, make sure it is correct and you have all the details with you. Fot creating any bug report, please fill out [the required template](https://github.com/atom/.github/blob/master/.github/ISSUE_TEMPLATE/bug_report.md). This template will give us necessary information to help solve a bug faster.

#### Before Submitting A Bug Report
The following is a list of items you need to check before submitting a bug report. <br>

[debugging guide](https://flight-manual.atom.io/hacking-atom/sections/debugging/). Check out this debugging guide, which helps you to find the cause of the problem and you may fix it by yourself manually. <br>
[cursory search](https://github.com/search?q=+is%3Aissue+user%3Aatom) A cursory search is necessary to check if the reported bug is already mentioned before or not. You can add to the existing bug report if the issue is still open.

#### To Submit A Good Bug Report
[GitHub issues](https://guides.github.com/features/issues/) You can trach the bugs from this. For the repository that has bug, create an issue and fill out [the template](https://github.com/atom/.github/blob/master/.github/ISSUE_TEMPLATE/bug_report.md) to give details of the bug.


* To identify the problem, give the issue a clear and informative term. <br>
* Describe in as much detail as possible to duplicate the problem. Explain the problem and explain about the exact command sused in the terminal which caus ethe bug to occur.
* To demonstrate the steps, give specific examples. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* Specify what is the problem beavior and what you expected to see and why
* If possible, include screenshots and animated GIFs that clearly demonstrate the problem. [this tool](https://www.cockos.com/licecap/)- to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* To include a crash report, add a stack trace from the operating system. For macOS, `Console.app` under "Diagnostic and usage information" > "User diagnostic reports" has crash report. Include the crash report in the issue in a [code block](https://help.github.com/articles/markdown-basics/#multiple-lines), a [file attachment](https://help.github.com/articles/file-attachments-on-issues-and-pull-requests/), or put it in a [gist](https://gist.github.com/) and provide link to that gist.
* For performance or memory issues, include a [CPU profile capture](https://flight-manual.atom.io/hacking-atom/sections/debugging/#diagnose-runtime-performance) with your report.

Provide more context by answering these questions: <br>
* If the problem started happening recently then try downloading the old version of the packages and the code.
* Include details about your configuration and environment.
* What is the name and version of the OS you're using?
* Are you running the project in a virtual environment?
* Which packages have installed in your system? You can get a list of packages installed by running 'apm list --installed'

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Atom, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one. When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion). Fill in [the template](https://github.com/atom/.github/blob/master/.github/ISSUE_TEMPLATE/feature_request.md), including the steps that you imagine you would take if the feature you're requesting existed.

#### Before Submitting An Enhancement Suggestion

* **Check the [debugging guide](https://flight-manual.atom.io/hacking-atom/sections/debugging/)** for tips — you might discover that the enhancement is already available. Most importantly, check if you're using [the latest version of Atom](https://flight-manual.atom.io/hacking-atom/sections/debugging/#update-to-the-latest-version) and if you can get the desired behavior by changing [Atom's or packages' config settings](https://flight-manual.atom.io/hacking-atom/sections/debugging/#check-atom-and-package-settings).
* **Check if there's already [a package](https://atom.io/packages) which provides that enhancement.**
* **Determine [which repository the enhancement should be suggested in](#atom-and-packages).**
* **Perform a [cursory search](https://github.com/search?q=+is%3Aissue+user%3Aatom)** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined [which repository](#atom-and-packages) your enhancement suggestion is related to, create an issue on that repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of Atom which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most Atom users and isn't something that can or should be implemented as a [community package](#atom-and-packages).
* **List some other text editors or applications where this enhancement exists.**
* **Specify which version of Atom you're using.** You can get the exact version by running `atom -v` in your terminal, or by starting Atom and running the `Application: About` command from the [Command Palette](https://github.com/atom/command-palette).
* **Specify the name and version of the OS you're using.**

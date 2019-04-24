# Contribution Guide

Thank you for your interest in contributing to Mobile App Control Center, Systers! There are always bugs to file; bugs to fix in the code; improvements to be made to the documentation; and more.


The instructions given below are for software developers who want to work on [our current code](https://github.com/systers/macc).

## What to work on

1. You can check the [opened issues](https://github.com/systers/macc/issues). They are related to the existing code or for tracking new features.

2. Claim the issue, after approval, work on it and send a pull request.

3. Create a new issue, a community member will get back to you and once approved, send a pull request for the same.

4. All the PRs are needed to be sent to the [develop](https://github.com/systers/macc) branch.

## Avoid doing the following mistakes
1. Fix a new issue and submit a PR without reporting and getting it approved at first.

2. Fix an issue assigned to somebody else and submit a PR before the assignee does. 

3. Report issues which are previously reported by others. (Please check the closed issues too before you report an issue).

4. Suggest completely new developments in the issue list. (Please use the mailing list for this kind of suggestions. Use issue list to suggest bugs/features in the already implemented sections.)

## Best Practices
### For Issue Reporting
1. Go through the Issue List and see whether the issue you found or any related issue is already reported.

2. If you don't find the issue you are reporting in issue list, check whether it is reported and closed (present in closed issue list).

3. If the issue is new, report the issue as a new one with following:
     * Screen shot if possible
     * Short description for the title
     * A detailed description with steps to recreate the issue (for bugs)
     * A description of how the issue will improve the application ( for enhancements)

### For Pull Requests
1. Use meaningful commit messages.

2. Do not over commit. (Do not include multiple commits for a small change)

3. Do not add the merge commits to the PR.

4. Usually use a single commit for a single issue, unless the issues are related or contain a significant code change.

5. There are certain kind of files you do not add to source control (Like the vitual environment folder). If you already don't know about them, please do a quick search and find them and remove them from your commit. 

6. When sending a PR have an appropriate title referencing the issue which it solves.

7. If it is a UI change, add a screen shot of the new/fixed UI.

8. Have a short description on what has gone wrong (like a root cause analysis and description of the fix), if that information is not already present in the issue.

9. Do not ask us to review it in a separate comment. We will review it anyway.


## Coding Style and Standards

Follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) and [PEP257](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings) Style Guides.

Most important things:

 1. Separate top-level function and class definitions with two blank lines.

 2. Keep lines shorter than 100 characters when possible (especially at Python code).

 3. Use whitespace between comma and separate values.

 4. Give classes CamelCase naming.

 5. Give functions lowercase namings.

 6. Refrain from suggesting completely new developments in the issue list. Make you discuss them once in our [slack channel](systers.io/slack-systers-opensource/).



## Git workflow

When you want to start contributing, you should [follow the instructions](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md). After that, follow these steps.

Set your cloned fork to track upstream changes (changes to the main repository), then fetch and merge from the upstream branch:

    `$ git remote add --track upstream https://github.com/systers/macc.git`
    `$ git fetch upstream develop`
    `$ git merge upstream/develop`


Set up a branch for a particular set of changes and switch to it:

    `$ git checkout -b my_branch`

It is important that you create a new branch from the default (develop) branch which is the exact copy of the upstream, else you might mix up commits from different branches. So switch to `develop` branch before creating a new one. 

Run `git remote -v` to check the status, you should see something like this:

    > origin https://github.com/YOUR_USERNAME/macc.git (fetch)

    > origin https://github.com/YOUR_USERNAME/macc.git (push)

    > upstream https://github.com/systers/macc.git (fetch)

    > upstream https://github.com/systers/macc/git (push)

Code!

Commit the changes.

    `$ git add my_changed_files`
    `$ git commit -m "A small but relevant commit message"`


When you're done, figure out how many commits you've made:

    `$ git log`

Push the changes to your forked repository.

    `$ git push origin my_branch`

Issue a pull request on GitHub.

Wait to hear from one of the collaborators.

If you're asked to change your commit message, you can amend the message and commit:

    `$ git commit --amend`
    `$ git push -f origin my_branch`

If you're asked to make changes on your code you can stage them and amend the commit:
    
    `$ git add my_changed_files`
    `$ git commit --amend`
    `$ git push -f origin my_branch`

Avoid doing `$ git add --all` since it also adds the changes needed specifically for your development environment. Manually go through the changes once before you stage them. In case you accidentally stage a file you were not supposed to, you have to unstage all the files again. This can be done by:

    `$ git reset --hard HEAD`

If you need more references and Git expertise, a good resource is the [Git Book](https://git-scm.com/book/en/v2).

##Troubleshooting
If there are any other questions or concerns, you can either send a mail to the systers-dev mailing list  or join #macc channel in our slack group. To get an invitation to the slack group [click here] (http://systers.io/slack-systers-opensource/). 




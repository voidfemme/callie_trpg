
# Collaborative Git Workflow

Collaborating on a git project involves making changes on a branch and merging them into the main codebase. It's a good practice to always work on a separate branch, not directly on the `master` branch, to avoid potential conflicts and keep the main codebase stable.

Here are the steps to collaborate using git:

1. Clone the Repository

   `git clone `<repository URL>`
   
2. Create a Branch

   `git checkout -b `<branch-name>`
   
3. Make Changes

   Make changes to the code in your preferred text editor.

4. Commit Changes

   `git add .`
   `git commit -m "Commit message"`
   
   The "Commit message" should be a short description of the changes you made.

5. Pull the Latest Code

   `git pull origin master`
   
   Replace `master` with your default branch name if it's different. This ensures your branch has the latest changes from `master` before you push your changes.

6. Resolve Conflicts

   If there are conflicts between your changes and the changes on `master`, Git will indicate where these conflicts are in your files. Conflicts are marked like this:

   `<<<<<<< HEAD`
   Your changes`
   `=======`
   Changes on the remote repository`
   `>>>>>>> commit_id`

   Everything between `<<<<<<< HEAD` and `=======` is your changes, and everything between `=======` and `>>>>>>> commit_id` are the changes from the remote repository. To resolve the conflicts, you need to manually edit the file to keep the changes you want and remove the conflict markers.

   After you've resolved all the conflicts:

   `git add .`
   `git commit -m "Resolved merge conflicts"`
   
   In some cases, it might be easier to use a merge tool to visualize and resolve conflicts. Many text editors and IDEs have built-in tools for this, or you can use a standalone tool.

7. Push Your Branch

   `git push origin `<branch-name>`

8. Create a Pull Request

   Go to the repository on GitHub and create a pull request. This is a request to merge your changes into the `master` branch.

9. Review Changes

   Ideally, you or someone else should review the changes before they're merged. They can leave comments directly on the pull request.

10. Merge the Pull Request

    Once you're satisfied with the changes, you can merge the pull request. This will integrate your changes into the `master` branch.

11. Delete the Branch

    After the pull request has been merged, you can delete the branch you were working on.

12. Pull the Changes

    `git pull origin master`

13. Start Again

    For the next set of changes, go back to step 2. Always ensure you're working with the latest version of the code before creating a new branch.

# GitHub Desktop Instructions

If you're using GitHub Desktop, the steps are slightly different but follow the same general workflow.

1. Clone the Repository

   Click `File -> Clone repository` from the menu, select the repository from the list and click `Clone`.

2. Create a Branch

   Click `Branch -> New branch` from the menu and enter a branch name, then click `Create branch`.

3. Make Changes

   Make changes to the code in your preferred text editor.

4. Commit Changes

   Enter your commit message in the bottom left field and click `Commit to `<branch-name>``.

5. Pull the Latest Code

   Click `Repository -> Pull` from the menu.

6. Resolve Conflicts

   If there are conflicts, GitHub Desktop will highlight the conflicted files. Click on the `Conflicted` icon next to the file name to open the conflict resolution tool.

7. Push Your Branch

   Click `Repository -> Push` from the menu.

8. Create a Pull Request

   Click `Branch -> Create Pull Request` from the menu.

9. Review Changes

   The pull request can be reviewed on GitHub's web interface.

10. Merge the Pull Request

    After the review, the pull request can be merged on GitHub's web interface.

11. Delete the Branch

    After the pull request has been merged, you can delete the branch on GitHub's web interface.

12. Pull the Changes

    Click `Repository -> Pull` from the menu.

13. Start Again

    For the next set of changes, go back to step 2.

# Protecting the Master Branch on GitHub

To ensure that changes are always reviewed before they're merged into the `master` branch, you can set up branch protections on GitHub.

Here are the steps to set up branch protection:

1. Go to your repository on GitHub.
2. Click on `Settings`.
3. In the left sidebar, click on `Branches`.
4. Under "Branch protection rules", click on `Add rule`.
5. In the "Branch name pattern", type the name of the branch you want to protect, for example, `master`.
6. Check the boxes according to your preferred protection rules. Typical selections include:
   - Require pull request reviews before merging: This forces all changes to be made through pull requests and requires at least one approved review before the changes can be merged.
   - Dismiss stale pull request approvals when new commits are pushed: If new commits are added to a pull request after a review, the approval is dismissed and must be done again.
   - Require status checks to pass before merging: This requires all continuous integration checks to pass before a pull request can be merged.
   - Require branches to be up to date before merging: This requires the branch to be up to date with the `master` branch before a pull request can be merged.
   - Restrict who can push to matching branches: This allows you to specify which users or teams can push to the protected branch.
7. Click on "Create" to save the rule.

With these settings in place, all changes to the `master` branch must be made through a pull request, ensuring that at least one person reviews the changes. It also means that the branch cannot accidentally be deleted, and force pushes are prevented.

Remember that these rules apply to everyone, including repository owners and administrators. If you want to make a direct push to the protected branch or perform other actions that are restricted by the branch protections, you'll need to temporarily disable the protections, perform your action, then re-enable them.

## Resolving Being "Ahead" or "Behind" a Branch

If your branch says it's "ahead" or "behind" another branch, it means there have been commits on both branches that aren't shared with each other. 

For example, if you're one commit "ahead" of `master`, it means you have one commit on your branch that hasn't been merged into `master` yet. If you're one commit "behind" `master`, it means there's one commit on `master` that you haven't merged into your branch yet.

Here's how to resolve being "ahead" or "behind" a branch:

1. Checkout to the branch that is ahead or behind.

   `git checkout `<branch-name>`

2. If you're behind, merge the branch you're behind to your current branch:

   `git merge master`

   This will bring your branch up to date with `master`.

3. If you're ahead, you can push your changes to the remote repository:

   `git push origin `<branch-name>`

   Then, create a pull request on GitHub to merge your changes into `master`.

Remember that if you're both "ahead" and "behind" at the same time, you'll need to do both steps.

# Conclusion

With these practices in place, you'll ensure that your git workflow is organized and that your `master` branch remains stable and reliable for production use. Happy coding!

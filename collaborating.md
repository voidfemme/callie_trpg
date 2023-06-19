# Collaborative Git Workflow

1. **Clone the Repository**

   ```bash
   git clone <repository URL>
   ```

2. **Create a Branch**

   ```bash
   git checkout -b <branch-name>
   ```

3. **Make Changes**

4. **Commit Changes**

   ```bash
   git add .
   git commit -m "Commit message"
   ```

5. **Pull the Latest Code**

   ```bash
   git pull origin master
   ```

   > Replace `master` with your default branch name if it's different.

6. **Resolve Conflicts**

   > If there are conflicts between your changes and the changes that have been pushed since you last pulled, Git will indicate where these conflicts are in your files.

   > Conflicts are marked in your files like this:

   ```bash
   <<<<<<< HEAD
   Your changes
   =======
   Changes on the remote repository
   >>>>>>> commit_id
   ```

   > Everything between `<<<<<<< HEAD` and `=======` is your changes, and everything between `=======` and `>>>>>>> commit_id` are the changes from the remote repository.

   > To resolve the conflicts, you need to manually edit the file to keep the changes you want, and remove the conflict markers. Once you have resolved all conflicts, you can continue with the commit.

   > After you've resolved all the conflicts:

   ```bash
   git add .
   git commit -m "Resolved merge conflicts"
   ```

   > Note: In some cases, it might be easier to use a merge tool to visualize and resolve conflicts. Many text editors and IDEs have built-in tools for this, or you can use a standalone tool.

7. **Push Your Branch**

   ```bash
   git push origin <branch-name>
   ```

8. **Create a Pull Request**

   > Go to the repository on GitHub and create a pull request. This is a request to merge your changes into the `master` branch.

9. **Review Changes**

   > Ideally, you or someone else should review the changes before they're merged. They can leave comments directly on the pull request.

10. **Merge the Pull Request**

    > Once you're satisfied with the changes, you can merge the pull request. This will integrate your changes into the `master` branch.

11. **Delete the Branch**

    > After the pull request has been merged, you can delete the branch you were working on.

12. **Pull the Changes**

    ```bash
    git pull origin master
    ```

13. **Start Again**
    > For the next set of changes, go back to step 2. Always ensure you're working with the latest version of the code before creating a new branch.

## GitHub Desktop Instructions

1. **Clone the Repository**

   > Click `File -> Clone repository` from the menu, select the repository from the list and click `Clone`.

2. **Create a Branch**

   > Click `Branch -> New branch` from the menu and enter a branch name, then click `Create branch`.

3. **Make Changes**

4. **Commit Changes**

   > Enter your commit message in the bottom left field and click `Commit to <branch-name>`.

5. **Pull the Latest Code**

   > Click `Repository -> Pull` from the menu.

6. **Resolve Conflicts**

   > If there are conflicts, GitHub Desktop will highlight the files where conflicts exist. Open these files in a text editor, resolve the conflicts, then return to GitHub Desktop. Check the boxes next to the files you resolved, enter a commit message, then click `Commit to <branch-name>`.

7. **Push Your Branch**

   > Click `Repository -> Push` from the menu.

8. **Create a Pull Request**

   > Click `Branch -> Create Pull Request` from the menu. This will open the repository on GitHub in your browser, where you can create the pull request.

9. **Review Changes**

   > Ideally, you or someone else should review the changes before they're merged. They can leave comments directly on the pull request on GitHub.

10. **Merge the Pull Request**

    > Once you're satisfied with the changes, you can merge the pull request on GitHub. This will integrate your changes into the `master` branch.

11. **Delete the Branch**

    > After the pull request has been merged, you can delete the branch in GitHub Desktop by clicking `Branch -> Delete Branch`.

12. **Pull the Changes**

    > Click `Repository -> Pull` from the menu.

13. **Start Again**
    > For the next set of changes, go back to step 2. Always ensure you're working with the latest version of the code before creating a new branch.

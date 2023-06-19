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
   git pull origin main
   ```

   > Replace `main` with your default branch name if it's different.

6. **Resolve Conflicts**

   > If there are any conflicts between your changes and changes that have been pushed since you last pulled, you'll need to resolve them manually. Git will indicate where the conflicts are in your files.

7. **Push Your Branch**

   ```bash
   git push origin <branch-name>
   ```

8. **Create a Pull Request**

   > Go to the repository on GitHub and create a pull request. This is a request to merge your changes into the `main` branch.

9. **Review Changes**

   > Ideally, you or someone else should review the changes before they're merged. They can leave comments directly on the pull request.

10. **Merge the Pull Request**

    > Once you're satisfied with the changes, you can merge the pull request. This will integrate your changes into the `main` branch.

11. **Delete the Branch**

    > After the pull request has been merged, you can delete the branch you were working on.

12. **Pull the Changes**

    ```bash
    git pull origin main
    ```

13. **Start Again**
    > For the next set of changes, go back to step 2. Always ensure you're working with the latest version of the code before creating a new branch.

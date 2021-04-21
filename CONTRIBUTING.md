# Contributing to datamol

Thank you for your interest in contributing to datamol!
When contributing to this repository, please first discuss the change you wish to make via issue. 


## Pull Request Process
Before starting work on a PR, it's highly advisable to go through existing PRs and issues to ensure that nobody else is already working on the same thing. If unsure, it's better to open an issue to get some feedback.

Proficiency in basic `git` is necessary to contribute to datamol. You can use the git manual by typing `git --help` or use [Pro Git](https://git-scm.com/book/en/v2) book to learn the basics.

Follow these steps to start contributing:

1. Fork the [repository](https://github.com/datamol-org/datamol/) by
   clicking on the 'Fork' button on the repository's page. This creates a copy of the code
   under your GitHub user account.

2. Clone your fork to your local disk, and add the base repository as a remote:
   
   ```bash
   $ git clone https://github.com/<your Github handle>/datamol.git
   $ cd datamol
   $ git remote add upstream https://github.com/datamol-org/datamol/
   ```

3. Create a dev environment:

   ```bash
	$ conda create -n datamol
	$ conda activate datamol
	$ mamba env update -f env.yml
	$ conda deactivate && conda activate datamol
	$ pip install -e .
   ```
4. Create a new branch to hold your development changes:

   ```bash
   $ git checkout -b a-descriptive-name-for-your-changes
   ```

5. Develop the features on your branch.

   As you are writing code and adding new files to the repo, ensure that the tests pass. In the `datamol` folder run 

   ```bash
   $ pytest
   ```

6. Updating the docs
   If the changes you made have to be updated on the docs, go to the `/docs` folder and update the required file. To check your changes on the docs you can build and serve the documentation locally with:
   
   ```bash
   $ python -m datamol._mkdocs
   $ mike serve
   ```

7. Pushing your changes:

   Once you're happy with your changes, add changed files using `git add` and
   make a commit with `git commit` to record your changes locally:

   ```bash
   $ git add file_changed.py
   $ git commit -m " descriptive-commit-message "
   ```

   ```bash
   $ git fetch upstream
   $ git rebase upstream/master
   ```

   Push the changes to your account using:

   ```bash
   $ git push -u origin a-descriptive-name-for-my-changes
   ```

8. Once you are satisfied, go to the webpage of your fork on GitHub. Click on 'Pull request' to send 	your changes to the project maintainers for review.

9. It's normal for maintainers to request changes. So everyone can see the changes in the PR, work in your local
   branch and push the changes to your fork. They will automatically appear in
   the pull request.

### Tests
A test suite is present to test the library behavior and several examples. The library tests can be found in the [tests folder](https://github.com/datamol-org/datamol/tree/master/tests).

To run tests you can use pytest by simply

```bash
$ pytest
```
If you want to contribute to writing tests, a good and easy example which you can refer to is the `test_mol.py` file. 


For more info visit:

homepage: https://doc.datamol.io/stable/index.html

website: https://datamol.io/



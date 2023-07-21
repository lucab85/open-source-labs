Suppose your GitHub account clones a repository called `git-playground` from `https://github.com/labex-labs/git-playground.git`.
1. Navigate to the repository directory and configure your GitHub identity .
2. Switch to the `feature-1` branch and add "hello" to the `README.md` file, add it to the staging area and commit, the commit message is "Add new content to README.md".
3. Switch to the `feature-2` branch and add "world" to the `index.html` file, add it to the staging area and commit, the commit message is "Update index.html file".
4. View the difference between the two branches.
```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
 # git-playground
 Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
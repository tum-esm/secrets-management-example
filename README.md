**You should not include secrets in your code!**

`bad-example/` includes an example of how _not_ to manage secrets. The will be part of the code's version history and visible to anyone with read-permissions on that repo. Selective CI tools are allowed to read our repositories and it is hard to keep track of secrets like that. Secrets leaks can happen very easily. Open sourcing a repository is not possible.

`good-example/` includes an example of how you _can_ manage secrets. Manage them in a separate file and do not include that separate file in a version control system. Include a template of that required file in your repository.

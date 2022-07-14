**You should not include secrets in your code!**

`bad-example/` includes an example of how _not_ to manage secrets. The secrets will be part of the code's version history and be visible to anyone with read-permissions on that repo - even after you remove/change them. Selective CI tools are allowed to read our repositories and it is hard to keep track of secrets like that. Secrets leaks can happen very easily. Open sourcing the repository is not easily possible.

`good-example-config-file/` includes an example of how you _can_ manage secrets. Keep them in a separate file and do not include that separate file in the version control system. Include a template of that required file in your repository.

`good-example-env-variables/` shows how you can use a local `.env` file (if it exists) or environment variables for your secrets. This requires installing the `python-dotenv` library.

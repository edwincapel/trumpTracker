# Create README.md


# Move out of `data` directory

```sh
git mv data/* .
```

# Don't include `articles.json` into git

```sh
cat "data/*" >> .gitignore
```

# Include Install

```sh
pip3 install feedparser
```

# Don't do a string search to see if entry already exists, just do a key lookup

# Scheduler should be moved into shell, and not run as python code

For the most part this is bad practice.

You should let the shell take care of executing and polling.

This gives you the flexibility of configuring the scheduling outside of code.


```sh
watch -n 60 python3 app.py
```

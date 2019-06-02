# GitHub clone
Git clone any sub-directories of any GitHub repository (at any reference) without having to clone the entire repository.
Uses the GitHub API to recursively clone the sub-directories tree and files.

# Rate limit
The GitHub API imposes a [rate limiting](https://developer.github.com/v3/#rate-limiting) of up to 60 requests per hour applies but can be increased to up to 5000 requests per hour using an _OAuth token_ (to get one see https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).

# Private repositories
To clone private repositories you need to supply an _OAuth token_ for an account with access to the private repository (to get one see https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).

# Installation


# Usage
```
GitHub clone (git.io/ghclone)

Usage:
  ghclone.py <url> [-t | --token=<token>]
  ghclone.py (-h | --help)
  ghclone.py (-v | --version)

Examples:
  ghclone.py https://github.com/HR/Crypter/tree/master/app
  ghclone.py https://github.com/HR/Crypter/tree/dev/app
  ghclone.py https://github.com/HR/Crypter/tree/v3.1.0/build
  ghclone.py https://github.com/HR/Crypter/tree/cbee54dd720bb8aaa3a2111fcec667ca5f700510/build
  ghclone.py https://github.com/HR/Picturesque/tree/master/app/src -t li50d67757gm20556d53f08126215725a698560b

Options:
  -h --help           Show this screen.
  -v --version        Show version.
  -t --token=<token>  Set a GitHub OAuth token (see https://developer.github.com/v3/#rate-limiting).
```


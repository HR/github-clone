# GitHub clone
Git clone any sub-directories of any GitHub repository (at any reference) without having to clone the entire repository.
Uses the GitHub API to recursively clone the sub-directories tree and files.

## Rate limit
The GitHub API imposes a [rate limiting](https://developer.github.com/v3/#rate-limiting) of up to 60 requests per hour applies but can be increased to up to 5000 requests per hour using an _OAuth token_ (to get one see https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). 

GitHub clone makes an initial request to fetch repo metadata and then, a request for every subfolder in the repo. The request to download the files within the folders are not counted against the rate limit so in most cases (i.e. the folder/repo you're trying to clone has less than 60 subfolders) the rate limit should not be a problem.

## Private repositories
To clone private repositories you need to supply an _OAuth token_ for an account with access to the private repository (to get one see https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).

# Installation
Install the script via the `pip`:
```
pip install git+git://github.com/HR/github-clone#egg=ghclone
```
or via `pipsi`:
```
pipsi install git+git://github.com/HR/github-clone#egg=ghclone
```
Uses Python 3.3+

# Usage
```
GitHub clone (git.io/ghclone)

Usage:
  ghclone <url> [-t | --token=<token>]
  ghclone (-h | --help)
  ghclone (-v | --version)

Examples:
  ghclone https://github.com/HR/Crypter/tree/master/app
  ghclone https://github.com/HR/Crypter/tree/dev/app
  ghclone https://github.com/HR/Crypter/tree/v3.1.0/build
  ghclone https://github.com/HR/Crypter/tree/cbee54dd720bb8aaa3a2111fcec667ca5f700510/build
  ghclone https://github.com/HR/Picturesque/tree/master/app/src -t li50d67757gm20556d53f08126215725a698560b

Options:
  -h --help           Show this screen.
  -v --version        Show version.
  -t --token=<token>  Set a GitHub OAuth token (see https://developer.github.com/v3/#rate-limiting).
```
# License
Copyright (C) 2019 Habib Rehman (https://git.io/HR)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


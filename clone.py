import requests
import re
import sys
import os
import errno


GH_API_BASE_URL = 'https://api.github.com'
GH_REPO_CONTENTS_ENDPOINT = GH_API_BASE_URL + '/repos/{}/{}/contents'
BASE_NORMALIZE_REGEX = re.compile(r'.*github\.com\/')


def exit_with_m(m='An error occured'):
    print(m)
    sys.exit(1)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as err:  # Python >2.5
        if err.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def clone_file(download_url, file_path):
    """
    Clones the file at the download_url to the file_path
    """
    print('Cloning file', file_path)
    r = requests.get(download_url, stream=True)
    try:
        r.raise_for_status()
    except Exception as e:
        exit_with_m('Failed cloneing ' + download_url, e)

    with open(file_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

def clone(base_url, path=None):
    """
    Recursively clones the path
    """
    print('Cloning directory', path)
    req_url = base_url if not path else os.path.join(base_url, path)
    # Get path metadata
    r = requests.get(req_url)
    try:
        r.raise_for_status()
    except Exception as e:
        exit_with_m('Failed fetching metadata of dir: ', e)
    repo_data = r.json()

    # Create path locally
    mkdir_p(path)

    if isinstance(repo_data, list):
        # Recursively clone content
        for item in repo_data:
            if item['type'] == 'dir':
                # Fetch dir recursively
                clone(base_url, item['path'])
            else:
                # Fetch the file
                clone_file(item['download_url'], item['path'])


###
# Main
###
arg_len = len(sys.argv)
if arg_len >= 2:
    # Github URL
    gh_url = sys.argv[1]
    # Normalize & parse input
    normal_gh_url = re.sub(BASE_NORMALIZE_REGEX, '', gh_url).replace('/tree', '')
    gh_url_comps = normal_gh_url.split('/')
    user, repo = gh_url_comps[:2]
    branch = gh_url_comps[2]
    path = os.path.join(*gh_url_comps[3:])
else:
    exit_with_m('Nothing to clone :(')

api_req_url = GH_REPO_CONTENTS_ENDPOINT.format(user, repo)
print("Cloning into '%s'..." % path)
clone(api_req_url, path)
print("done.")
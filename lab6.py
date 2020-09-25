# Use environment variables to perform read/write to result files
# process.env.TEST_FILE_NAME is the name of THIS file (the unit tests you're writing - use it as compile command)
# process.env.USER_CODE_DIR is the directory path of user's code. Use it to import/run user specific code
# process.env.PUBLIC_PORT is the publicly accessible port on localhost for user's server. Use it to perform HTTP requests to user server
# process.env.IO_TEST_OUTPUT_FILE is the name of the file where results of IO tests should be put
# process.env.UNIT_TEST_OUTPUT_FILE is the name of the file where results of UNIT tests should be put
# The results file should have a JSON array with ONLY "true" or "false" values (booleans) as elements having one-to-one correspondance to challenges you design

import sys
import os
import json
# Add the path to script
sys.path.append(os.environ['USER_CODE_DIR'])

import script

results = []


try:
    assert type(script.all_links) is list
    results.append(True)
except Exception as e:
    results.append(False)

try:
    assert type(script.all_links[7]['text']) is str
    assert type(script.all_links[7]['href']) is str
    results.append(True)
except Exception as e:
    results.append(False)

try:
    assert len(script.all_links) == 37
    results.append(True)
except Exception as e:
    results.append(False)

try:
    assert script.all_links[7].get(
        'href') == '/webscraper-python-codedamn-classroom-website/documentation'
    assert script.all_links[7].get('text') == 'Documentation'
    results.append(True)
except Exception as e:
    results.append(False)


file = open(os.environ['UNIT_TEST_OUTPUT_FILE'], 'w')
file.write(json.dumps(results))
file.close()

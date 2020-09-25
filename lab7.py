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
import os.path
# Add the path to script
sys.path.append(os.environ['USER_CODE_DIR'])

import script

results = []


try:
    assert os.path.exists(os.environ['USER_CODE_DIR'] + '/products.csv')
    results.append(True)
except Exception as e:
    results.append(False)

try:
    csv = open(os.environ['USER_CODE_DIR'] + '/products.csv').read()
    assert '$1139.54' in csv
    assert '$1101.83' in csv
    assert '$494.71' in csv
    results.append(True)
except Exception as e:
    results.append(False)

try:
    csv = open(os.environ['USER_CODE_DIR'] + '/products.csv').read()
    assert 'Asus AsusPro' in csv
    assert 'Asus ROG Strix' in csv
    assert 'Acer Aspire 3' in csv
    results.append(True)
except Exception as e:
    results.append(False)

try:
    csv = open(os.environ['USER_CODE_DIR'] + '/products.csv').read()
    assert 'AsusPro Advanced BU401LA-FA271G Dark Grey' in csv
    assert 'Apple MacBook Air 13.3' in csv
    assert 'Acer Aspire 3 A315-51 Black, 15.6' in csv
    results.append(True)
except Exception as e:
    results.append(False)

try:
    csv = open(os.environ['USER_CODE_DIR'] + '/products.csv').read()
    assert '/webscraper-python-codedamn-classroom-website/cart2.png' in csv
    results.append(True)
except Exception as e:
    results.append(False)

try:
    csv = open(os.environ['USER_CODE_DIR'] + '/products.csv').read()
    assert '7 reviews' in csv
    assert '4 reviews' in csv
    assert '2 reviews' in csv
    results.append(True)
except Exception as e:
    results.append(False)


file = open(os.environ['UNIT_TEST_OUTPUT_FILE'], 'w')
file.write(json.dumps(results))
file.close()

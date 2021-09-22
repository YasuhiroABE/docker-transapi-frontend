#!/usr/bin/env python3

import os
import sys
import json

def usage():
    print("Usage: %s <target-dir>" % (sys.argv[0]))
    pass

if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]) or not os.path.isfile(os.path.join(sys.argv[1], "package.json")):
    usage()
    sys.exit(1)
    pass

package_jsonfile = os.path.join(sys.argv[1], "package.json")
package_json = json.load(open(package_jsonfile))

package_json['dependencies']['axios'] = "^0.21.4"

## overwrite package.json
with open(package_jsonfile, "w") as f:
    json.dump(package_json, f)
    pass

## end ##










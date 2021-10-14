import sys
print(sys.path.insert(0, '/app/python/pages'))

import os
os.system("ls")

from pages import main

main.main()

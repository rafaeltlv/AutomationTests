#!/bin/bash

source /Users/Apikorus/QAProjects/AutomationTests/env/bin/activate

pytest -n 5 --html=report.html

(crontab -l ; echo "0 0 * * * /bin/bash /path/to/your/script.sh") | crontab -
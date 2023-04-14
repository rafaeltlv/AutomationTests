#!/bin/bash

# Check if the cron job already exists
if ! crontab -l | grep -q "/bin/bash /Users/Apikorus/QAProjects/AutomationTests/build.sh"; then
    # Add the cron job
    (crontab -l 2>/dev/null; echo "0 0 * * * /bin/bash /Users/Apikorus/QAProjects/AutomationTests/build.sh") | crontab -
fi

# Activate the virtual environment
source /Users/Apikorus/QAProjects/AutomationTests/.env/bin/activate

# Run the tests
pytest -n 5 --html=report.html

exit 0
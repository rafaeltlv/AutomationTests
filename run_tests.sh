#!/bin/bash

source /Users/Apikorus/QAProjects/AutomationTests/env/bin/activate

pytest -n 5 --html=report.html

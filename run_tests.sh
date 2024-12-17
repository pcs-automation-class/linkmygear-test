#!/bin/bash

# Run tests
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

# Save history if exists
if [ -d "history-reports/history" ]; then
    cp -r history-reports/history reports/
fi

# Generate report
allure generate reports/ -o history-reports/ --clean

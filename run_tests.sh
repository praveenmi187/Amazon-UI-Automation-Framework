#!/bin/bash

# Amazon UI Automation Framework - Test Runner Script

echo "🛒 Amazon UI Automation Framework - Test Runner"
echo "================================================"

# Run tests with HTML report and screenshots
echo ""
echo "Running tests with HTML report..."
pytest tests/test_login.py -v \
    --html=Reports/report.html \
    --self-contained-html \
    --tb=short

# Check if tests passed
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All tests passed!"
    echo "📊 HTML Report: Reports/report.html"
    echo "📸 Screenshots: Reports/screenshots/"
else
    echo ""
    echo "❌ Tests failed. Check report and screenshots for details."
    echo "📊 HTML Report: Reports/report.html"
    echo "📸 Failed Screenshots: Reports/screenshots/"
fi

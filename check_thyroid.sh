#!/bin/bash

echo "🔍 Health Risk Predictor - Thyroid Check"
echo "========================================"

# Check all Python files
echo "📁 Checking Python files for 'thyroid'..."
PYTHON_FILES=$(find /workspace -name "*.py" -type f)
THYROID_COUNT_PY=0

for file in $PYTHON_FILES; do
    if grep -qi "thyroid" "$file"; then
        echo "❌ FOUND in: $file"
        grep -n -i "thyroid" "$file"
        THYROID_COUNT_PY=$((THYROID_COUNT_PY + 1))
    fi
done

if [ $THYROID_COUNT_PY -eq 0 ]; then
    echo "✅ No thyroid found in Python files"
fi

# Check HTML files
echo ""
echo "📄 Checking HTML templates for 'thyroid'..."
HTML_FILES=$(find /workspace -name "*.html" -type f)
THYROID_COUNT_HTML=0

for file in $HTML_FILES; do
    if grep -qi "thyroid" "$file"; then
        echo "❌ FOUND in: $file"
        grep -n -i "thyroid" "$file"
        THYROID_COUNT_HTML=$((THYROID_COUNT_HTML + 1))
    fi
done

if [ $THYROID_COUNT_HTML -eq 0 ]; then
    echo "✅ No thyroid found in HTML files"
fi

# Check all text files
echo ""
echo "📝 Checking all text files for 'thyroid'..."
ALL_FILES=$(find /workspace -type f \( -name "*.py" -o -name "*.html" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.csv" \))
THYROID_COUNT_ALL=0

for file in $ALL_FILES; do
    if grep -qi "thyroid" "$file"; then
        echo "❌ FOUND in: $file"
        grep -n -i "thyroid" "$file"
        THYROID_COUNT_ALL=$((THYROID_COUNT_ALL + 1))
    fi
done

if [ $THYROID_COUNT_ALL -eq 0 ]; then
    echo "✅ No thyroid found in any text files"
fi

# Summary
echo ""
echo "📊 SUMMARY:"
echo "Python files with thyroid: $THYROID_COUNT_PY"
echo "HTML files with thyroid: $THYROID_COUNT_HTML"
echo "Total files with thyroid: $THYROID_COUNT_ALL"

if [ $THYROID_COUNT_ALL -eq 0 ]; then
    echo ""
    echo "🎉 CLEAN CODE! No thyroid references found anywhere."
    echo "✅ Your code only contains diabetes and heart disease as requested."
else
    echo ""
    echo "⚠️ Thyroid references found. Clean deployment needed."
fi
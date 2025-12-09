#!/bin/bash
cd medwiki_facts_extractor
python simple_batch.py > batch_results.log 2>&1 &
PID=$!
echo "Started process $PID"
echo "Checking status every 30 seconds for 3 minutes..."

for i in {1..6}; do
  sleep 30
  if ps -p $PID > /dev/null; then
    echo "Process still running... (check $i)"
    tail -5 batch_results.log
    echo "---"
  else
    echo "Process finished"
    break
  fi
done

echo "Final output:"
cat batch_results.log

#!/bin/bash
# setup.sh — Project setup script
 
echo '========================================='
echo ' DevOps + ML Project Setup'
echo '========================================='
 
# Create virtual environment
python3 -m venv venv
echo '[OK] Virtual environment created'
 
# Activate and install dependencies
source venv/bin/activate
pip install -r requirements.txt -q
echo '[OK] Dependencies installed'
 
# Create log directory
mkdir -p logs
echo "[OK] Setup complete at $(date)" >> logs/setup.log
 
echo ''
echo 'Setup complete! Run: source venv/bin/activate'
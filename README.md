# Failed Login Analyzer

## Description
Python tool that analyzes authentification logs to detect repeated failed login attempts and flag suspicious IP addresses. 

## Why This Matters
Repeated failed logins are a common indicator of brute-force activity. Automating detection helps security analysts triage faster and reduce manual review

## How It Works
1. Reads authentifaction log entries
2. Filters failed login events
3. Extracts source IP addresses
4. Counts failures per IP
5. Flag IPs exceeding a configurable threshold
6. Supports configurable alert thresholds via command-line arguments

## Skills Demonstrated
- Python Scripting
- Log Analysis
- Regular Expressions
- Security Alert Thresholds
- SOC Tier-1 Detection Logic

## Example Use Case
Supports rapid identification of potential brute-force login attempts for investigation or escalation.

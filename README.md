# OT Cybersecurity Risk Register

A lightweight Python-based risk register for assessing and prioritizing
cybersecurity risks across Operational Technology (OT) assets.

## Overview

OT environments often contain assets with very different operational
criticality, exposure, and potential impact.

This project demonstrates a simple approach to organizing OT asset information,
calculating risk scores, classifying risks, and generating a prioritized
risk report.

The example environment represents a fictional manufacturing facility containing
PLCs, HMIs, SCADA infrastructure, engineering workstations, network devices,
servers, gateways, and vendor remote access.

## Risk Methodology

For this initial version, risk is calculated using:

Risk Score = Likelihood × Impact

Both Likelihood and Impact are rated from 1 to 5.

Risk scores are classified as:

| Risk Score | Classification |
|------------|----------------|
| 1–4 | Low |
| 5–9 | Medium |
| 10–15 | High |
| 16–25 | Critical |

Asset criticality and network exposure are also recorded in the source dataset
for future extensions of the prioritization methodology.

## Features

- Reads OT asset data from CSV
- Calculates cybersecurity risk scores
- Classifies risks as Low, Medium, High, or Critical
- Prioritizes assets by risk score
- Displays results in the terminal
- Exports results to a CSV risk report
- Uses only Python's built-in CSV module

## Project Structure

```text
01-OT-Risk-Register/
├── assets.csv
├── risk_register.py
├── risk_report.csv
└── README.md
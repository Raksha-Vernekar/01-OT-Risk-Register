import csv


def classify_risk(score):
    if 1 <= score <= 4:
        return "Low"
    elif 5 <= score <= 9:
        return "Medium"
    elif 10 <= score <= 15:
        return "High"
    elif 16 <= score <= 25:
        return "Critical"
    else:
        return "Unknown"


assets = []

with open("assets.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        likelihood = int(row["Likelihood"])
        impact = int(row["Impact"])

        risk_score = likelihood * impact
        risk_level = classify_risk(risk_score)

        assets.append({
            "Asset_Name": row["Asset_Name"],
            "Asset_Type": row["Asset_Type"],
            "Risk_Score": risk_score,
            "Risk_Level": risk_level
        })


assets.sort(key=lambda asset: asset["Risk_Score"], reverse=True)

# Export the sorted results to risk_report.csv
with open("risk_report.csv", "w", newline="", encoding="utf-8") as report_file:
    fieldnames = ["Asset_Name", "Asset_Type", "Risk_Score", "Risk_Level"]
    writer = csv.DictWriter(report_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(assets)


for asset in assets:
    print(
        asset["Asset_Name"],
        "|", asset["Asset_Type"],
        "| Score:", asset["Risk_Score"],
        "|", asset["Risk_Level"]
    )
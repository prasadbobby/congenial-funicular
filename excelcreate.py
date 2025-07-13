import pandas as pd
import os
import json

def create_excel_files_from_json():
    """
    Create Excel files from the JSON sample data provided in the original code.
    """
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Sample Clinical Records
    clinical_cases = [
        {
            "case_id": "C001",
            "age": 45,
            "gender": "Female",
            "symptoms": ["persistent cough", "low-grade fever", "fatigue"],
            "medical_history": ["asthma", "seasonal allergies"],
            "diagnosis": "COVID-19",
            "treatment": "Antiviral medication, rest, monitoring",
            "outcome": "Full recovery after 3 weeks",
            "complications": None
        },
        {
            "case_id": "C002",
            "age": 16,
            "gender": "Male",
            "symptoms": ["severe abdominal pain", "nausea", "fever"],
            "medical_history": ["none"],
            "diagnosis": "Acute appendicitis",
            "treatment": "Laparoscopic appendectomy",
            "outcome": "Successful recovery",
            "complications": "None"
        },
        {
            "case_id": "C003",
            "age": 62,
            "gender": "Male",
            "symptoms": ["chest pain", "shortness of breath", "arm pain"],
            "medical_history": ["hypertension", "diabetes"],
            "diagnosis": "Myocardial infarction",
            "treatment": "Angioplasty, stent placement",
            "outcome": "Stable condition, ongoing medication",
            "complications": "Minor arrhythmia"
        },
        {
            "case_id": "C004",
            "age": 28,
            "gender": "Female",
            "symptoms": ["severe headache", "blurred vision", "nausea"],
            "medical_history": ["migraines"],
            "diagnosis": "Migraine with aura",
            "treatment": "Triptans, preventive medication",
            "outcome": "Improved with ongoing management",
            "complications": "None"
        },
        {
            "case_id": "C005",
            "age": 55,
            "gender": "Female",
            "symptoms": ["joint pain", "fatigue", "morning stiffness"],
            "medical_history": ["family history of autoimmune disease"],
            "diagnosis": "Rheumatoid arthritis",
            "treatment": "DMARDs, physical therapy",
            "outcome": "Controlled with medication",
            "complications": "Mild medication side effects"
        }
    ]
    
    # Convert lists to strings for Excel storage
    for case in clinical_cases:
        if isinstance(case["symptoms"], list):
            case["symptoms"] = ", ".join(case["symptoms"])
        if isinstance(case["medical_history"], list):
            case["medical_history"] = ", ".join(case["medical_history"])
        if case["complications"] is None:
            case["complications"] = "None"
    
    # Medical Literature
    medical_literature = [
        {
            "paper_id": "ML001",
            "title": "Novel Treatment Approaches for Metformin-Resistant Type 2 Diabetes",
            "authors": "Johnson et al.",
            "publication_date": "2023",
            "journal": "Diabetes Care",
            "key_findings": [
                "GLP-1 receptor agonists showed 67% success rate",
                "SGLT2 inhibitors reduced HbA1c by 1.2%",
                "Combination therapy more effective than monotherapy"
            ],
            "methodology": "Randomized controlled trial",
            "sample_size": 500
        },
        {
            "paper_id": "ML002",
            "title": "Immunotherapy Outcomes in Advanced Melanoma",
            "authors": "Smith et al.",
            "publication_date": "2024",
            "journal": "Cancer Research",
            "key_findings": [
                "PD-1 inhibitors showed 45% response rate",
                "Combination therapy improved survival by 40%",
                "Early intervention critical for success"
            ],
            "methodology": "Multi-center clinical trial",
            "sample_size": 300
        },
        {
            "paper_id": "ML003",
            "title": "Comparison of SSRI Effectiveness in Treatment-Resistant Depression",
            "authors": "Wong et al.",
            "publication_date": "2023",
            "journal": "Journal of Psychiatry",
            "key_findings": [
                "Escitalopram showed 25% higher remission rates",
                "Combination with CBT improved outcomes by 35%",
                "Side effect profiles varied significantly between medications"
            ],
            "methodology": "Double-blind placebo-controlled trial",
            "sample_size": 450
        },
        {
            "paper_id": "ML004",
            "title": "Emerging Antibiotic Resistance in Hospital-Acquired Pneumonia",
            "authors": "Garcia et al.",
            "publication_date": "2024",
            "journal": "Infectious Disease Journal",
            "key_findings": [
                "Carbapenem resistance increased by 15%",
                "Combination therapy showed 30% better efficacy",
                "Early culture essential for targeted treatment"
            ],
            "methodology": "Retrospective cohort study",
            "sample_size": 750
        },
        {
            "paper_id": "ML005",
            "title": "Stem Cell Therapy for Osteoarthritis of the Knee",
            "authors": "Chen et al.",
            "publication_date": "2023",
            "journal": "Journal of Orthopedics",
            "key_findings": [
                "Pain reduction in 70% of patients",
                "Improved cartilage regeneration observed in MRI",
                "Effects lasted 18+ months in 65% of responders"
            ],
            "methodology": "Prospective clinical trial",
            "sample_size": 200
        }
    ]
    
    # Convert lists to strings for Excel storage
    for paper in medical_literature:
        if isinstance(paper["key_findings"], list):
            paper["key_findings"] = "; ".join(paper["key_findings"])
    
    # Symptom Cases
    symptom_cases = [
        {
            "symptom_id": "S001",
            "presenting_symptoms": ["chest pain", "shortness of breath", "dizziness"],
            "diagnosis": "Pulmonary Embolism",
            "risk_factors": ["recent surgery", "prolonged immobility"],
            "recommended_specialists": ["Pulmonologist", "Hematologist"],
            "urgency_level": "High",
            "diagnostic_tests": ["D-dimer", "CT pulmonary angiogram"]
        },
        {
            "symptom_id": "S002",
            "presenting_symptoms": ["high fever", "rash", "fatigue"],
            "diagnosis": "Measles",
            "risk_factors": ["unvaccinated", "exposure to infected individual"],
            "recommended_specialists": ["Pediatrician", "Infectious Disease Specialist"],
            "urgency_level": "Medium",
            "diagnostic_tests": ["Antibody test", "Viral culture"]
        },
        {
            "symptom_id": "S003",
            "presenting_symptoms": ["severe headache", "neck stiffness", "photophobia"],
            "diagnosis": "Bacterial Meningitis",
            "risk_factors": ["recent infection", "immunocompromised state"],
            "recommended_specialists": ["Neurologist", "Infectious Disease Specialist"],
            "urgency_level": "Critical",
            "diagnostic_tests": ["Lumbar puncture", "Blood cultures"]
        },
        {
            "symptom_id": "S004",
            "presenting_symptoms": ["abdominal pain", "bloating", "diarrhea"],
            "diagnosis": "Irritable Bowel Syndrome",
            "risk_factors": ["stress", "dietary triggers", "family history"],
            "recommended_specialists": ["Gastroenterologist", "Nutritionist"],
            "urgency_level": "Low",
            "diagnostic_tests": ["Stool analysis", "Colonoscopy"]
        },
        {
            "symptom_id": "S005",
            "presenting_symptoms": ["joint pain", "swelling", "morning stiffness"],
            "diagnosis": "Rheumatoid Arthritis",
            "risk_factors": ["family history", "smoking", "female gender"],
            "recommended_specialists": ["Rheumatologist", "Physical Therapist"],
            "urgency_level": "Medium",
            "diagnostic_tests": ["Rheumatoid factor", "Anti-CCP antibodies", "Joint X-rays"]
        }
    ]
    
    # Convert lists to strings for Excel storage
    for case in symptom_cases:
        if isinstance(case["presenting_symptoms"], list):
            case["presenting_symptoms"] = ", ".join(case["presenting_symptoms"])
        if isinstance(case["risk_factors"], list):
            case["risk_factors"] = ", ".join(case["risk_factors"])
        if isinstance(case["recommended_specialists"], list):
            case["recommended_specialists"] = ", ".join(case["recommended_specialists"])
        if isinstance(case["diagnostic_tests"], list):
            case["diagnostic_tests"] = ", ".join(case["diagnostic_tests"])
    
    # Drug Interactions
    drug_interactions = [
        {
            "interaction_id": "D001",
            "medications": ["Lisinopril", "Metformin", "Ibuprofen"],
            "severity": "Moderate",
            "effects": [
                "Reduced blood pressure control",
                "Increased risk of kidney dysfunction"
            ],
            "recommendations": [
                "Monitor blood pressure closely",
                "Consider alternative pain medication",
                "Regular kidney function testing"
            ],
            "alternatives": ["Acetaminophen for pain relief"]
        },
        {
            "interaction_id": "D002",
            "medications": ["Sertraline", "Omeprazole", "Diphenhydramine"],
            "severity": "Mild to Moderate",
            "effects": [
                "Increased sedation",
                "Potential serotonin syndrome risk"
            ],
            "recommendations": [
                "Avoid concurrent use of multiple sedating medications",
                "Consider alternative sleep aids",
                "Monitor for excessive drowsiness"
            ],
            "alternatives": ["Melatonin for sleep", "Alternative SSRI"]
        },
        {
            "interaction_id": "D003",
            "medications": ["Warfarin", "Aspirin", "Ginkgo biloba"],
            "severity": "Severe",
            "effects": [
                "Significantly increased bleeding risk",
                "Unpredictable INR values"
            ],
            "recommendations": [
                "Avoid combination",
                "More frequent INR monitoring if necessary", 
                "Educate patient on bleeding signs"
            ],
            "alternatives": ["Different anticoagulant", "Discuss with cardiologist"]
        },
        {
            "interaction_id": "D004",
            "medications": ["Simvastatin", "Clarithromycin", "Grapefruit juice"],
            "severity": "Severe",
            "effects": [
                "Increased statin levels",
                "Higher risk of myopathy and rhabdomyolysis"
            ],
            "recommendations": [
                "Temporary statin discontinuation during antibiotic course",
                "Avoid grapefruit products",
                "Monitor for muscle pain"
            ],
            "alternatives": ["Azithromycin (less interaction)", "Rosuvastatin (less affected)"]
        },
        {
            "interaction_id": "D005",
            "medications": ["Levothyroxine", "Calcium supplements", "Iron supplements"],
            "severity": "Moderate",
            "effects": [
                "Reduced thyroid hormone absorption",
                "Suboptimal thyroid control"
            ],
            "recommendations": [
                "Take supplements at least 4 hours apart from thyroid medication",
                "Morning thyroid dose on empty stomach"
            ],
            "alternatives": ["Timing separation rather than medication change"]
        }
    ]
    
    # Convert lists to strings for Excel storage
    for interaction in drug_interactions:
        if isinstance(interaction["medications"], list):
            interaction["medications"] = ", ".join(interaction["medications"])
        if isinstance(interaction["effects"], list):
            interaction["effects"] = "; ".join(interaction["effects"])
        if isinstance(interaction["recommendations"], list):
            interaction["recommendations"] = "; ".join(interaction["recommendations"])
        if isinstance(interaction["alternatives"], list):
            interaction["alternatives"] = "; ".join(interaction["alternatives"])
    
    # Create dataframes
    clinical_df = pd.DataFrame(clinical_cases)
    literature_df = pd.DataFrame(medical_literature)
    symptom_df = pd.DataFrame(symptom_cases)
    drug_df = pd.DataFrame(drug_interactions)
    
    # Save to Excel files
    clinical_df.to_excel('data/clinical_cases.xlsx', index=False)
    literature_df.to_excel('data/medical_literature.xlsx', index=False)
    symptom_df.to_excel('data/symptom_cases.xlsx', index=False)
    drug_df.to_excel('data/drug_interactions.xlsx', index=False)
    
    print("Excel files created successfully in the 'data' directory")

def read_data_from_excel():
    """
    Read data from Excel files and convert string representations of lists back to lists.
    Returns a dictionary with all data categories.
    """
    data = {}
    
    # Read clinical cases
    clinical_df = pd.read_excel('data/clinical_cases.xlsx')
    clinical_cases = clinical_df.to_dict(orient='records')
    for case in clinical_cases:
        if isinstance(case["symptoms"], str):
            case["symptoms"] = [s.strip() for s in case["symptoms"].split(",")]
        if isinstance(case["medical_history"], str):
            case["medical_history"] = [m.strip() for m in case["medical_history"].split(",")]
        if case["complications"] == "None":
            case["complications"] = None
    data['clinical'] = clinical_cases
    
    # Read medical literature
    literature_df = pd.read_excel('data/medical_literature.xlsx')
    literature_cases = literature_df.to_dict(orient='records')
    for paper in literature_cases:
        if isinstance(paper["key_findings"], str):
            paper["key_findings"] = [f.strip() for f in paper["key_findings"].split(";")]
    data['literature'] = literature_cases
    
    # Read symptom cases
    symptom_df = pd.read_excel('data/symptom_cases.xlsx')
    symptom_cases = symptom_df.to_dict(orient='records')
    for case in symptom_cases:
        if isinstance(case["presenting_symptoms"], str):
            case["presenting_symptoms"] = [s.strip() for s in case["presenting_symptoms"].split(",")]
        if isinstance(case["risk_factors"], str):
            case["risk_factors"] = [r.strip() for r in case["risk_factors"].split(",")]
        if isinstance(case["recommended_specialists"], str):
            case["recommended_specialists"] = [s.strip() for s in case["recommended_specialists"].split(",")]
        if isinstance(case["diagnostic_tests"], str):
            case["diagnostic_tests"] = [t.strip() for t in case["diagnostic_tests"].split(",")]
    data['symptom'] = symptom_cases
    
    # Read drug interactions
    drug_df = pd.read_excel('data/drug_interactions.xlsx')
    drug_interactions = drug_df.to_dict(orient='records')
    for interaction in drug_interactions:
        if isinstance(interaction["medications"], str):
            interaction["medications"] = [m.strip() for m in interaction["medications"].split(",")]
        if isinstance(interaction["effects"], str):
            interaction["effects"] = [e.strip() for e in interaction["effects"].split(";")]
        if isinstance(interaction["recommendations"], str):
            interaction["recommendations"] = [r.strip() for r in interaction["recommendations"].split(";")]
        if isinstance(interaction["alternatives"], str):
            interaction["alternatives"] = [a.strip() for a in interaction["alternatives"].split(";")]
    data['drug'] = drug_interactions
    
    return data

if __name__ == "__main__":
    create_excel_files_from_json()
    # Verify by reading the data back
    data = read_data_from_excel()
    print("\nVerification - Number of records by category:")
    for category, records in data.items():
        print(f"{category}: {len(records)} records")
    
    # Print first record of each category as sample
    print("\nSample records:")
    for category, records in data.items():
        print(f"\n{category.upper()} sample:")
        print(json.dumps(records[0], indent=2))

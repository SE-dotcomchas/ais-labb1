# Skapa ett testscenario och mät tider
import time
import json
from datetime import datetime

results = {
    'test_scenario': 'SSH brute force + portskanning + filändring',
    'tests': []
}

# Simulera mätning (ersätt med faktiska mätningar från din miljö)
test_cases = [
    {
        'attack': 'SSH brute force (10 försök)',
        'rule_based_detection_sec': None,   # Fyll i din mätning
        'ai_detection_sec': None,           # Fyll i din mätning
        'rule_based_detected': None,        # True/False
        'ai_detected': None,               # True/False
    },
    {
        'attack': 'Portskanning (top 1000)',
        'rule_based_detection_sec': None,
        'ai_detection_sec': None,
        'rule_based_detected': None,
        'ai_detected': None,
    },
    {
        'attack': 'Kritisk filändring',
        'rule_based_detection_sec': None,
        'ai_detection_sec': None,
        'rule_based_detected': None,
        'ai_detected': None,
    },
    {
        'attack': 'Långsam brute force (1 försök/min)',
        'rule_based_detection_sec': None,
        'ai_detection_sec': None,
        'rule_based_detected': None,
        'ai_detected': None,
    },
]

results['tests'] = test_cases
results['measurement_date'] = datetime.now().isoformat()

with open('detection_comparison.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Mall skapad: detection_comparison.json")
print("Fyll i med dina faktiska mätresultat efter testning.")
print("\nFör VG: Beräkna procentuell förbättring:")
print("  Förbättring = (regelbaserad_tid - ai_tid) / regelbaserad_tid * 100")
SCRIPT

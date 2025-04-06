import json
from contact_tracing import (
    parse_interaction_log,
    trace_infection,
    identify_super_spreaders
)

def run_test_cases():
    """Reads test cases from a JSON file and executes them."""
    
    try:
        with open("src/test_cases.txt", "r") as file:
            test_cases = json.load(file)
    except FileNotFoundError:
        print("\n❌ Error: Test cases file not found. Make sure 'test_cases.txt' exists in 'src' folder.")
        return
    except json.JSONDecodeError:
        print("\n❌ Error: Invalid JSON format in test_cases.txt. Please check the syntax.")
        return

    print("\n🚀 Running Test Cases...\n")

    for i, case in enumerate(test_cases, start=1):
        print(f"🔎 Test Case {i}: {case['name']}")

        log_data = case["log_data"]
        initial_infected = case["initial_infected"]
        contagious_period = case["contagious_period"]
        super_spreader_threshold = case["super_spreader_threshold"]
        expected_infected = case.get("expected_infected", [])
        expected_super_spreaders = case.get("expected_super_spreaders", [])

        # Execute the logic
        parsed_log = parse_interaction_log(log_data)
        actual_infected = trace_infection(initial_infected, parsed_log, contagious_period)
        actual_super_spreaders = identify_super_spreaders(parsed_log, super_spreader_threshold)

        # Results comparison
        infected_match = set(actual_infected) == set(expected_infected)
        super_spreader_match = set(actual_super_spreaders) == set(expected_super_spreaders)

        # Output results
        print(f"   ✅ Expected Infected: {expected_infected}")
        print(f"   🛑 Actual Infected: {actual_infected}")
        print(f"   ✅ Expected Super Spreaders: {expected_super_spreaders}")
        print(f"   🚀 Actual Super Spreaders: {actual_super_spreaders}")

        # Validate test case
        if infected_match and super_spreader_match:
            print("   🎉 Test Passed!\n")
        else:
            print("   ❌ Test Failed!\n")

if __name__ == "__main__":
    run_test_cases()

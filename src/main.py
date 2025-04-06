import os
import time
import json
from contact_tracing import (
    parse_interaction_log,
    trace_infection,
    identify_super_spreaders,
    generate_report,
    visualize_network,
    find_contacts
)

def get_user_input():
    """Allows users to input test cases manually or choose predefined ones."""
    print("\n📢 Welcome to the Contact Tracing System!")
    choice = input("\n🔹 Choose input method (1: Manual Entry, 2: Load Test Cases): ")

    if choice == "1":
        log_data = []
        num_entries = int(input("\n🔹 Enter number of interaction logs: "))
        for i in range(num_entries):
            entry = input(f"🔸 Log {i+1} (PersonA PersonB Time): ").split()
            log_data.append((entry[0], entry[1], int(entry[2])))

        initial_infected = input("\n🛑 Enter initially infected individuals (comma-separated): ").split(',')
        contagious_period = int(input("\n⏳ Enter contagious period (hours): "))
        super_spreader_threshold = int(input("\n🚨 Enter contact threshold for super spreaders: "))
        return log_data, initial_infected, contagious_period, super_spreader_threshold

    elif choice == "2":
        with open("src/test_cases.txt", "r") as file:
            test_cases = json.load(file)

        print("\n🔹 Available Test Cases:")
        for idx, case in enumerate(test_cases, start=1):
            print(f"  {idx}. {case['name']}")

        selected = int(input("\n🔹 Select a test case number: ")) - 1
        selected_case = test_cases[selected]
        return (selected_case["log_data"], selected_case["initial_infected"], 
                selected_case["contagious_period"], selected_case["super_spreader_threshold"])

    else:
        print("\n❌ Invalid choice! Please restart.")
        exit()

def main():
    """Handles input, processes data, and displays results."""
    log_data, initial_infected, contagious_period, super_spreader_threshold = get_user_input()
    print("\n🕵️‍♂️ Analyzing data...", end="", flush=True)
    time.sleep(1)
    print(" ✅\n")

    parsed_log = parse_interaction_log(log_data)
    infected_people = trace_infection(initial_infected, parsed_log, contagious_period)
    super_spreaders = identify_super_spreaders(parsed_log, super_spreader_threshold)

    print("\n📌 Analysis Complete!")
    print("\n🦠 Potentially Infected Individuals:", ", ".join(infected_people) if infected_people else "None")
    print("🚀 Super Spreaders:", ", ".join(super_spreaders) if super_spreaders else "None")

    # Finding contacts of a specific person
    person = input("\n🔎 Enter a person to find their contacts: ")
    time_window = int(input("\n⏳ Enter the time window (hours): "))
    contacts = find_contacts(person, time_window, parsed_log)
    
    print(f"\n📊 Contacts of {person} within {time_window} hours: {contacts}")

    generate_report(infected_people, super_spreaders)
    visualize_network(parsed_log, infected_people, super_spreaders)

if __name__ == "__main__":
    os.makedirs("src", exist_ok=True)
    os.makedirs("bin", exist_ok=True)
    main()

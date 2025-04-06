from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt
import os
import json

def parse_interaction_log(log_data):
    """Parses the interaction log and returns a structured format."""
    return [(p1, p2, int(time)) for p1, p2, time in log_data]

def build_interaction_map(log_data):
    """Creates a mapping of interactions for efficient lookup."""
    interaction_map = defaultdict(list)
    for p1, p2, time in log_data:
        interaction_map[p1].append((p2, time))
        #interaction_map[p2].append((p1, time))
    return interaction_map

def get_earliest_interaction_time(log_data):
    """Finds the earliest recorded interaction time."""
    return min(time for _, _, time in log_data) if log_data else 0

def find_contacts(person, time_window, log_data):
    """Finds all people a given person contacted within a specific time window."""
    contacts = []
    for p1, p2, time in log_data:
        if p1 == person or p2 == person:
            if abs(time - get_earliest_interaction_time(log_data)) <= time_window:
                contacts.append((p1, p2, time))
    return contacts

def trace_infection(initial_infected, log_data, contagious_period):
    """Traces the infection spread based on interactions within the contagious period."""
    if not initial_infected:
        return []

    infected = set(initial_infected)
    interaction_map = build_interaction_map(log_data)

    # Assume infections start at the earliest interaction time
    start_time = log_data #get_earliest_interaction_time(log_data)
    infection_times = {person: start_time for person in initial_infected}

    queue = deque([(person, start_time) for person in initial_infected])

    while queue:
        person, infection_time = queue.popleft()
        for contact, contact_time in interaction_map[person]:
            if (contact not in infected) and (contact_time - infection_time <= contagious_period):
                infected.add(contact)
                infection_times[contact] = contact_time
                queue.append((contact, contact_time))

    return sorted(infected)  # Ensure consistent output for testing

def identify_super_spreaders(log_data, threshold):
    """Identifies individuals who have had more interactions than the given threshold."""
    contact_count = defaultdict(int)
    for p1, p2, _ in log_data:
        contact_count[p1] += 1
        contact_count[p2] += 1
    return sorted([person for person, count in contact_count.items() if count >= threshold])

def generate_report(infected_people, super_spreaders):
    """Generates and saves a contact tracing report."""
    report = {
        "Potentially Infected Individuals": infected_people,
        "Super Spreaders": super_spreaders
    }
    os.makedirs("reports", exist_ok=True)
    with open("reports/contact_tracing_report.json", "w") as file:
        json.dump(report, file, indent=4)
    print("\n📄 Report saved to reports/contact_tracing_report.json")

def visualize_network(log_data, infected_people, super_spreaders):
    """Generates a contact tracing network graph."""
    G = nx.Graph()
    for p1, p2, _ in log_data:
        G.add_edge(p1, p2)

    node_colors = []
    for node in G.nodes():
        if node in infected_people:
            node_colors.append("red")
        elif node in super_spreaders:
            node_colors.append("orange")
        else:
            node_colors.append("blue")

    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color=node_colors, edge_color="gray", node_size=700, font_size=10)
    plt.title("🦠 Contact Tracing Network")
    plt.show()

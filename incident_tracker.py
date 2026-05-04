# Store All Incidents In A List
incidents = []


# Add A New Incident To The List
def add_incident():
    print("\nAdd Incident")

    # Get User Input
    employee_name = input("Enter employee name: ")
    incident_type = input("Enter incident type: ")
    severity = input("Enter severity (Low/Medium/High): ")

    # Create Incident As A Dictionary
    incident = {
        "employee_name": employee_name,
        "incident_type": incident_type,
        "severity": severity,
        "status": "Open"
    }

    # Add Incident To List
    incidents.append(incident)

    # Confirm Success To User
    print("Incident added successfully!")


# Display All Incidents
def view_incidents():
    print("\nView All Incidents")

    # Check If List Is Empty
    if len(incidents) == 0:
        print("No incidents found.")
    else:
        # Loop Through And Display Each Incident
        for index, incident in enumerate(incidents, start=1):
            print(f"\nIncident ID: {index}")
            print(f"Employee Name: {incident['employee_name']}")
            print(f"Incident Type: {incident['incident_type']}")
            print(f"Severity: {incident['severity']}")
            print(f"Status: {incident['status']}")


# Search Incidents By Employee Name
def search_incidents():
    print("\nSearch Incidents")

    # Check If List Is Empty
    if len(incidents) == 0:
        print("No incidents found.")
        return

    # Get Search Input
    search_name = input("Enter employee name to search: ")

    # Track If Any Match Is Found
    found = False

    # Loop Through Incidents And Match Name
    for index, incident in enumerate(incidents, start=1):
        if search_name.lower() in incident["employee_name"].lower():
            print(f"\nIncident ID: {index}")
            print(f"Employee Name: {incident['employee_name']}")
            print(f"Incident Type: {incident['incident_type']}")
            print(f"Severity: {incident['severity']}")
            print(f"Status: {incident['status']}")
            found = True

    # If No Matches Found
    if not found:
        print("No matching incidents found.")


# Update The Status Of An Existing Incident
def update_incident_status():
    print("\nUpdate Incident Status")

    # Check If List Is Empty
    if len(incidents) == 0:
        print("No incidents found.")
        return

    # Show Incidents Before Updating
    view_incidents()

    try:
        # Get Incident ID From User
        incident_id = int(input("Enter the Incident ID to update: "))

        # Validate ID Range
        if incident_id < 1 or incident_id > len(incidents):
            print("Invalid Incident ID.")
            return

        # Get New Status
        new_status = input("Enter new status (Open/In Progress/Closed): ")

        # Update Status
        incidents[incident_id - 1]["status"] = new_status

        # Confirm Update
        print("Incident status updated successfully!")

    except ValueError:
        # Handle Invalid Input
        print("Invalid input. Please enter a number.")


# Main Menu Loop
def main():
    while True:
        print("\nIncident Tracker")
        print("1. Add Incident")
        print("2. View All Incidents")
        print("3. Search Incidents")
        print("4. Update Incident Status")
        print("5. Exit")

        # Get User Choice
        choice = input("Choose an option: ")

        # Call Functions Based On Choice
        if choice == "1":
            add_incident()
        elif choice == "2":
            view_incidents()
        elif choice == "3":
            search_incidents()
        elif choice == "4":
            update_incident_status()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            # Handle Invalid Menu Input
            print("Invalid option. Please choose 1-5.")


# Run The Program
main()

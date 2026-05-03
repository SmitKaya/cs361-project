def main():
    while True:
        print("\nIncident Tracker")
        print("1. Add Incident")
        print("2. View All Incidents")
        print("3. Search Incidents")
        print("4. Update Incident Status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Add Incident selected")
        elif choice == "2":
            print("View All Incidents selected")
        elif choice == "3":
            print("Search Incidents selected")
        elif choice == "4":
            print("Update Incident Status selected")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


main()

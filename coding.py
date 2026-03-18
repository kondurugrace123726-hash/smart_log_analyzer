from collections import defaultdict

def analyze_logs(filename):
    user_actions = defaultdict(int)
    logged_in_users = set()
    error_count = 0

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 3:
                continue

            timestamp, user, action = parts

            # Count actions
            user_actions[user] += 1

            # Track login/logout
            if action == "LOGIN":
                logged_in_users.add(user)
            elif action == "LOGOUT":
                logged_in_users.discard(user)

            # Count errors
            if action == "ERROR":
                error_count += 1

    # Find most active user
    max_actions = max(user_actions.values())
    most_active = [u for u, c in user_actions.items() if c == max_actions]

    print("User Activity Count:")
    for user, count in user_actions.items():
        print(user, ":", count)

    print("\nMost Active User(s):", ", ".join(most_active))
    print("Total ERROR actions:", error_count)

    if logged_in_users:
        print("Users without logout:", ", ".join(logged_in_users))
    else:
        print("All users logged out properly.")


if __name__ == "__main__":
    filename = input("Enter log file name: ").strip()
    analyze_logs(filename)
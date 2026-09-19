# Raw data or user records: (User ID, Name, Role, Is_Active, Login_Attempts)
users = [
    (101, "Alice", "admin", True, 1),
    (102, "Bob", "member", True, 4),
    (103, "Charlie", "editor", False, 0),
    (104, "Diana", "admin", False, 6),
    (105, "Evan", "member", True, 2),
    (106, "Fiona", "guest", True, 0),
]

active_granted = 0
inactive_count = 0
alert_count = 0

for user_id, name, role, is_active, attempts in users:
    # PART A: Access control based on role and active status
    if is_active and role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
        active_granted += 1
    elif is_active and role in ("member", "editor"):
        print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
        active_granted += 1
    elif not is_active:
        print(f"[DENIED] Account {name} is inactive.")
        inactive_count += 1
    else:
        # Active user with a role that has no access rule (e.g. guest)
        print(f"[NO ACCESS] {name} (ID: {user_id}) has role '{role}' with no access rule.")

    # PART B: Security audit (applies to every account, active or not)
    if attempts >= 5:
        print(f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({attempts} attempts).")
        alert_count += 1


print("\nAUDIT SUMMARY REPORT")
print("=" * 40)
print(f"Total Active Users Granted: {active_granted}")
print(f"Total Inactive Accounts: {inactive_count}")
print(f"Total Security Alerts: {alert_count}")

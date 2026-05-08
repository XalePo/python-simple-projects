def main():
    events = read_events()
    sus_attempts = analyze_failed_attempts(events)
    display_results(sus_attempts)


def read_events():
    with open("login_logs.txt", "r") as f:
        all_lines = f.readlines()

        keys = [key.strip() for key in all_lines[0].rstrip().split("|")]
        lines = all_lines[1:]

        events = []

        for line in lines:
            values = [value.strip() for value in line.rstrip().split("|")]
            event_data = dict(zip(keys, values))
            events.append(event_data)

    return events


def analyze_failed_attempts(events):
    failure_counter = {}
    for event in events:
        if event.get("status") == "failed":
            ip = event.get("ip_address")
            failure_counter[ip] = failure_counter.get(ip, 0) + 1
    
    sus = {}
    for ip, attempts in failure_counter.items():
        if attempts >= 5:
            sus[ip] = attempts

    return sus


def display_results(sus_ip):
    if not sus_ip:
        print("No suspicious IPs detected.")
        return
    
    print("Suspicious IPs:")
    for ip, attempts in sus_ip.items():
        print(f"{ip} - {attempts} failed attempts")


if __name__ == "__main__":
    main()
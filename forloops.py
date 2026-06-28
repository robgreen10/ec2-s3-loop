servers = [{"title": "secops-1"}, {"title": "secops-2"}, {"title": "secops-3"}]
s3_buckets = [{"name": "bucket-1"}, {"name": "bucket-2"}, {"name": "bucket-3"}]


def aws_sheet():
    print("\nAWS assets in order:\n")
    for x, (server, s3) in enumerate(zip(servers, s3_buckets), start=1):
        print(f"{x}: {server['title']} - {s3['name']}")


aws_sheet()

timing = int(input("Enter avg seconds it takes to spin up EC2: "))

if timing < 60:
    print("\nGood no further action required\n")
elif timing > 60:
    print("\nThis is too slow, sending for further evaluation\n")
elif timing == 60:
    print("\nTarget time reached\n")

# EXECUTION
print("Calculating avg spin uptime per server...")
print("---Avg time per server spin up below---")

for server in servers:
    server["spin_time"] = timing

for server in servers:
    print(f"{server['title']} ---> {timing} seconds")

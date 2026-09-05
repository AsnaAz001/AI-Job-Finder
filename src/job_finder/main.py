from job_finder.crew import JobFinder


def run():
    print("\n=== Research and Job Finder ===\n")

    user_request = input("What do you want to research? ")

    inputs = {
        "user_request": user_request
    }

    result = JobFinder().crew().kickoff(inputs=inputs)

    print("\n\n========== FINAL RESULT ==========\n")
    print(result)
    print("\n==================================\n")


if __name__ == "__main__":
    run()

def plot1():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    script_dir = Path(__file__).resolve().parent
    print(script_dir)
    # Construct the full path to 'dataset.csv'
    file_path = script_dir / 'dataset.csv'


    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    domain_groups = df.groupby('Domain')
    avg_rates = domain_groups[['Success Rate (%)', 'Failure Rate (%)']].mean()

    # Extrapolating rates for the next 5 years (2024-2028)
    years = range(2024, 2029)

    # Extrapolating rates for each domain
    extrapolated_rates = {}
    for domain, rates in avg_rates.iterrows():
        success_rate = rates['Success Rate (%)']
        failure_rate = rates['Failure Rate (%)']
        extrapolated_success = [success_rate] * len(years)
        extrapolated_failure = [failure_rate] * len(years)
        extrapolated_rates[domain] = {
            'Success Rate (%)': extrapolated_success,
            'Failure Rate (%)': extrapolated_failure
        }

    # Creating a bar graph for predicted rates
    plt.figure(figsize=(10, 6))

    # Plotting bars for each domain
    for i, (domain, rates) in enumerate(extrapolated_rates.items()):
        plt.bar(
            [year + i * 0.15 for year in years],
            rates['Success Rate (%)'],
            width=0.15,
            align='center',
            label=f'{domain} - Success'
        )
        plt.bar(
            [year + i * 0.15 for year in years],
            rates['Failure Rate (%)'],
            width=0.15,
            align='center',
            label=f'{domain} - Failure',
            alpha=0.7
        )

    # Adding labels and title
    plt.xlabel('Years')
    plt.ylabel('Rate (%)')
    plt.title('Predicted Success and Failure Rates for 2024-2028')
    plt.xticks(years)
    plt.legend()
    plt.tight_layout()
    plt.savefig(script_dir / 'upload/main.png')
    # Show the plot
    #plt.show()


def gf1():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    script_dir = Path(__file__).resolve().parent
    print(script_dir)
    # Construct the full path to 'dataset.csv'
    file_path = script_dir / 'dataset.csv'

    # Load your dataset into a Pandas DataFrame (replace 'path_to_your_csv_file.csv' with your file path)
    df = pd.read_csv(file_path)


    # Assuming your DataFrame columns are named 'Domain', 'Success Rate (%)', and 'Failure Rate (%)'

    # Filter data for the year 2023
    data_2023 = df[df['Year'] == 2023]

    # Get unique domains from the dataset
    domains = data_2023['Domain'].unique()

    # Define the colors for success and failure bars
    success_color = 'lightblue'
    failure_color = 'darkblue'
    i=1
    # Iterate through each domain and plot for the next 5 years
    for domain in domains:
        domain_data = data_2023[data_2023['Domain'] == domain]
        success_rate = domain_data['Success Rate (%)'].values[0]
        failure_rate = domain_data['Failure Rate (%)'].values[0]

        # Predicting next 5 years' rates based on the assumption of no significant change
        predicted_success = [success_rate] * 5
        predicted_failure = [failure_rate] * 5

        # Years from 2024 to 2028
        years = list(range(2024, 2029))

        plt.figure(figsize=(8, 6))
        plt.bar(years, predicted_success, color=success_color, alpha=0.6, label='Success Rate')
        plt.bar(years, predicted_failure, color=failure_color, alpha=0.6, label='Failure Rate')

        plt.xlabel('Year')
        plt.ylabel('Rate (%)')
        plt.title(f'Predicted Success and Failure Rates for {domain} from 2023 to 2028')
        plt.legend()
        plt.savefig(script_dir / str('upload/predicted_rates_graph'+str(i)+'.png'))
        i+=1
        #plt.show()
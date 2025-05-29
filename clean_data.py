import pandas as pd

def clean_mine_data(file_path):
    df = pd.read_csv(file_path)

    # 1. Remove all rows with any missing values
    df.dropna(inplace=True)

    # 2. Fix inconsistent date formats
    if 'Date' in df.columns:
        df['Date'] = df['Date'].astype(str).str.replace("'", "", regex=False)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)

    # 3. Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # 4. Remove wrong data
    if 'Duration' in df.columns:
        df = df[df['Duration'] <= 240]
    for col in ['Pulse', 'Maxpulse', 'Calories']:
        if col in df.columns:
            if col == 'Calories':
                df = df[df[col] >= 0]
            else:
                df = df[df[col] > 0]

    return df

def clean_sales_data(file_path):
    df = pd.read_csv(file_path)

    # 1. Remove all rows with any missing values
    df.dropna(inplace=True)

    # 2. Fix inconsistent date formats
    if 'Order Date' in df.columns:
        df['Order Date'] = df['Order Date'].astype(str).str.replace("'", "", regex=False)
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        df.dropna(subset=['Order Date'], inplace=True)

    # 3. Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # 4. Remove wrong data
    if 'Quantity' in df.columns:
        df = df[df['Quantity'] >= 0]
    for col in ['Unit Price', 'Total Revenue']:
        if col in df.columns:
            df = df[df[col] >= 0]

    return df

if __name__ == "__main__":
    cleaned_mine_df = clean_mine_data('Mine.csv')
    cleaned_sales_df = clean_sales_data('Sales.csv')

    cleaned_mine_df.to_csv('Cleaned_Mine.csv', index=False)
    cleaned_sales_df.to_csv('Cleaned_Sales.csv', index=False)

    print("\n Cleaning complete. Files saved as 'Cleaned_Mine.csv' and 'Cleaned_Sales.csv'")

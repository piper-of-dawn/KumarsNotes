def shift_quarters(business_date: str, num_quarters: int) -> namedtuple:
    if isinstance(business_date, str):
        business_date = datetime.datetime.strptime(business_date, '%d/%m/%Y')
    # Calculate the number of months to shift based on the number of quarters
    num_months = (num_quarters - 1) * 3

    # Add the calculated number of months to the business_date to get the first date
    first_date = (business_date + datetime.timedelta(weeks=(num_months * 5))).replace(day=1)

  
    # Calculate the number of months to shift by 1 more quarter for the second date
    num_months = 3

    # Add the calculated number of months to the first_date to get the second date
    second_date = first_date + datetime.timedelta(weeks=num_months * 5)
    second_date = second_date.replace(day=1) - datetime.timedelta(days=1)

    # Create a namedtuple to store the two new dates
    Dates = namedtuple('Dates', ['first_date', 'second_date'])

    # Return the two new dates as a namedtuple
    return Dates(first_date.strftime('%d/%m/%Y'), second_date.strftime('%d/%m/%Y'))

# Test the function
business_date = '31/03/2023'
num_quarters = 3
result = shift_quarters(business_date, num_quarters)
print(result)


Get-ChildItem -Path 'C:\path\to\source' -File -Filter '*pattern*' | Copy-Item -Destination 'C:\path\to\destination'

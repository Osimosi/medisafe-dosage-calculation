# Accutane Medication Dosage Tracker

This project is a Python script designed to calculate the remaining dosage of Accutane (Isotretinoin) medication. Accutane has a specific cumulative dosage requirement that needs to be taken over a prescribed period, typically six months. This script helps you track your medication intake, identify any missed doses, and calculate the remaining dosage needed to meet the prescribed cumulative dosage.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Background

Accutane (Isotretinoin) is a medication often prescribed for severe acne. It requires strict adherence to a dosing schedule to achieve the desired cumulative dosage over the treatment period. This script was developed to help me manage and track my dosage, it especially useful if doses are missed or skipped.

## Features

- **Import medication data from CSV**: The script processes CSV data exported from the Medisafe app.
- **Calculate total dosage taken**: It computes the total amount of medication consumed.
- **Calculate remaining dosage**: It calculates the remaining dosage needed to meet the prescribed cumulative dosage.
- **Display progress**: Shows a progress bar and percentage of the cumulative dosage taken.

## Requirements

- Python 3.11
- Pandas
- NumPy

## Usage

1. **Prepare your CSV file**: Export your medication data from the Medisafe app and ensure it's saved in the same directory as the script.

2. **Run the script**: Execute the script in a Python environment. The script will prompt you to enter the name of your CSV file.


python calc.py


3. **Follow the prompts**: Enter the name of your CSV file when prompted (without the `.csv` extension).

### CSV File Format

Ensure your CSV file is structured as follows:

```
Type,  Name,  Recorded on,  Scheduled for,  Value,  Notes
Medication,  Isotretinoin 20,  4/16/23 4:10 AM,  4/16/23 4:10 AM,  Taken,   ...
```

### Example Output

```
name dat file boah: my_medication_data
Total dosage supposed to be taken = 6 months = 180 days
60mg per day = 180 * 60 = 10800 mg

Total pills popped (mg) =  280 mg 

Total pills skipped tsk tsk tsk =  60 mg 

gotta pop  10220.0 more pills of 40mg or  5110.0 more pills of 20mg

170.33333333333334 more days to go .-. 


Progress bar
------------
[#####                                             ]
Percentage of dosage taken =  5.833333333333333 %
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please submit a pull request or open an issue :)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

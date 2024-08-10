# California Housing Price Prediction

This project provides a web application for predicting California housing prices using a trained machine learning model. The application allows users to input various features related to housing and get an estimated price prediction.

## Project Structure

- `app.py`: Contains the main code for the Streamlit app. It handles user input, makes predictions using the trained model, and displays the result.
- `trained_model.sav`: The trained machine learning model saved in a `.sav` file format. Ensure this file is in the same directory as `app.py`.
- `requirements.txt`: Lists the Python packages required to run the application.
- `california_housing.csv`: Dataset used for creating this model
- `House_Prediction.ipynb`: Notebook file

## Requirements

To run this project, you need to install the required Python packages. You can do this using the `requirements.txt` file included in the project.

1. **Install Dependencies**:
   - Make sure you have `pip` installed.
   - Install the required packages by running:

     ```bash
     pip install -r requirements.txt
     ```

## Setup

1. **Ensure the Model File is Present**:
   - Place the `trained_model.sav` file in the same directory as `app.py`.

2. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `app.py`.
   - Run the following command to start the Streamlit server:

     ```bash
     streamlit run app.py
     ```

   - This command will start the Streamlit application and automatically open it in your default web browser.

## Usage

1. **Enter Data**:
   - **Median Income**: Enter the median income of the area.
   - **Median House Age**: Enter the median age of houses in the area.
   - **Average Number of Rooms**: Enter the average number of rooms per house.
   - **Average Number of Bedrooms**: Enter the average number of bedrooms per house.
   - **Block Group Population**: Enter the population of the block group.
   - **Average Number of Household Members**: Enter the average number of people per household.
   - **Latitude**: Enter the latitude of the house location.
   - **Longitude**: Enter the longitude of the house location (use negative values for Western Hemisphere).

2. **Predict**:
   - Click the **"Housing Price Prediction"** button to receive the predicted housing price.

3. **View Results**:
   - The predicted housing price will be displayed on the screen in USD.

## Troubleshooting

- **Error Handling**: If an error occurs, ensure all input fields contain valid numeric values. Check that `trained_model.sav` is correctly placed and not corrupted.

- **Common Issues**:
  - Ensure no fields are left empty.
  - Verify that the data types for each input are correct.

## Contributing

Contributions are welcome! To contribute to this project, please fork the repository and create a pull request with your changes. Ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [rishankj749@gmail.com].

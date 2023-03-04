import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import requests
import pandas as pd
from PIL import Image, ImageTk


class SurveyGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Recommended Sprinkler Usage")
        self.master.geometry("1500x1500")  # set window size
        self.pack(fill=tk.BOTH, expand=True)  # fill the screen

        # Add a title
        title_label = tk.Label(self, text="Sprinkler Recommendation System", font=("Arial", 30))
        title_label.pack(pady=10)

        # Load the sustainability image
        img = Image.open("/Users/adishsundar/Desktop/growing-zone-map-e1632410337830.webp")
        img = img.resize((250, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # Add the image to the GUI
        self.image_label = tk.Label(self, image=img)
        self.image_label.image = img
        self.image_label.pack(pady=10)

        # First Question in the Survey
        # Add another input question
        self.input_var2 = tk.StringVar()
        question_label2 = tk.Label(self, text="What Climate Zone do you live in (1-11):", font=("Arial", 10))
        question_label2.pack(pady=10)
        input_entry2 = tk.Entry(self, textvariable=self.input_var2)
        input_entry2.pack(pady=5)

        # Second Question in the Survey
        # Add a question that allows user input
        self.input_var = tk.StringVar()
        input_label = tk.Label(self, text="What city do you live in?", font=("Arial", 10))
        input_label.pack(pady=10)
        input_entry = tk.Entry(self, textvariable=self.input_var)
        input_entry.pack(pady=5)

        # Third Question in the Survey
        # Add a question that allows user input
        self.input_var3 = tk.StringVar()
        input_label3 = tk.Label(self, text="What type of sprinkler do you have? Enter 1 for rotor, 2 for spray, or 3 for drip:", font=("Arial", 10))
        input_label3.pack(pady=10)
        input_entry3 = tk.Entry(self, textvariable=self.input_var3)
        input_entry3.pack(pady=5)

        # Add a submit button after all the questions
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.pack(pady=10)

        # First output - How much water their garden needs
        self.output_label4 = tk.Label(self, text="", font=("Arial", 10))
        self.output_label4.pack(pady=10)

        # Second output showing how much upcoming rainfall their is
        self.output_label3 = tk.Label(self, text="Here is rainfall data in inches over the upcoming week:",
                                      font=("Arial", 10))
        self.output_label3.pack(pady=10)

        # Shows Rainfall Data
        self.output_label2 = tk.Label(self, text="", font=("Arial", 10))
        self.output_label2.pack(pady=10)

        # Prints after Rainfall Data is shown
        self.output_label5 = tk.Label(self, text="", font=("Arial", 10))
        self.output_label5.pack(pady=10)

        # Prints for Sprinkler Info
        self.output_label6 = tk.Label(self, text="", font=("Arial", 10))
        self.output_label6.pack(pady=10)

        # Final Recommendation
        self.output_label = tk.Label(self, text="", font=("Arial", 20))
        self.output_label.pack(pady=10)

    # Function to submit the survey
    def submit(self):
        city_name = self.input_var.get()
        # sprinkler_head = self.color_var.get()

        zone = self.input_var2.get()

        sprinkler_input = self.input_var3.get()

        # API key
        api_key = '83e66063a2f7ce7efad23b2c390b1666'

        # API endpoint
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric'

        # Make API request
        response = requests.get(url)

        # Parse JSON response
        json_data = response.json()

        precipitation_data = []
        for item in json_data['list']:
            try:
                precipitation = item['rain']['3h']
            except KeyError:
                precipitation = 0
            precipitation_data.append({
                'date': pd.Timestamp(item['dt'], unit='s'),
                'precipitation': round((precipitation / 25.4), 3)
            })


        x = str((precipitation_data[0]))

        month = x[25:27]

        # Convert to pandas DataFrame and set date column as index
        df = pd.DataFrame(precipitation_data)
        df.set_index('date', inplace=True)

        # Resample data by day and calculate total precipitation
        daily_precipitation = df['precipitation'].resample('D').sum()

        total_precipitation = round(df['precipitation'].sum(), 3)

        # Get the days when there was no precipitation
        no_precipitation_days = daily_precipitation[daily_precipitation == 0]

        # Get the names of the days when there was no precipitation
        no_watering_days = no_precipitation_days.index.day_name()

        month_int = int(month)
        if month_int >= 5 and month_int <= 8:
            num = 1.25
        elif month_int >= 11 or month_int <= 2:
            num = 0.75
        else:
            num = 1

        if zone == '1':
            num *= .7
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '2':
            num *= .81
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '3':
            num *= .76
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '4':
            num *= .95
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '5':
            num *= 1.0
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '6':
            num *= 1.1
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '7':
            num *= 1.2
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '8':
            num *= 1.3
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '9':
            num *= 1.5
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '10':
            num *= 1.4
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        elif zone == '11':
            num *= 1.2
            output_text4 = f'Your garden needs a total of {num} inches of water based off of the climate zone and month of current date.'
        else:
            print("Invalid input")

        if sprinkler_input == '1':
            sprinkler_type = 20
        elif sprinkler_input == '2':
            sprinkler_type = 25
        elif sprinkler_input == '3':
            sprinkler_type = 40
        else:
            print("Invalid input. Please enter either 1, 2, or 3.")

        # Update the output label
        self.output_label4.config(text = output_text4)

        output_text2 = "Over the next week, the predicted rainfall for {} is:\n\n".format(city_name)

        daily_precipitation = {}

        for index, row in df.iterrows():
            day_of_week = index.strftime('%A')
            if day_of_week not in daily_precipitation:
                daily_precipitation[day_of_week] = row['precipitation']
            else:
                daily_precipitation[day_of_week] += row['precipitation']

        for day, precipitation in daily_precipitation.items():
            output_text2 += f"{day}: {precipitation:.3f} inches\n"

        # Shows Data
        self.output_label2.config(text=output_text2)

        # Prints after Rainfall Data is shown
        # num = water needed, total_precipitation = rain for upcoming week
        difference = num - total_precipitation

        if difference > 0:
            self.output_label5.config(
                text=f"It will rain a total of {total_precipitation} inches in the upcoming week, so your garden needs "
                     f"{round(difference, 3)} inches of water.")
        else:
            self.output_label5.config(
                text=f"You do not need to water your garden")

        water_per_day = (round(difference, 3))/len(no_precipitation_days)

        if len(no_precipitation_days > 0):
            output_text = f"The days when you have to water your garden are: {', '.join(no_watering_days)}," \
                          f" so your garden needs {round(water_per_day, 3)} inches of water " \
                          f"each day!"
        else:
            output_text = "Thank you for using our service!"

        time_per_day = (water_per_day / 0.5) * sprinkler_type
        roundedtime = round(time_per_day, 3)

        # Final Recommendations
        self.output_label.config(text=output_text)

        self.output_label6.config(text = f'We recommend watering for {roundedtime} minutes per day to meet the '
                                         f'optimal watering rate of {num} inches per week based off of your sprinkler type.'
                                         f'\n\nWe recommend watering in the early morning prior to 10 a.m. to allow the water to soak into the soil before evaporation can occur!')


# Start the GUI
root = tk.Tk()
survey_gui = SurveyGUI(root)
survey_gui.mainloop()

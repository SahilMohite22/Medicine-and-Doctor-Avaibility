from flask import Flask, render_template, request

app = Flask(__name__)

# Mocking the list of specializations, locations, and doctors
specializations = ['Cardiology', 'Orthopedics', 'Dermatology', 'Pediatrics', 'Gynecology']
locations = ['Mumbai', 'Delhi', 'Chennai', 'Hyderabad', 'Bangalore', 'Kanpur', 'Ahmedabad', 'Pune']
doctors = ['Dr. Sneha Kapoor', 'Dr. Vikas Deshmukh', 'Dr. Ayesha Patel', 'Dr. Sameera Singh',
           'Dr. Varun Reddy', 'Dr. Kavita Desai', 'Dr. Rishi Verma', 'Dr. Nandini Gupta',
           'Dr. Abhinav Patel', 'Dr. Ananya Kumar', 'Dr. Vivek Joshi', 'Dr. Ishita Malhotra',
           'Dr. Prateek Deshmukh', 'Dr. Sanjana Yadav']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        specialization = request.form.get('specialization')
        location = request.form.get('location')
        date = request.form.get('date')
        doctor = request.form.get('doctor')

        # Process the form data or perform further actions
        # For now, just printing the values to the console
        print(f'Specialization: {specialization}')
        print(f'Location: {location}')
        print(f'Date: {date}')
        print(f'Doctor: {doctor}')

    return render_template('form.html', specializations=specializations, locations=locations, doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)

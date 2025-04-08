# 🧮 Unit Converter Web App 🌐

This is a simple web application that allows users to convert between various units of measurement. Users can input a value and select the units to convert from and to, and the application will return the converted value.

## Features

- **📏 Length Conversion**: Convert between millimeter, centimeter, meter, kilometer, inch, foot, yard, and mile.
- **⚖️ Weight Conversion**: Convert between milligram, gram, kilogram, ounce, and pound.
- **🌡️ Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.

## How It Works 🔧
The application provides three main pages for converting between different units of measurement:

- **📏 Length Conversion**: Convert between various units of length, including millimeter, centimeter, meter, kilometer, inch, foot, yard, and mile.
- **⚖️ Weight Conversion**: Convert between different weight units, such as milligram, gram, kilogram, ounce, and pound.
- **🌡️ Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.

Each page contains a form where users can input a value and select the units they wish to convert from and to. Upon form submission, the server will calculate the converted value and display it on the same page.

### Form Submission Logic 📥
The form is submitted to the same page using the POST method. The backend checks if the form has been submitted and then calculates the converted value. If the form is not submitted, it will display the form for input.

### Conversion Functions 🔄
- **📏 Length Conversion**: The application uses predefined conversion factors to convert between different length units.
- **⚖️ Weight Conversion**: Similar to length conversion, weight conversions are handled using predefined conversion factors.
- **🌡️ Temperature Conversion**: Temperature conversion uses standard formulas for converting between Celsius, Fahrenheit, and Kelvin.

## Installation 🛠️

To run this application locally, follow these steps:

### 1. Clone the repository
```sh
git clone https://github.com/shdh23/unit_converter/
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the application
```sh
python app.py
```

unit-converter/  
│
├── app.py              # Flask application logic  
├── templates/          # HTML templates for the web pages  
│   ├── layout.html     # Base template with common UI elements  
│   ├── length.html     # Length conversion page  
│   ├── weight.html     # Weight conversion page  
│   └── temperature.html # Temperature conversion page  
├── static/             # Static files like CSS  
│   └── style.css       # Styles for the application  
├── requirements.txt    # List of dependencies  
└── README.md           # This file


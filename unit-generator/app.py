from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')  # Ensure this points to your correct HTML file

# Conversion route
@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    conversion_type = data.get('conversionType')
    value = data.get('value')
    from_unit = data.get('fromUnit')
    to_unit = data.get('toUnit')

    # Input validation
    try:
        value = float(value)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid value input. Please enter a numeric value."}), 400

    # Conversion logic
    try:
        if conversion_type == 'length':
            converted_value = convert_length(value, from_unit, to_unit)
        elif conversion_type == 'temperature':
            converted_value = convert_temperature(value, from_unit, to_unit)
        elif conversion_type == 'weight':
            converted_value = convert_weight(value, from_unit, to_unit)
        else:
            return jsonify({"error": "Invalid conversion type."}), 400

        return jsonify({"convertedValue": converted_value})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

def convert_length(value, from_unit, to_unit):
    # Conversion logic for length
    conversions = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'centimeters': 0.01,
        'inches': 0.0254,
        'yards': 0.9144
    }

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported unit for length conversion: {from_unit} or {to_unit}")
    
    # Convert value to meters
    value_in_meters = value * conversions[from_unit]
    # Convert meters to target unit
    converted_value = value_in_meters / conversions[to_unit]
    
    return round(converted_value, 4)

def convert_temperature(value, from_unit, to_unit):
    # Conversion logic for temperature
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return round((value * 9/5) + 32, 2)
        elif to_unit == 'kelvin':
            return round(value + 273.15, 2)
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return round((value - 32) * 5/9, 2)
        elif to_unit == 'kelvin':
            return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return round(value - 273.15, 2)
        elif to_unit == 'fahrenheit':
            return round((value - 273.15) * 9/5 + 32, 2)
    
    if from_unit == to_unit:
        return round(value, 2)
    
    raise ValueError(f"Unsupported unit for temperature conversion: {from_unit} or {to_unit}")

def convert_weight(value, from_unit, to_unit):
    # Conversion logic for weight
    conversions = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495
    }

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported unit for weight conversion: {from_unit} or {to_unit}")
    
    # Convert value to grams
    value_in_grams = value * conversions[from_unit]
    # Convert grams to target unit
    converted_value = value_in_grams / conversions[to_unit]
    
    return round(converted_value, 4)

if __name__ == '__main__':
    app.run(debug=True)

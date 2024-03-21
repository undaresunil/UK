#api flask?
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime, timedelta
import random

# Init app
app = Flask(__name__)
CORS(app)

#get post api
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})


@app.route('/diet', methods=['POST'])
def diet():
    data = request.get_json()
    print(data)

    # Define the list of food items with their nutritional content for protein and carbs separately
    protein_sources = [
        {'name': 'Chicken Breast', 'protein': 30, 'carbs': 0},
        {'name': 'Turkey Breast', 'protein': 25, 'carbs': 0},
        {'name': 'Eggs', 'protein': 6, 'carbs': 1},
        {'name': 'Tofu', 'protein': 8, 'carbs': 2},
        {'name': 'Lentils', 'protein': 9, 'carbs': 20},
        {'name': 'Greek Yogurt', 'protein': 10, 'carbs': 3},
        {'name': 'Almonds', 'protein': 21, 'carbs': 22},
        {'name': 'Milk', 'protein': 8, 'carbs': 12},
        {'name': 'Cottage Cheese', 'protein': 11, 'carbs': 3},
        {'name': 'Salmon', 'protein': 25, 'carbs': 0},
        {'name': 'Tuna', 'protein': 30, 'carbs': 0},
        {'name': 'Beef', 'protein': 36, 'carbs': 0},
        {'name': 'Pork', 'protein': 25, 'carbs': 0},
        {'name': 'Shrimp', 'protein': 24, 'carbs': 0},
        {'name': 'Lamb', 'protein': 25, 'carbs': 0},
        {'name': 'Bison', 'protein': 29, 'carbs': 0},
        {'name': 'Venison', 'protein': 30, 'carbs': 0},
        {'name': 'Duck', 'protein': 29, 'carbs': 0},
        {'name': 'Quail', 'protein': 25, 'carbs': 0},
        {'name': 'Goose', 'protein': 29, 'carbs': 0}
        # Add more protein sources here
    ]

    carbs_sources = [
        {'name': 'Brown Rice', 'protein': 5, 'carbs': 45},
        {'name': 'Quinoa', 'protein': 4, 'carbs': 21},
        {'name': 'Sweet Potato', 'protein': 2, 'carbs': 20},
        {'name': 'Oats', 'protein': 13, 'carbs': 68},
        {'name': 'Whole Grain Bread', 'protein': 8, 'carbs': 49},
        {'name': 'Bananas', 'protein': 1, 'carbs': 27},
        {'name': 'Apples', 'protein': 0, 'carbs': 25},
        {'name': 'Oranges', 'protein': 1, 'carbs': 21},
        {'name': 'Grapes', 'protein': 1, 'carbs': 27},
        {'name': 'Mangoes', 'protein': 1, 'carbs': 28},
        {'name': 'Pineapples', 'protein': 0, 'carbs': 22},
        {'name': 'Peaches', 'protein': 1, 'carbs': 21},
        {'name': 'Cherries', 'protein': 1, 'carbs': 18},
        {'name': 'Pears', 'protein': 1, 'carbs': 28},
        {'name': 'Plums', 'protein': 1, 'carbs': 16},
        {'name': 'Apricots', 'protein': 1, 'carbs': 11},
        {'name': 'Nectarines', 'protein': 1, 'carbs': 12},
        {'name': 'Papayas', 'protein': 1, 'carbs': 15},
        {'name': 'Watermelon', 'protein': 1, 'carbs': 8},
        {'name': 'Cantaloupe', 'protein': 1, 'carbs': 8}
        # Add more carbs sources here
    ]

    # Define the daily protein and carbs requirements
    daily_protein_requirement = data['Protien_intake']  # in grams
    daily_carbs_requirement = data['Carbs_intake']  # in grams

    # Define the time intervals for meals
    meal_timetable = {
        'Breakfast': {'start': '08:00', 'end': '09:00'},
        'Lunch': {'start': '12:00', 'end': '13:00'},
        'Dinner': {'start': '18:00', 'end': '19:00'}
    }

    # Shuffle the food items lists to randomize selection
    random.shuffle(protein_sources)
    random.shuffle(carbs_sources)

    # Initialize variables to track food item repetition
    protein_counts = {food['name']: 0 for food in protein_sources}
    carbs_counts = {food['name']: 0 for food in carbs_sources}
    selected_protein_today = {}
    selected_carbs_today = {}

    Timetable_dict={}
    # Generate the weekly timetable
    start_date = datetime.today()
    end_date = start_date + timedelta(days=(data['week']*7))  # One week

    current_date = start_date
    while current_date <= end_date:
        print(f"Diet Plan for {current_date.strftime('%A, %Y-%m-%d')}:")
        # print(Timetable_dict)
        # Reset counts at the start of each day
        protein_counts = {food['name']: 0 for food in protein_sources}
        carbs_counts = {food['name']: 0 for food in carbs_sources}
        selected_protein_today = {}
        selected_carbs_today = {}
        
        total_protein_intake = 0
        total_carbs_intake = 0
        
        for meal, timing in meal_timetable.items():
            # print(f"{meal} ({timing['start']} - {timing['end']}):")
            
            # Select a protein source for the current mealtime
            selected_protein = None
            while not selected_protein:
                selected_protein = random.choice(protein_sources)
                if protein_counts[selected_protein['name']] >= 2:
                    selected_protein = None
            
            selected_protein_today[meal] = selected_protein['name']
            protein_counts[selected_protein['name']] += 1

            # Calculate protein intake amount for the current meal
            remaining_protein = daily_protein_requirement - total_protein_intake
            protein_intake_amount = min(remaining_protein, selected_protein['protein'])
            total_protein_intake += protein_intake_amount
            
            # Select a carbs source for the current mealtime
            selected_carbs = None
            
            while not selected_carbs:
                selected_carbs = random.choice(carbs_sources)
                if carbs_counts[selected_carbs['name']] >= 2:
                    selected_carbs = None
            
            selected_carbs_today[meal] = selected_carbs['name']
            carbs_counts[selected_carbs['name']] += 1

            # Calculate carbs intake amount for the current meal
            remaining_carbs = daily_carbs_requirement - total_carbs_intake
            carbs_intake_amount = min(remaining_carbs, selected_carbs['carbs'])
            total_carbs_intake += carbs_intake_amount
            Timetable_dict[current_date.strftime('%A, %Y-%m-%d')]={'Protiein':selected_protein['name'],'Carbs':selected_carbs['name']}
        
        current_date += timedelta(days=1)

    return jsonify({'data': Timetable_dict})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

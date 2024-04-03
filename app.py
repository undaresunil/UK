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
# 
    # veg = data['veg']
    # Define the list of food items with their nutritional content for protein and carbs separately
    protein_sources = {
        "Veg": [
            {'name': 'Tofu', 'protein': 8, 'carbs': 2},
            {'name': 'Lentils', 'protein': 9, 'carbs': 20},
            {'name': 'Greek Yogurt', 'protein': 10, 'carbs': 3},
            {'name': 'Almonds', 'protein': 21, 'carbs': 22},
            {'name': 'Milk', 'protein': 8, 'carbs': 12},
            {'name': 'Cottage Cheese', 'protein': 11, 'carbs': 3},
            {'name': 'Chickpeas', 'protein': 9, 'carbs': 27},
            {'name': 'Peanuts', 'protein': 26, 'carbs': 16},
            {'name': 'Green Peas', 'protein': 5, 'carbs': 14},
            {'name': 'Pumpkin Seeds', 'protein': 19, 'carbs': 10},
            {'name': 'Chia Seeds', 'protein': 17, 'carbs': 12},
            {'name': 'Quinoa', 'protein': 4, 'carbs': 21},
            {'name': 'Soy Milk', 'protein': 7, 'carbs': 4},
            {'name': 'Edamame', 'protein': 11, 'carbs': 10},
            {'name': 'Tempeh', 'protein': 19, 'carbs': 9},
            {'name': 'Seitan', 'protein': 25, 'carbs': 9}
            # Add more vegetarian protein sources here
        ],
        "Non_veg": [
            {'name': 'Chicken Breast', 'protein': 30, 'carbs': 0},
            {'name': 'Turkey Breast', 'protein': 25, 'carbs': 0},
            {'name': 'Eggs', 'protein': 6, 'carbs': 1},
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
            {'name': 'Goose', 'protein': 29, 'carbs': 0},
            {'name': 'Rabbit', 'protein': 29, 'carbs': 0},
            {'name': 'Elk', 'protein': 30, 'carbs': 0},
            {'name': 'Ostrich', 'protein': 28, 'carbs': 0},
            {'name': 'Buffalo', 'protein': 29, 'carbs': 0},
            {'name': 'Alligator', 'protein': 46, 'carbs': 0},
            {'name': 'Kangaroo', 'protein': 27, 'carbs': 0}
        ]
    }

    carbs_sources = {
    "Veg": [
        {'name': 'Brown Rice', 'protein': 5, 'carbs': 25},
        {'name': 'Quinoa', 'protein': 4, 'carbs': 21},
        {'name': 'Sweet Potato', 'protein': 2, 'carbs': 20},
        {'name': 'Oats', 'protein': 13, 'carbs': 28},
        {'name': 'Whole Grain Bread', 'protein': 8, 'carbs': 29},
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
        # Add more vegetarian carbs sources here
    ],
    "Non Veg": [
        {'name': 'White Rice', 'protein': 3, 'carbs': 28},
        {'name': 'Pasta', 'protein': 6, 'carbs': 25},
        {'name': 'Bread', 'protein': 6, 'carbs': 24},
        {'name': 'Potatoes', 'protein': 2, 'carbs': 17},
        {'name': 'Corn', 'protein': 2, 'carbs': 19},
        {'name': 'Peas', 'protein': 5, 'carbs': 14},
        {'name': 'Beans', 'protein': 7, 'carbs': 23},
        {'name': 'Barley', 'protein': 3, 'carbs': 32},
        {'name': 'Pumpkin', 'protein': 1, 'carbs': 6},
        {'name': 'Carrots', 'protein': 1, 'carbs': 12},
        {'name': 'Onions', 'protein': 1, 'carbs': 9},
        {'name': 'Tomatoes', 'protein': 1, 'carbs': 4},
        {'name': 'Bell Peppers', 'protein': 1, 'carbs': 6},
        {'name': 'Broccoli', 'protein': 3, 'carbs': 7},
        {'name': 'Spinach', 'protein': 3, 'carbs': 4},
        {'name': 'Lettuce', 'protein': 1, 'carbs': 2},
        {'name': 'Cucumbers', 'protein': 1, 'carbs': 4},
        {'name': 'Zucchini', 'protein': 1, 'carbs': 3},
        {'name': 'Eggplant', 'protein': 1, 'carbs': 5},
        {'name': 'Mushrooms', 'protein': 3, 'carbs': 3}
        # Add more non-vegetarian carbs sources here
    ]
}


    # Define the daily protein and carbs requirements
    daily_protein_requirement = int(data['Protien_intake'])  # in grams
    daily_carbs_requirement = int(data['Carbs_intake'])  # in grams

    # Define the time intervals for meals
    meal_timetable = {
        'Breakfast': {'start': '08:00', 'end': '09:00'},
        'Lunch': {'start': '12:00', 'end': '13:00'},
        'Dinner': {'start': '18:00', 'end': '19:00'}
    }

    if data['mealType']=="Veg":
        protein_sources=protein_sources["Veg"]
        carbs_sources=carbs_sources["Veg"]
    else:
        protein_sources=protein_sources["Non_veg"]
        carbs_sources=carbs_sources["Non Veg"]
        
    print(protein_sources,"==========================================================================")
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
    end_date = start_date + timedelta(days=int(data['week'])*7)  # One week

    current_date = start_date
    while current_date <= end_date:
        # print(f"Diet Plan for {current_date.strftime('%A, %Y-%m-%d')}:")
        Timetable_dict[current_date.strftime('%A, %Y-%m-%d')]={}
        # Reset counts at the start of each week
        if current_date.weekday() == 0:  # Monday
            protein_counts = {food['name']: 0 for food in protein_sources}
            carbs_counts = {food['name']: 0 for food in carbs_sources}
            selected_protein_today = {}
            selected_carbs_today = {}
            # Reshuffle food items at the start of each week
            random.shuffle(protein_sources)
            random.shuffle(carbs_sources)
        
        for meal, timing in meal_timetable.items():
            # print(f"{meal} ({timing['start']} - {timing['end']}):")
            
            # Select a protein source for the current mealtime
            selected_protein = None
            while not selected_protein:
                selected_protein = random.choice(protein_sources)
                if selected_protein['name'] in selected_protein_today.values() or protein_counts[selected_protein['name']] >= 2:
                    selected_protein = None
            
            selected_protein_today[meal] = selected_protein['name']
            protein_counts[selected_protein['name']] += 1

            protein_intake_amount = daily_protein_requirement * (selected_protein['protein'] / sum(food['protein'] for food in protein_sources))
            
            # Select a carbs source for the current mealtime
            selected_carbs = None
            
            while not selected_carbs:
                selected_carbs = random.choice(carbs_sources)
                if selected_carbs['name'] in selected_carbs_today.values() or carbs_counts[selected_carbs['name']] >= 2:
                    selected_carbs = None
            
            selected_carbs_today[meal] = selected_carbs['name']
            carbs_counts[selected_carbs['name']] += 1

            carbs_intake_amount = daily_carbs_requirement * (selected_carbs['carbs'] / sum(food['carbs'] for food in carbs_sources))
            
            # print(f"\t- Protein Source: {selected_protein['name']}: {protein_intake_amount:.2f} grams")
            # print(f"\t- Carbs Source: {selected_carbs['name']}: {carbs_intake_amount:.2f} grams")
            Timetable_dict[current_date.strftime('%A, %Y-%m-%d')][meal]={"protein":selected_protein['name'],"carbs":selected_carbs['name']}
        current_date += timedelta(days=1)

    # Mapping protein values
    for date_key, meals in Timetable_dict.items():
        for meal_key, nutrients in meals.items():
            print(nutrients)
            print(meal_key)
            protein_name = nutrients['protein']
            for source in protein_sources:
                if source['name'] == protein_name:
                    nutrients['protein'] = {'name': protein_name, 'protein': source['protein']}
            
            carbs_name = nutrients['carbs']
            for source in carbs_sources:
                if source['name'] == carbs_name:
                    nutrients['carbs'] = {'name': carbs_name, 'carbs': source['carbs']}
                if source['name'] == carbs_name:
                    nutrients['carbs'] = {'name': carbs_name, 'carbs': source['carbs']}
    for i,v in Timetable_dict.items():
        tot1=[]
        tot=[]
        for j,k in v.items():
            tot.append(k['protein']['protein'])
            tot1.append(k['carbs']['carbs'])
        sum1=sum(tot)
        sum2=sum(tot1)
        print(f"tot:{tot}, tot1:{tot1}")
        print(f"sum1:{sum1}, sum2:{sum2}")
        Diff_protein=100-sum1
        Diff_carbs=100-sum2
        New_p=round(Diff_protein/len(v), 2)
        New_c=round(Diff_carbs/len(v), 2)
        print(f"Diff_protein:{Diff_protein}, Diff_carbs:{Diff_carbs}")
        print(f"New_p:{New_p}, New_c:{New_c}")
        print("==================================================")
        for i,v in Timetable_dict.items():
            for j,k in v.items():
                k['protein']['protein'] += New_p
                k['carbs']['carbs'] += New_c
        
    print(Timetable_dict)

    return jsonify({'data': Timetable_dict})

# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

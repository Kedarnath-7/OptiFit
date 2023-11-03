# Import libraries for user data storage
import json

class UserProfile:
    def __init__(self, name, age, gender, weight_kg, height_cm):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm

# Create a user profile
user1 = UserProfile("Alice", 25, "Female", 65, 165)
user2 = UserProfile("Bob", 30, "Male", 80, 175)


class WearableDevice:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.steps = 0
        self.sleep_hours = 0

    def collect_data(self, steps, sleep_hours):
        self.steps = steps
        self.sleep_hours = sleep_hours
        self.update_user_profile()

    def update_user_profile(self):
        # Update user profile with wearable data
        self.user_profile.steps = self.steps
        self.user_profile.sleep_hours = self.sleep_hours

# Simulate data collection from wearables
wearable1 = WearableDevice(user1)
wearable1.collect_data(8000, 7)
wearable2 = WearableDevice(user2)
wearable2.collect_data(10000, 6)


class HealthRecommendation:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def generate_recommendations(self):
        # Use machine learning and AI models to generate recommendations
        # This can include dietary advice, exercise plans, and sleep guidelines
        recommendations = {
            "calories": 2200,
            "exercise": "30 minutes of cardio",
            "meal_plan": "Balanced diet with plenty of vegetables",
            "sleep_hours": 7,
            "hydration": "Stay hydrated throughout the day",
        }
        return recommendations

# Generate personalized health recommendations
recommendation1 = HealthRecommendation(user1)
user1_recommendations = recommendation1.generate_recommendations()
recommendation2 = HealthRecommendation(user2)
user2_recommendations = recommendation2.generate_recommendations()


# Create a dictionary to store user profiles (simulated data for demonstration)
user_profiles = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "gender": "Female",
        "weight_kg": 65,
        "height_cm": 165,
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "gender": "Male",
        "weight_kg": 80,
        "height_cm": 175,
    },
}

# Function to calculate daily calorie needs based on user profile
def calculate_daily_calories(user_profile, activity_level):
    # Calculate BMR (Basal Metabolic Rate) using Harris-Benedict equation
    if user_profile["gender"] == "Female":
        bmr = 655 + 9.6 * user_profile["weight_kg"] + 1.8 * user_profile["height_cm"] - 4.7 * user_profile["age"]
    else:
        bmr = 66 + 13.7 * user_profile["weight_kg"] + 5 * user_profile["height_cm"] - 6.8 * user_profile["age"]

    # Adjust for activity level
    activity_levels = {"sedentary": 1.2, "lightly_active": 1.375, "moderately_active": 1.55, "very_active": 1.725}
    daily_calories = bmr * activity_levels.get(activity_level, 1.2)

    return daily_calories

# Function to generate a personalized health plan
def generate_health_plan(user_profile, activity_level):
    daily_calories = calculate_daily_calories(user_profile, activity_level)
    plan = {
        "calories": daily_calories,
        "exercise": "30 minutes of moderate-intensity exercise",
        "meal_plan": "Balanced diet with a focus on fruits and vegetables",
        "sleep_hours": 7,
        "hydration": "Drink at least 8 glasses of water per day",
    }
    return plan

# Simulated user input
user_name = "user1"
activity_level = "lightly_active"  # Adjust this based on user input

if user_name in user_profiles:
    user_profile = user_profiles[user_name]
    health_plan = generate_health_plan(user_profile, activity_level)
    print(f"Hello {user_profile['name']}! Here's your personalized health plan:")
    print(json.dumps(health_plan, indent=4))
else:
    print("User not found. Please create a user profile.")

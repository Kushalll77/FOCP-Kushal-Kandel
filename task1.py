import time

def get_user_input():
    while True:
        try:
            num_pizzas = get_positive_integer_input('🍕 How many pizzas ordered? ')
            is_delivery = get_yes_no_input('🚚 Is delivery required? ')
            is_tuesday = get_yes_no_input('📅 Is it Tuesday? ')
            is_app_order = get_yes_no_input('📱 Did the customer use the app? ')

            return num_pizzas, is_tuesday, is_delivery, is_app_order
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyboardInterrupt:
            print("\nProgram terminated by the user.")
            exit()
            

def get_positive_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                raise ValueError("Please enter a positive integer!")
            return user_input
        except ValueError:
            print("Please enter a valid number!")

#Error handling
def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in {'yes', 'no'}:
            return user_input == 'yes'
        else:
            print('Please answer "Yes" or "No".')


def calculate_total_price(num_pizzas, is_tuesday, is_delivery, is_app_order):
    pizza_price = 12.00
    delivery_cost = 2.50
    app_discount = 0.25
    tuesday_discount = 0.50

    # Apply Tuesday discount
    if is_tuesday:
        pizza_price *= (1 - tuesday_discount)

    # Calculate costs with delivery
    total_pizza_cost = num_pizzas * pizza_price
    total_delivery_cost = delivery_cost if is_delivery and num_pizzas < 5 else 0.00
    total_cost_before_app = total_pizza_cost + total_delivery_cost

    # Apply app discount
    total_cost = total_cost_before_app * (1 - app_discount) if is_app_order else total_cost_before_app

    # Display the total price with delay effect
    print("\nCalculating the total price...\n")
    time.sleep(1)
    print(f'💸 Total Price: £{total_cost:.2f}\n')


def main():
    print("BPP Pizza Price Calculator 🍕📊")
    print("==========================")
    
    # Get user input and calculate total price
    user_inputs = get_user_input()
    calculate_total_price(*user_inputs)

main()
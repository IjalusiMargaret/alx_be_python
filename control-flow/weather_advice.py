def main():
    # Prompt the user for the weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

    # Check the weather conditions and provide clothing recommendations
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the main function
if __name__ == "__main__":
    main()
 
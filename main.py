import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_numbers(count=5, min_value=1, max_value=100):
    """Generate a list of random numbers and log them."""
    numbers = [random.randint(min_value, max_value) for _ in range(count)]
    logging.info(f"Generated random numbers: {numbers}")
    return numbers

if __name__ == "__main__":
    while True:
        generate_random_numbers()
        time.sleep(5)  # Wait 5 seconds before generating again

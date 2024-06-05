from PIL import Image
import random

def generate_key_schedule(key, length):
    
    random.seed(key)
    return [random.randint(0, 255) for _ in range(length)]

def encrypt_image(input_image_path, output_image_path, key):
    
    # Open the input image
    image = Image.open(input_image_path)
    image = image.convert("RGB")

    # Get image dimensions
    width, height = image.size

    # Generate key schedule
    key_schedule = generate_key_schedule(key, width * height * 3)  # 3 channels per pixel

    # Create a new image for the encrypted data
    encrypted_image = Image.new("RGB", (width, height))

    # Loop through each pixel of the image
    pixel_index = 0
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = image.getpixel((x, y))

            # Apply encryption operation with the key schedule on each color channel
            new_pixel = tuple([(channel + key_schedule[pixel_index + i]) % 256 for i, channel in enumerate(pixel)])
            pixel_index += 3

            # Set the encrypted pixel value in the new image
            encrypted_image.putpixel((x, y), new_pixel)

    # Save the encrypted image in PNG format
    encrypted_image.save(output_image_path, "PNG")

def decrypt_image(encrypted_image_path, output_image_path, key):
    
    # Open the encrypted image
    image = Image.open(encrypted_image_path)
    image = image.convert("RGB")

    # Get image dimensions
    width, height = image.size

    # Generate key schedule
    key_schedule = generate_key_schedule(key, width * height * 3)  # 3 channels per pixel

    # Create a new image for the decrypted data
    decrypted_image = Image.new("RGB", (width, height))

    # Loop through each pixel of the image
    pixel_index = 0
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = image.getpixel((x, y))

            # Reverse the encryption operation with the key schedule on each color channel
            new_pixel = tuple([(channel - key_schedule[pixel_index + i]) % 256 for i, channel in enumerate(pixel)])
            pixel_index += 3

            # Set the decrypted pixel value in the new image
            decrypted_image.putpixel((x, y), new_pixel)

    # Save the decrypted image in PNG format
    decrypted_image.save(output_image_path, "PNG")

# Example usage
input_image = './image.jpg'
output_encrypted_image = './encrypted_image.png'
output_decrypted_image = './decrypted_image.png'
key = 128  # encryption key

encrypt_image(input_image, output_encrypted_image, key)
decrypt_image(output_encrypted_image, output_decrypted_image, key)
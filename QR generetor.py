#!/usr/bin/env python
# coding: utf-8

# In[1]:


import segno


# In[2]:


import qrcode
from PIL import Image, ImageShow

def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

    # Display the QR code
    img.show()

if __name__ == "__main__":
    # Input data for the QR code
    data_to_encode = input("Enter the data you want to encode in the QR code: ")

    # Specify the file name for the generated QR code image
    file_name = input("Enter the file name for the QR code image (include extension like .png): ")

    # Generate and display the QR code
    generate_qr_code(data_to_encode, file_name)


# In[ ]:





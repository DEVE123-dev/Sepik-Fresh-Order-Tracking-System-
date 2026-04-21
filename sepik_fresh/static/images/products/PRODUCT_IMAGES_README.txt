PRODUCT IMAGES FOLDER
=====================

This folder stores product images uploaded by administrators.

HOW TO ADD PRODUCT IMAGES:
--------------------------
1. Log in as an admin user
2. Navigate to the Products page
3. Find the product you want to add an image for
4. Click the "Add Image" or "Update Image" button on the product card
5. Select an image file from your computer (PNG, JPG, JPEG, GIF, or WEBP)
6. The image will be automatically uploaded and displayed

SUPPORTED IMAGE FORMATS:
-----------------------
- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- WEBP (.webp)

IMAGE RECOMMENDATIONS:
---------------------
- Use high-quality images (at least 800x800 pixels)
- Keep file sizes reasonable (under 2MB for faster loading)
- Use clear, well-lit photos of products
- Square or landscape orientation works best
- Show the product clearly without too much background clutter

AUTOMATIC FEATURES:
------------------
- Images are automatically resized to fit the display areas
- Each image gets a unique filename to prevent conflicts
- Old images are kept when you upload new ones (manual cleanup may be needed)
- Images appear in:
  * Product listing page (for customers and admins)
  * Order placement page (for customers)
  * Home page slideshow (featured products)

MANUAL IMAGE MANAGEMENT:
-----------------------
You can also manually add images to this folder:
1. Name your image file descriptively (e.g., "fresh_chicken.jpg")
2. Upload it to this folder via FTP or file manager
3. Update the database directly with the image path:
   UPDATE products SET image_url='/static/images/products/fresh_chicken.jpg' WHERE product_id=X;

Note: Using the admin interface is recommended for easier management.

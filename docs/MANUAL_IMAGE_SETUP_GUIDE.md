# Manual Product Image Setup Guide

## Simple 3-Step Process

### Step 1: Add Database Column

Run this SQL in phpMyAdmin:

```sql
ALTER TABLE products 
ADD COLUMN IF NOT EXISTS image_url VARCHAR(500) DEFAULT NULL 
AFTER description;
```

### Step 2: Add Your Images to Folder

1. Get your product images (chicken, eggs, etc.)
2. Save them to: `sepik_fresh/static/images/products/`
3. Name them something simple like:
   - `chicken.jpg`
   - `eggs.jpg`
   - `chicken_pieces.jpg`
   - `egg_tray.jpg`

### Step 3: Update Database with Image Paths

Run these SQL commands in phpMyAdmin to link images to products:

```sql
-- For Whole Fresh Chicken (product_id = 2)
UPDATE products 
SET image_url = '/static/images/products/chicken.jpg' 
WHERE product_id = 2;

-- For Chicken Pieces (product_id = 3)
UPDATE products 
SET image_url = '/static/images/products/chicken_pieces.jpg' 
WHERE product_id = 3;

-- For Fresh Eggs Tray (product_id = 4)
UPDATE products 
SET image_url = '/static/images/products/egg_tray.jpg' 
WHERE product_id = 4;

-- For Fresh Eggs Dozen (product_id = 5)
UPDATE products 
SET image_url = '/static/images/products/eggs.jpg' 
WHERE product_id = 5;
```

## Image Path Format

The image path format is always:
```
/static/images/products/YOUR_IMAGE_NAME.jpg
```

Examples:
- `/static/images/products/chicken.jpg`
- `/static/images/products/eggs.png`
- `/static/images/products/fresh_chicken.jpg`
- `/static/images/products/egg_tray_30.jpg`

## Quick Reference for Your Products

Based on your current database, here are the products and suggested image names:

| Product ID | Product Name | Suggested Image Name | SQL Command |
|------------|--------------|---------------------|-------------|
| 2 | Whole Fresh Chicken (1.5kg) | `chicken.jpg` | `UPDATE products SET image_url = '/static/images/products/chicken.jpg' WHERE product_id = 2;` |
| 3 | Chicken Pieces (1kg) | `chicken_pieces.jpg` | `UPDATE products SET image_url = '/static/images/products/chicken_pieces.jpg' WHERE product_id = 3;` |
| 4 | Fresh Eggs (Tray of 30) | `egg_tray.jpg` | `UPDATE products SET image_url = '/static/images/products/egg_tray.jpg' WHERE product_id = 4;` |
| 5 | Fresh Eggs (Dozen) | `eggs_dozen.jpg` | `UPDATE products SET image_url = '/static/images/products/eggs_dozen.jpg' WHERE product_id = 5;` |

## Where to Get Free Product Images

Download free stock images from:
- **Unsplash.com** - High quality, free to use
- **Pexels.com** - Free stock photos
- **Pixabay.com** - Free images and photos

Search for:
- "fresh chicken"
- "whole chicken"
- "chicken pieces"
- "fresh eggs"
- "egg tray"
- "dozen eggs"

## Complete Example Workflow

1. **Download 4 images** for your products
2. **Rename them:**
   - Image 1 → `chicken.jpg`
   - Image 2 → `chicken_pieces.jpg`
   - Image 3 → `egg_tray.jpg`
   - Image 4 → `eggs_dozen.jpg`

3. **Copy to folder:**
   ```
   sepik_fresh/static/images/products/
   ```

4. **Run SQL:**
   ```sql
   UPDATE products SET image_url = '/static/images/products/chicken.jpg' WHERE product_id = 2;
   UPDATE products SET image_url = '/static/images/products/chicken_pieces.jpg' WHERE product_id = 3;
   UPDATE products SET image_url = '/static/images/products/egg_tray.jpg' WHERE product_id = 4;
   UPDATE products SET image_url = '/static/images/products/eggs_dozen.jpg' WHERE product_id = 5;
   ```

5. **Refresh your browser** - Images will appear!

## Checking Your Product IDs

If you're not sure of your product IDs, run this SQL:

```sql
SELECT product_id, product_name, image_url FROM products ORDER BY product_id;
```

This will show you all products and their current image URLs.

## Adding Images for New Products

When you add a new product in the future:

1. Add the image to `/static/images/products/`
2. Note the product_id from the products page
3. Run:
   ```sql
   UPDATE products 
   SET image_url = '/static/images/products/YOUR_IMAGE.jpg' 
   WHERE product_id = X;
   ```

## Troubleshooting

**Images not showing?**
- Check the file exists in `sepik_fresh/static/images/products/`
- Check the filename matches exactly (case-sensitive on Linux)
- Check the image_url in database is correct
- Try accessing directly: `http://localhost:5000/static/images/products/chicken.jpg`

**Wrong image showing?**
- Check product_id in SQL command
- Verify image_url in database: `SELECT product_id, product_name, image_url FROM products;`

## That's It!

No upload functionality needed - just:
1. Add images to folder
2. Update database with paths
3. Refresh browser

Simple and straightforward! 🎉

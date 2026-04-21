# Quick Setup Guide: Product Images & Slideshow

## Step 1: Database Migration

Run this SQL command in phpMyAdmin or MySQL command line:

```sql
ALTER TABLE products 
ADD COLUMN IF NOT EXISTS image_url VARCHAR(500) DEFAULT NULL 
AFTER description;
```

Or use the migration file:
```bash
cd sepik_fresh/database
mysql -u root -p sepik_database < add_product_images_column.sql
```

## Step 2: Verify Folder Permissions

Ensure the products images folder exists and is writable:

```bash
# Linux/Mac
mkdir -p sepik_fresh/static/images/products
chmod 755 sepik_fresh/static/images/products

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path sepik_fresh/static/images/products
```

## Step 3: Test the Features

### Test Image Upload (Admin):
1. Start the application: `python sepik_fresh/app.py`
2. Log in as admin (email: ishojonduo@gmail.com, password: Pass@2026!)
3. Go to Products page
4. Click "Add Image" on any product
5. Select an image file
6. Verify image appears on the product card

### Test Slideshow (Public):
1. Go to home page: http://localhost:5000/
2. Scroll down to "Featured Products" section
3. Verify slideshow displays products
4. Test arrow navigation
5. Test dot navigation
6. Verify auto-advance works (5 seconds)

### Test Order Form (Customer):
1. Log in as a customer or register new account
2. Go to "Place Order" page
3. Verify product images display in the order form
4. Verify you can see product details clearly

## Step 4: Add Sample Product Images

For testing, you can add sample images:

1. Download free stock images of chicken and eggs from:
   - Unsplash.com
   - Pexels.com
   - Pixabay.com

2. Upload via admin interface:
   - Log in as admin
   - Go to Products page
   - Click "Add Image" for each product
   - Select downloaded images

3. Or manually add to database:
```sql
-- Example: Add image URL for product ID 2
UPDATE products 
SET image_url = '/static/images/products/chicken.jpg' 
WHERE product_id = 2;
```

## Step 5: Verify Everything Works

### Checklist:
- [ ] Database column added successfully
- [ ] Products folder exists and is writable
- [ ] Admin can upload images
- [ ] Images display on products page
- [ ] Images display on order form
- [ ] Slideshow works on home page
- [ ] Slideshow auto-advances
- [ ] Navigation arrows work
- [ ] Dot indicators work
- [ ] Mobile responsive design works

## Troubleshooting

### "No such column: image_url"
- Run the database migration SQL again
- Verify you're connected to the correct database
- Check if column exists: `DESCRIBE products;`

### "Permission denied" when uploading
- Check folder permissions: `ls -la sepik_fresh/static/images/`
- Make folder writable: `chmod 755 sepik_fresh/static/images/products`
- On Windows, check folder properties and security settings

### Images not displaying
- Check if file was uploaded: `ls sepik_fresh/static/images/products/`
- Verify image_url in database: `SELECT product_id, product_name, image_url FROM products;`
- Check browser console for 404 errors
- Verify Flask is serving static files correctly

### Slideshow not working
- Check browser console for JavaScript errors
- Verify products exist: `SELECT COUNT(*) FROM products WHERE is_available=1;`
- Clear browser cache and reload
- Check if CSS is loading: View page source and verify CSS links

## Quick Commands Reference

### Start Application:
```bash
cd sepik_fresh
python app.py
```

### Check Database:
```bash
mysql -u root -p sepik_database
```

```sql
-- View products with images
SELECT product_id, product_name, image_url FROM products;

-- Count products with images
SELECT COUNT(*) FROM products WHERE image_url IS NOT NULL;

-- View all products
SELECT * FROM products;
```

### Check Uploaded Files:
```bash
# Linux/Mac
ls -lh sepik_fresh/static/images/products/

# Windows
dir sepik_fresh\static\images\products\
```

## Default Admin Credentials

For testing:
- **Email:** ishojonduo@gmail.com
- **Password:** Pass@2026!

## Need Help?

1. Check `PRODUCT_IMAGES_FEATURE.md` for detailed documentation
2. Review code comments in `app.py` and templates
3. Check server logs for error messages
4. Verify all files were updated correctly

## Success Indicators

You'll know everything is working when:
1. ✅ Admin can upload images without errors
2. ✅ Product cards show images instead of placeholders
3. ✅ Order form displays product images
4. ✅ Home page slideshow cycles through products
5. ✅ All navigation controls work smoothly
6. ✅ Mobile view is responsive and functional

---

**Setup Time:** ~5-10 minutes  
**Difficulty:** Easy  
**Requirements:** MySQL/MariaDB, Python 3.7+, Flask

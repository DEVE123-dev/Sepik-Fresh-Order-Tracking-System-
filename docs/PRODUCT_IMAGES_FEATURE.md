# Product Images & Slideshow Feature

## Overview
This document describes the new product image management and home page slideshow features added to Sepik Fresh.

## Features Added

### 1. Product Image Upload (Admin)
Administrators can now upload images for each product directly from the Products page.

**How to Use:**
1. Log in as an admin user
2. Navigate to the Products page (`/products`)
3. Find the product card you want to add an image to
4. Click the "Add Image" or "Update Image" button
5. Select an image file (PNG, JPG, JPEG, GIF, or WEBP)
6. The image uploads automatically and displays immediately

**Technical Details:**
- Images are stored in `/static/images/products/`
- Each image gets a unique filename: `product_{id}_{random}.{ext}`
- Supported formats: PNG, JPG, JPEG, GIF, WEBP
- Maximum recommended size: 2MB
- Database field: `products.image_url` (VARCHAR 500)

### 2. Product Image Display
Product images are displayed in multiple locations:

**Products Page:**
- Shows product image at the top of each product card
- Falls back to icon placeholder if no image is uploaded
- Images have hover effects for better UX

**Order Placement Page:**
- Customers see product images when placing orders
- Helps customers identify products visually
- Improves ordering experience

**Home Page Slideshow:**
- Featured products with images appear in an automatic slideshow
- Shows up to 6 products
- Auto-advances every 5 seconds
- Manual navigation with arrows and dots
- Responsive design for mobile devices

### 3. Home Page Product Slideshow
An attractive slideshow showcasing featured products on the home page.

**Features:**
- Automatic slide transitions (5 seconds)
- Manual navigation (left/right arrows)
- Dot indicators for quick navigation
- Displays product image, name, description, price, and stock status
- "Order Now" button links to login page
- Fully responsive design

**Slideshow Controls:**
- **Auto-play:** Slides change automatically every 5 seconds
- **Arrow Navigation:** Click left/right arrows to navigate
- **Dot Navigation:** Click dots to jump to specific slides
- **Pause on Interaction:** Auto-play pauses when user interacts

## Database Changes

### Migration Required
Run the following SQL to add the image_url column:

```sql
ALTER TABLE products 
ADD COLUMN IF NOT EXISTS image_url VARCHAR(500) DEFAULT NULL 
AFTER description;
```

Or run the migration file:
```bash
mysql -u your_user -p sepik_database < database/add_product_images_column.sql
```

### Updated Schema
```sql
CREATE TABLE products (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(200) NOT NULL,
  product_category ENUM('poultry','eggs') NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  description TEXT,
  image_url VARCHAR(500) DEFAULT NULL,  -- NEW COLUMN
  is_available TINYINT(1) DEFAULT 1,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## File Changes

### Backend (Python)
**app.py:**
- Added `/admin/product/<pid>/image` route for image upload
- Updated `/` route to pass featured products to home page
- Added image handling with werkzeug secure_filename
- Added UUID for unique filenames

**models.py:**
- Already had `update_image()` method (no changes needed)
- `image_url` parameter in `create()` method

### Frontend (HTML)
**templates/products.html:**
- Added product image container
- Added image upload form for admins
- Added placeholder icons when no image exists

**templates/order_new.html:**
- Replaced table layout with grid of product cards
- Added product images to order form
- Improved visual presentation

**templates/home.html:**
- Added product slideshow section
- Added slideshow JavaScript for auto-play and navigation
- Added responsive design

### Styling (CSS)
**static/css/main.css:**
- Added `.product-slideshow-section` styles
- Added `.slide` animation styles
- Added `.slide-prev` and `.slide-next` button styles
- Added `.dot` navigation styles
- Added `.product-image-container` styles
- Added `.product-image-upload` styles
- Added responsive media queries

**static/css/dashboard.css:**
- Added `.order-products-grid` styles
- Added `.order-product-card` styles
- Added `.order-product-image` styles
- Added responsive grid layout

## Usage Examples

### Admin: Upload Product Image
```python
# Route: POST /admin/product/<pid>/image
# Form data: product_image (file)
# Returns: Redirect to products page with success message
```

### Customer: View Products with Images
```python
# Route: GET /products
# Returns: Product list with images displayed
```

### Public: View Slideshow
```python
# Route: GET / or GET /home
# Returns: Home page with featured products slideshow
```

## Image Best Practices

### Recommended Specifications:
- **Resolution:** 800x800 pixels or higher
- **Aspect Ratio:** Square (1:1) or landscape (4:3)
- **File Size:** Under 2MB for optimal loading
- **Format:** JPEG for photos, PNG for graphics with transparency
- **Quality:** High quality, well-lit, clear product shots

### Photography Tips:
1. Use natural lighting or soft artificial light
2. Plain white or neutral background
3. Show product from best angle
4. Fill the frame with the product
5. Keep focus sharp and clear
6. Avoid shadows and reflections

## Security Considerations

### File Upload Security:
- Only image file types allowed (PNG, JPG, JPEG, GIF, WEBP)
- Filenames are sanitized using `secure_filename()`
- Unique UUID added to prevent filename conflicts
- Files stored outside of user-accessible directories
- Admin-only access to upload functionality

### Access Control:
- Only admin users can upload images
- Login required for all image management
- Role-based access control enforced

## Troubleshooting

### Image Not Displaying
1. Check if file was uploaded successfully
2. Verify image_url in database is correct
3. Check file permissions on `/static/images/products/`
4. Verify image file exists in the folder
5. Check browser console for 404 errors

### Upload Fails
1. Check file size (should be under 2MB)
2. Verify file format is supported
3. Check folder permissions (should be writable)
4. Verify admin user is logged in
5. Check server logs for errors

### Slideshow Not Working
1. Check if products exist in database
2. Verify JavaScript is loading correctly
3. Check browser console for errors
4. Ensure featured_products is passed to template
5. Verify CSS is loading properly

## Future Enhancements

Potential improvements for future versions:
- Image cropping/resizing tool
- Multiple images per product
- Image gallery view
- Bulk image upload
- Image optimization/compression
- CDN integration for faster loading
- Image alt text management for SEO
- Drag-and-drop upload interface

## Testing Checklist

- [ ] Admin can upload product images
- [ ] Images display on products page
- [ ] Images display on order form
- [ ] Slideshow displays on home page
- [ ] Slideshow auto-advances
- [ ] Arrow navigation works
- [ ] Dot navigation works
- [ ] Responsive design works on mobile
- [ ] Placeholder icons show when no image
- [ ] File upload security works
- [ ] Database migration successful

## Support

For issues or questions about this feature:
1. Check this documentation first
2. Review the code comments in relevant files
3. Check server logs for errors
4. Verify database schema is up to date
5. Contact the development team

---

**Version:** 1.0  
**Date:** April 2026  
**Author:** Sepik Fresh Development Team

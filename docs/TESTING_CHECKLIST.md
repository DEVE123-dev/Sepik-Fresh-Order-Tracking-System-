# Product Images & Slideshow - Testing Checklist

## Pre-Testing Setup

### Database Setup
- [ ] Database migration completed successfully
- [ ] `image_url` column exists in products table
- [ ] Column type is VARCHAR(500)
- [ ] Column allows NULL values

### File System Setup
- [ ] `/static/images/products/` folder exists
- [ ] Folder has write permissions (755 on Linux/Mac)
- [ ] Folder is accessible via web browser

### Application Setup
- [ ] Application starts without errors
- [ ] No Python syntax errors
- [ ] All dependencies installed
- [ ] Static files serving correctly

---

## 1. Admin Image Upload Testing

### Basic Upload Functionality
- [ ] Admin can log in successfully
- [ ] Products page loads without errors
- [ ] "Add Image" button visible on product cards
- [ ] File input opens when button clicked
- [ ] Can select image file (PNG, JPG, JPEG, GIF, WEBP)
- [ ] Form submits automatically after file selection
- [ ] Success message or redirect occurs
- [ ] Image appears on product card immediately

### File Type Validation
- [ ] PNG files upload successfully
- [ ] JPG files upload successfully
- [ ] JPEG files upload successfully
- [ ] GIF files upload successfully
- [ ] WEBP files upload successfully
- [ ] Non-image files are rejected (e.g., .txt, .pdf)
- [ ] Appropriate error message shown for invalid files

### Security Testing
- [ ] Non-admin users cannot access upload route
- [ ] Customer users don't see "Add Image" button
- [ ] Delivery staff don't see "Add Image" button
- [ ] Direct POST to upload route requires admin login
- [ ] Filenames are sanitized (no directory traversal)
- [ ] Unique filenames generated (no conflicts)

### Edge Cases
- [ ] Upload works with very long filenames
- [ ] Upload works with special characters in filename
- [ ] Upload works with uppercase extensions (.JPG, .PNG)
- [ ] Multiple uploads to same product work correctly
- [ ] Upload works after page refresh
- [ ] Upload works in different browsers

---

## 2. Product Image Display Testing

### Products Page (Admin View)
- [ ] Images display correctly on product cards
- [ ] Image fits container properly (no distortion)
- [ ] Placeholder icon shows when no image
- [ ] Hover effects work on images
- [ ] "Update Image" button shows for products with images
- [ ] "Add Image" button shows for products without images
- [ ] Images load quickly (no long delays)

### Products Page (Customer View)
- [ ] Customers can see product images
- [ ] Images display in product cards
- [ ] No upload buttons visible to customers
- [ ] Placeholder icons show when no image
- [ ] Images help identify products

### Order Placement Page
- [ ] Product images display in order form
- [ ] Images show in grid layout
- [ ] Each product card has image or placeholder
- [ ] Images help customers make selections
- [ ] Layout is clean and organized
- [ ] Quantity inputs work correctly

### Dashboard (Customer)
- [ ] Featured products show images (if applicable)
- [ ] Images display correctly in any product widgets

---

## 3. Home Page Slideshow Testing

### Basic Slideshow Functionality
- [ ] Slideshow section appears on home page
- [ ] At least one slide displays
- [ ] First slide shows by default
- [ ] Slideshow auto-advances after 5 seconds
- [ ] Slides transition smoothly (fade animation)
- [ ] All product information displays correctly:
  - [ ] Product name
  - [ ] Product description
  - [ ] Product price
  - [ ] Stock status
  - [ ] Product image or placeholder

### Navigation Controls
- [ ] Left arrow button visible
- [ ] Right arrow button visible
- [ ] Left arrow goes to previous slide
- [ ] Right arrow goes to next slide
- [ ] Arrows work at first/last slide (loops)
- [ ] Dot indicators visible at bottom
- [ ] Correct number of dots (one per product)
- [ ] Active dot highlighted
- [ ] Clicking dot navigates to that slide
- [ ] Dot indicators update when slide changes

### Auto-Advance Behavior
- [ ] Slideshow auto-advances every 5 seconds
- [ ] Auto-advance pauses when user clicks arrow
- [ ] Auto-advance resumes after user interaction
- [ ] Auto-advance pauses when user clicks dot
- [ ] Timer resets after manual navigation

### Content Display
- [ ] Product images display correctly
- [ ] Placeholder icons show when no image
- [ ] Product names are readable
- [ ] Descriptions are readable
- [ ] Prices format correctly (K XX.XX)
- [ ] Stock status shows correctly:
  - [ ] "In Stock" for available products
  - [ ] "Out of Stock" for unavailable products
- [ ] "Order Now" button visible
- [ ] "Order Now" button links to login page

---

## 4. Responsive Design Testing

### Desktop (1920x1080)
- [ ] Slideshow displays full width
- [ ] Product cards in grid layout (3-4 columns)
- [ ] Images display at full size
- [ ] All text readable
- [ ] Navigation controls positioned correctly
- [ ] No horizontal scrolling

### Laptop (1366x768)
- [ ] Slideshow scales appropriately
- [ ] Product cards adjust to screen size
- [ ] Images scale proportionally
- [ ] Text remains readable
- [ ] Layout remains organized

### Tablet (768x1024)
- [ ] Slideshow switches to single column
- [ ] Product cards stack vertically
- [ ] Images resize appropriately
- [ ] Touch navigation works
- [ ] Arrows remain accessible
- [ ] Dots remain visible

### Mobile (375x667)
- [ ] Slideshow fully responsive
- [ ] Single column layout
- [ ] Images fit screen width
- [ ] Text remains readable (no tiny fonts)
- [ ] Buttons are touch-friendly (min 44px)
- [ ] Navigation arrows accessible
- [ ] Dots visible and tappable
- [ ] No horizontal scrolling
- [ ] Vertical scrolling smooth

---

## 5. Performance Testing

### Load Times
- [ ] Home page loads in under 3 seconds
- [ ] Products page loads in under 3 seconds
- [ ] Order page loads in under 3 seconds
- [ ] Images load progressively (no blocking)
- [ ] Slideshow initializes quickly

### Image Optimization
- [ ] Images under 2MB load acceptably
- [ ] Multiple images don't slow page significantly
- [ ] Lazy loading works (if implemented)
- [ ] No memory leaks in slideshow

### Browser Performance
- [ ] Slideshow doesn't cause lag
- [ ] Animations are smooth (60fps)
- [ ] No console errors
- [ ] No JavaScript errors
- [ ] CPU usage remains reasonable

---

## 6. Cross-Browser Testing

### Chrome/Edge (Chromium)
- [ ] All features work correctly
- [ ] Images display properly
- [ ] Slideshow functions correctly
- [ ] Upload works
- [ ] Animations smooth

### Firefox
- [ ] All features work correctly
- [ ] Images display properly
- [ ] Slideshow functions correctly
- [ ] Upload works
- [ ] Animations smooth

### Safari (if available)
- [ ] All features work correctly
- [ ] Images display properly
- [ ] Slideshow functions correctly
- [ ] Upload works
- [ ] Animations smooth

### Mobile Browsers
- [ ] Chrome Mobile works correctly
- [ ] Safari Mobile works correctly
- [ ] Touch interactions work
- [ ] Responsive design works

---

## 7. Database Testing

### Data Integrity
- [ ] image_url saves correctly after upload
- [ ] image_url format is correct (/static/images/products/...)
- [ ] NULL values handled correctly (no image)
- [ ] Updates don't affect other columns
- [ ] Multiple products can have images

### Query Performance
- [ ] Product queries remain fast with image_url
- [ ] Filtering works correctly
- [ ] Sorting works correctly
- [ ] Search includes products with/without images

---

## 8. Error Handling Testing

### Upload Errors
- [ ] Appropriate error for invalid file type
- [ ] Appropriate error for missing file
- [ ] Appropriate error for permission denied
- [ ] Appropriate error for disk full (if testable)
- [ ] Error messages are user-friendly
- [ ] Errors don't crash application

### Display Errors
- [ ] Missing image files handled gracefully
- [ ] Broken image URLs show placeholder
- [ ] Invalid image_url doesn't break page
- [ ] Empty slideshow handled (no products)

### Network Errors
- [ ] Slow network doesn't break slideshow
- [ ] Failed image loads show placeholder
- [ ] Timeout handled gracefully

---

## 9. Accessibility Testing

### Keyboard Navigation
- [ ] Can tab to upload button
- [ ] Can activate upload with Enter/Space
- [ ] Can navigate slideshow with keyboard
- [ ] Focus indicators visible

### Screen Reader
- [ ] Images have alt text (if implemented)
- [ ] Buttons have labels
- [ ] Slideshow announces changes (if implemented)
- [ ] Form inputs have labels

### Visual
- [ ] Sufficient color contrast
- [ ] Text readable at all sizes
- [ ] Icons have text alternatives
- [ ] No information conveyed by color alone

---

## 10. Integration Testing

### Full User Flows
- [ ] Admin uploads image → Customer sees it in products
- [ ] Admin uploads image → Customer sees it in order form
- [ ] Admin uploads image → Public sees it in slideshow
- [ ] Customer orders product → Image shows in order history
- [ ] Admin updates image → New image displays everywhere

### Multi-User Testing
- [ ] Multiple admins can upload simultaneously
- [ ] Customers see updates in real-time (after refresh)
- [ ] No conflicts between concurrent uploads

---

## 11. Regression Testing

### Existing Features Still Work
- [ ] Product creation works
- [ ] Product editing works
- [ ] Product deletion works
- [ ] Stock management works
- [ ] Price updates work
- [ ] Order placement works
- [ ] Order tracking works
- [ ] User management works
- [ ] Authentication works
- [ ] All existing pages load

### No Breaking Changes
- [ ] Products without images still work
- [ ] Old database records compatible
- [ ] Existing orders unaffected
- [ ] User accounts unaffected

---

## 12. Documentation Testing

### Documentation Accuracy
- [ ] PRODUCT_IMAGES_FEATURE.md is accurate
- [ ] SETUP_PRODUCT_IMAGES.md steps work
- [ ] QUICK_START_IMAGES.txt is correct
- [ ] Code comments are accurate
- [ ] README files are helpful

### Documentation Completeness
- [ ] All features documented
- [ ] All routes documented
- [ ] All files explained
- [ ] Troubleshooting covers common issues

---

## Test Results Summary

### Pass/Fail Counts
- Total Tests: _____ / _____
- Passed: _____
- Failed: _____
- Skipped: _____

### Critical Issues Found
1. _____________________________________
2. _____________________________________
3. _____________________________________

### Minor Issues Found
1. _____________________________________
2. _____________________________________
3. _____________________________________

### Recommendations
1. _____________________________________
2. _____________________________________
3. _____________________________________

---

## Sign-Off

### Tested By
- Name: _____________________________________
- Date: _____________________________________
- Environment: _____________________________________

### Approved By
- Name: _____________________________________
- Date: _____________________________________
- Signature: _____________________________________

---

**Testing Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Complete | ⬜ Approved

**Production Ready:** ⬜ Yes | ⬜ No | ⬜ With Conditions

**Notes:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

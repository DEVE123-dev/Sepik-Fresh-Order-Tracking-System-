# User Stories
## Sepik Fresh Tracking System
## Agile Format with Acceptance Criteria

---

## User Story Format

**Standard Format:** "As a [role], I want [feature], so that [benefit]."

**Components:**
- **Story ID:** Unique identifier
- **User Story:** Description in standard format
- **Priority:** MoSCoW (Must Have, Should Have, Could Have, Won't Have)
- **Story Points:** Effort estimate (1-13 Fibonacci scale)
- **Acceptance Criteria:** Minimum 2 testable conditions
- **Sprint:** Assigned sprint number
- **Status:** Not Started, In Progress, Completed

---

## Sprint 1: Foundation Features (Must Have)

### US-001: User Registration
**As a** new customer  
**I want** to create an account with my personal details  
**So that** I can place orders and track my deliveries

**Priority:** Must Have  
**Story Points:** 5  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. User can register with first name, last name, email, phone, address, and password
2. Password must be at least 6 characters long
3. Email must be unique in the system
4. Password confirmation must match the original password
5. User is automatically assigned 'customer' role
6. Success message is displayed after registration
7. User can immediately login after registration

**Technical Notes:**
- Password hashed with bcrypt (cost factor 12)
- Customer number auto-generated (SF-CUST-XXXXX format)
- Email validation performed

---

### US-002: User Login
**As a** registered user  
**I want** to login with my email and password  
**So that** I can access my account and use the system

**Priority:** Must Have  
**Story Points:** 3  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. User can login with valid email and password
2. Invalid credentials show error message
3. Session is created upon successful login
4. User is redirected to role-appropriate dashboard
5. Session expires after 30 minutes of inactivity
6. User can logout at any time

**Technical Notes:**
- Bcrypt password verification
- Session-based authentication
- Role-based dashboard routing

---

### US-003: Browse Products
**As a** customer  
**I want** to view all available products with prices and stock  
**So that** I can decide what to order

**Priority:** Must Have  
**Story Points:** 3  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customer can view all available products
2. Each product displays name, category, price, stock quantity, and description
3. Only products marked as "available" are shown to customers
4. Products are displayed in alphabetical order
5. Search functionality allows filtering by product name or description
6. Pagination displays 20 products per page

**Technical Notes:**
- Products filtered by is_available=1
- Search uses LIKE query on name and description
- Pagination implemented with offset/limit

---

### US-004: Place Order
**As a** customer  
**I want** to select multiple products with quantities and place an order  
**So that** I can purchase fresh produce for delivery

**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customer can select multiple products with quantities
2. Total amount is calculated automatically
3. Order is created with "pending" status
4. Stock is deducted for ordered items
5. Order confirmation email is sent to customer
6. Customer is redirected to order tracking page
7. System prevents ordering out-of-stock items

**Technical Notes:**
- Order items stored in order_items table
- Stock deduction atomic with order creation
- Email notification via email_utils.py

---

### US-005: Track Order
**As a** customer  
**I want** to view my order status with a visual timeline  
**So that** I know when my delivery will arrive

**Priority:** Must Have  
**Story Points:** 5  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customer can view order details (items, quantities, prices, total)
2. Visual timeline shows current order status
3. Timeline includes: Pending → Confirmed → Processing → Out for Delivery → Delivered
4. Current status is highlighted
5. Customer details (name, phone, address) are displayed
6. Order date and estimated delivery time are shown

**Technical Notes:**
- Visual timeline implemented with CSS
- Status progression tracked in orders table
- Customer info joined from users table

---

### US-006: Admin Product Management
**As an** administrator  
**I want** to add, edit, and delete products  
**So that** I can manage the product catalog

**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Admin can add new products with name, category, price, stock, and description
2. Admin can update product price inline
3. Admin can update stock quantity inline
4. Admin can enable/disable products
5. Admin can delete products (or disable if they have orders)
6. All products (available and unavailable) are visible to admin
7. Changes are reflected immediately

**Technical Notes:**
- Smart deletion: disable if has orders, delete if no orders
- Inline updates via POST requests
- Admin-only access via login_required('admin')

---

### US-007: Admin Order Management
**As an** administrator  
**I want** to view all orders and update their status  
**So that** I can manage the order fulfillment process

**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Admin can view all orders with customer details
2. Admin can search orders by order ID, customer name, or email
3. Admin can filter orders by status
4. Admin can update order status
5. Customer receives email notification when status changes
6. Orders are sorted by most recent first
7. Pagination displays 20 orders per page

**Technical Notes:**
- Search uses LIKE query on multiple fields
- Status update triggers email notification
- Join with users table for customer details

---

### US-008: Role-Based Dashboards
**As a** user  
**I want** to see a dashboard appropriate for my role  
**So that** I can quickly access relevant features

**Priority:** Must Have  
**Story Points:** 5  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customers see: recent orders, order statistics, featured products
2. Admin sees: system statistics, recent orders, quick actions
3. Staff sees: active deliveries count, delivery list
4. Dashboard displays user's name
5. Navigation menu shows role-appropriate links
6. Unauthorized users cannot access other role dashboards

**Technical Notes:**
- Role stored in session
- Dashboard routing based on session['role']
- login_required decorator enforces access control

---

### US-009: Contact Form
**As a** visitor or customer  
**I want** to send a message to Sepik Fresh  
**So that** I can ask questions or provide feedback

**Priority:** Should Have  
**Story Points:** 3  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Anyone can access the contact form
2. Form requires name, email, and message
3. Message is saved to database
4. Success message is displayed after submission
5. Admin can view messages in admin inbox
6. Form validation prevents empty submissions

**Technical Notes:**
- Messages stored in contact_messages table
- No authentication required for submission
- Admin inbox added in Phase 3

---

### US-010: Staff Delivery Management
**As a** delivery staff member  
**I want** to view active deliveries and update their status  
**So that** I can manage my delivery route efficiently

**Priority:** Must Have  
**Story Points:** 5  
**Sprint:** Sprint 1  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Staff can view all active deliveries (not delivered or cancelled)
2. Each delivery shows customer name, address, phone, and order details
3. Staff can update status to "out for delivery" or "delivered"
4. Customer receives email notification when status changes
5. Dashboard shows count of active deliveries
6. Interface is mobile-friendly for field use

**Technical Notes:**
- Active orders: status NOT IN ('delivered', 'cancelled')
- Status update via POST request
- Mobile-responsive CSS

---

## Sprint 2: Critical Features (Should Have)

### US-011: Password Reset
**As a** user who forgot their password  
**I want** to reset my password via email  
**So that** I can regain access to my account

**Priority:** Should Have  
**Story Points:** 8  
**Sprint:** Sprint 2  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. User can request password reset by entering email
2. System generates secure reset token (1-hour expiration)
3. Reset link is sent via email
4. User can set new password using valid token
5. Expired tokens are rejected with error message
6. Token is marked as used after successful reset
7. User can login with new password immediately

**Technical Notes:**
- Token stored in password_reset_tokens table
- Token generated with secrets.token_urlsafe(32)
- Email sent via email_utils.py

---

### US-012: Email Notifications
**As a** customer  
**I want** to receive email notifications for important events  
**So that** I stay informed about my orders

**Priority:** Should Have  
**Story Points:** 8  
**Sprint:** Sprint 2  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customer receives email when order is placed
2. Customer receives email when order status changes
3. Customer receives email when password is reset
4. Customer receives email when profile is updated
5. Customer receives email when order is cancelled
6. Emails are logged to database
7. System works without SMTP (logs to terminal)

**Technical Notes:**
- Email functions in email_utils.py
- Emails logged to email_notifications table
- Fallback to terminal logging if SMTP not configured

---

### US-013: Profile Management
**As a** user  
**I want** to view and edit my profile information  
**So that** I can keep my details up to date

**Priority:** Should Have  
**Story Points:** 5  
**Sprint:** Sprint 2  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. User can view their profile (name, email, phone, address, role)
2. User can edit first name, last name, phone, and address
3. User can change their password
4. Current password must be verified before changing
5. New password must be at least 6 characters
6. Email notification is sent after profile update
7. Session name is updated after profile change

**Technical Notes:**
- Profile update via profile_edit route
- Password change requires current password verification
- Email notification via send_profile_update_notification

---

### US-014: Order Cancellation
**As a** customer  
**I want** to cancel my order if it hasn't been delivered  
**So that** I can change my mind or correct mistakes

**Priority:** Should Have  
**Story Points:** 5  
**Sprint:** Sprint 2  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Customer can cancel orders with status "pending" or "confirmed"
2. Customer cannot cancel orders that are "out for delivery" or "delivered"
3. Stock is automatically restored for cancelled items
4. Cancellation reason can be provided (optional)
5. Order status changes to "cancelled"
6. Email notification is sent to customer
7. Cancellation timestamp is recorded

**Technical Notes:**
- Stock restoration via UPDATE products query
- Cancellation reason stored in orders table
- cancelled_at timestamp recorded

---

## Sprint 3: Advanced Features (Could Have)

### US-015: Pagination
**As a** user viewing large lists  
**I want** to see items split across multiple pages  
**So that** pages load quickly and are easy to navigate

**Priority:** Could Have  
**Story Points:** 5  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Products page shows 20 items per page
2. Orders page shows 20 items per page
3. Admin inbox shows 20 messages per page
4. Previous/Next navigation buttons are displayed
5. Page counter shows "Page X of Y"
6. Search and filter parameters are maintained across pages
7. Pagination only shows when more than 20 items exist

**Technical Notes:**
- Implemented with LIMIT and OFFSET in SQL
- Page parameter in URL query string
- Total pages calculated from total count

---

### US-016: Admin Inbox
**As an** administrator  
**I want** to view and manage contact form submissions  
**So that** I can respond to customer inquiries

**Priority:** Could Have  
**Story Points:** 5  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Admin can view all contact messages
2. Unread message count is displayed on dashboard
3. Admin can filter to show only unread messages
4. Messages are automatically marked as read when viewed
5. Admin can delete messages
6. Admin can reply via email link
7. Messages are paginated (20 per page)

**Technical Notes:**
- Messages stored in contact_messages table
- Unread count via COUNT query with is_read=0
- Mark as read on view

---

### US-017: CSV Export
**As an** administrator  
**I want** to export data to CSV files  
**So that** I can analyze data in external tools

**Priority:** Could Have  
**Story Points:** 5  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Admin can export all orders to CSV
2. Admin can export all products to CSV
3. Admin can export all users to CSV
4. CSV files have descriptive headers
5. Filenames include timestamp
6. Export includes all relevant fields
7. One-click download

**Technical Notes:**
- CSV generation using Python csv module
- Response with text/csv mimetype
- Timestamped filenames (YYYYMMDD_HHMMSS)

---

### US-018: Advanced Filtering
**As an** administrator  
**I want** to filter orders by multiple criteria  
**So that** I can find specific orders quickly

**Priority:** Could Have  
**Story Points:** 5  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Admin can search by order ID, customer name, or email
2. Admin can filter by order status
3. Admin can filter by date range (from/to)
4. Multiple filters can be combined
5. Clear filters button resets all filters
6. Filters are maintained across pagination
7. Results update immediately after filtering

**Technical Notes:**
- Dynamic WHERE clause construction
- Date filtering with DATE() function
- Filter parameters in URL query string

---

### US-019: Product Search
**As a** customer  
**I want** to search for products by name or description  
**So that** I can quickly find what I need

**Priority:** Could Have  
**Story Points:** 3  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. Search box is prominently displayed on products page
2. Search matches product name or description
3. Search is case-insensitive
4. Results are displayed immediately
5. Search query is preserved in search box
6. Clear search returns to all products
7. Search works with pagination

**Technical Notes:**
- LIKE query with % wildcards
- Search parameter in URL query string
- Pagination maintains search query

---

### US-020: Background Monitoring
**As an** administrator  
**I want** the system to automatically monitor for issues  
**So that** I can proactively address problems

**Priority:** Could Have  
**Story Points:** 8  
**Sprint:** Sprint 3  
**Status:** ✅ Completed

**Acceptance Criteria:**
1. System monitors for low stock products
2. System monitors for overdue deliveries
3. System logs new orders immediately
4. Alerts are stored in database
5. Admin can view alerts on alerts page
6. Admin can clear alerts
7. Background agents run automatically

**Technical Notes:**
- Background agents in agents.py
- Agents run in separate threads
- Alerts stored in agent_notifications table

---

## User Story Summary

### By Priority (MoSCoW)

| Priority | Count | Story Points | Status |
|----------|-------|--------------|--------|
| **Must Have** | 10 | 53 | ✅ 100% Complete |
| **Should Have** | 4 | 26 | ✅ 100% Complete |
| **Could Have** | 6 | 31 | ✅ 100% Complete |
| **Won't Have** | 0 | 0 | N/A |
| **TOTAL** | **20** | **110** | ✅ **100% Complete** |

### By Sprint

| Sprint | Story Count | Story Points | Status |
|--------|-------------|--------------|--------|
| **Sprint 1** | 10 | 53 | ✅ Complete |
| **Sprint 2** | 4 | 26 | ✅ Complete |
| **Sprint 3** | 6 | 31 | ✅ Complete |
| **TOTAL** | **20** | **110** | ✅ **Complete** |

### By User Role

| Role | Story Count | Key Features |
|------|-------------|--------------|
| **Customer** | 9 | Registration, login, browse, order, track, cancel, profile, search, contact |
| **Administrator** | 8 | Product management, order management, user management, inbox, export, filtering, alerts |
| **Delivery Staff** | 2 | View deliveries, update status |
| **System** | 1 | Background monitoring |

---

## Requirements Traceability Matrix

| User Story | Functional Requirement | Implementation | Test Status |
|------------|------------------------|----------------|-------------|
| US-001 | FR-001: User registration | register route, User.create() | ✅ Tested |
| US-002 | FR-002: User authentication | login route, bcrypt verification | ✅ Tested |
| US-003 | FR-003: Product catalog | products route, Product.get_available() | ✅ Tested |
| US-004 | FR-004: Order placement | order_new route, Order.create() | ✅ Tested |
| US-005 | FR-005: Order tracking | track_order route, Order.get_by_id() | ✅ Tested |
| US-006 | FR-006: Product management | admin routes, Product CRUD | ✅ Tested |
| US-007 | FR-007: Order management | admin_orders route, Order.update_status() | ✅ Tested |
| US-008 | FR-008: Role-based access | dashboard route, login_required() | ✅ Tested |
| US-009 | FR-009: Contact form | contact route, ContactMessage | ✅ Tested |
| US-010 | FR-010: Delivery management | staff_deliveries route | ✅ Tested |
| US-011 | FR-011: Password reset | forgot_password, reset_password routes | ✅ Tested |
| US-012 | FR-012: Email notifications | email_utils.py functions | ✅ Tested |
| US-013 | FR-013: Profile management | profile_edit route, User.update_profile() | ✅ Tested |
| US-014 | FR-014: Order cancellation | cancel_order route, Order.cancel_order() | ✅ Tested |
| US-015 | FR-015: Pagination | get_paginated() methods | ✅ Tested |
| US-016 | FR-016: Admin inbox | admin_inbox routes, ContactMessage | ✅ Tested |
| US-017 | FR-017: CSV export | export routes, csv module | ✅ Tested |
| US-018 | FR-018: Advanced filtering | admin_orders with filters | ✅ Tested |
| US-019 | FR-019: Product search | products route with search | ✅ Tested |
| US-020 | FR-020: Background monitoring | agents.py, agent threads | ✅ Tested |

---

## Conclusion

All 20 user stories have been successfully implemented and tested, covering the complete functionality of the Sepik Fresh Tracking System. The stories span three sprints and address the needs of all stakeholder groups (customers, administrators, and delivery staff).

**Key Achievements:**
- ✅ 100% story completion rate
- ✅ 110 story points delivered
- ✅ All acceptance criteria met
- ✅ Full requirements traceability
- ✅ Comprehensive test coverage

The user stories demonstrate a clear progression from foundational features (Sprint 1) through critical enhancements (Sprint 2) to advanced capabilities (Sprint 3), resulting in a production-ready system that exceeds initial requirements.

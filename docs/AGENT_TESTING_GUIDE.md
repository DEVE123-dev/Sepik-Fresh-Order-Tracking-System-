# 🤖 Agent Testing Guide

## Overview

Your Sepik Fresh system has **3 background agents** that monitor the system automatically:

1. **OrderStatusAgent** - Monitors order status changes
2. **StockAlertAgent** - Alerts when stock is low
3. **DeliveryCheckAgent** - Flags overdue deliveries

---

## ✅ Agents Are Working If:

When you start the application with `py app.py`, you should see:

```
[Agent] OrderStatusAgent started.
[Agent] StockAlertAgent started.
[Agent] DeliveryCheckAgent started.
[Agents] All agents running.
 * Running on http://127.0.0.1:5000
```

---

## 🧪 How to Test Each Agent

### **Test 1: OrderStatusAgent**

**What it does:** Detects when an order status changes

**How to test:**
1. Login as admin
2. Go to "Orders" page
3. Find any order
4. Change its status (e.g., from "pending" to "confirmed")
5. Go to "Alerts" page
6. You should see: "Order #X changed from 'pending' to 'confirmed'"

**Check interval:** Every 30 seconds

---

### **Test 2: StockAlertAgent**

**What it does:** Alerts when product stock falls below 10 units

**How to test:**
1. Login as admin
2. Go to "Products" page
3. Find a product with stock > 10
4. Edit stock to 5 (below threshold)
5. Wait 60 seconds
6. Go to "Alerts" page
7. You should see: "LOW STOCK: [Product Name] has only 5 units left"

**To test restock alert:**
1. Edit the same product stock back to 20
2. Wait 60 seconds
3. Check "Alerts" page
4. You should see: "RESTOCKED: [Product Name] is back to 20 units"

**Check interval:** Every 60 seconds

---

### **Test 3: DeliveryCheckAgent**

**What it does:** Flags orders that are past their delivery time

**How to test:**
1. Login as admin
2. Go to "Orders" page
3. Find an order with status "out_for_delivery"
4. Note its estimated delivery time
5. If the delivery time has passed, wait 60 seconds
6. Go to "Alerts" page
7. You should see: "OVERDUE: Order #X is Y minutes past its ETA"

**Alternative test (create overdue order):**
1. Create a new order as customer
2. As admin, set estimated delivery time to 1 hour ago
3. Set status to "out_for_delivery"
4. Wait 60 seconds
5. Check "Alerts" page

**Check interval:** Every 60 seconds

---

### **Test 4: NewOrderAlert**

**What it does:** Instantly alerts when a new order is placed

**How to test:**
1. Logout if logged in
2. Login as "basic" / "Pass@2026!" (customer)
3. Go to "New Order" page
4. Select products and place order
5. Logout and login as admin
6. Go to "Alerts" page
7. You should see: "NEW ORDER PLACED: Order #X by [Customer Name]"

**This alert is instant** - no waiting required!

---

## 📊 Viewing Agent Alerts

### **Method 1: Alerts Page (Recommended)**
1. Login as admin
2. Click "Alerts" in sidebar
3. View all agent notifications
4. Most recent alerts appear at the top

### **Method 2: Database (phpMyAdmin)**
1. Open http://localhost/phpmyadmin
2. Select `sepik_database`
3. Click `agent_notifications` table
4. Click "Browse"
5. View all logged alerts

### **Method 3: Terminal/Console**
Agents also print to the console where you ran `py app.py`:
```
[OrderStatusAgent] 2026-04-21 10:30:15 — Order #1 changed from 'pending' to 'confirmed'
[StockAlertAgent] 2026-04-21 10:31:20 — LOW STOCK: 'Fresh Eggs' has only 5 units left
```

---

## 🔧 Agent Configuration

### **Check Intervals (in agents.py):**
```python
ORDER_CHECK_INTERVAL   = 30   # 30 seconds
STOCK_CHECK_INTERVAL   = 60   # 60 seconds
DELIVERY_CHECK_INTERVAL = 60  # 60 seconds
```

### **Stock Threshold:**
```python
STOCK_THRESHOLD = 10  # Alert when stock < 10
```

**To change these:** Edit `sepik_fresh/agents.py` and restart the application.

---

## ✅ Verification Checklist

- [ ] Application starts with agent messages in console
- [ ] OrderStatusAgent detects status changes
- [ ] StockAlertAgent detects low stock
- [ ] DeliveryCheckAgent detects overdue orders
- [ ] NewOrderAlert triggers on new orders
- [ ] Alerts appear in "Alerts" page
- [ ] Alerts are saved to database
- [ ] Alerts print to console

---

## 🐛 Troubleshooting

### **Problem: No agent messages in console**
**Solution:** 
- Check if `start_agents()` is called in app.py
- Restart the application
- Check for errors in console

### **Problem: Agents not detecting changes**
**Solution:**
- Wait for the check interval (30-60 seconds)
- Verify database connection is working
- Check console for agent error messages

### **Problem: Alerts not appearing in Alerts page**
**Solution:**
- Check if `agent_notifications` table exists
- Verify database permissions
- Check console for database errors

### **Problem: "Alerts" page shows no data**
**Solution:**
- Trigger an event (change order status, lower stock, etc.)
- Wait for agent check interval
- Refresh the Alerts page

---

## 📝 Quick Test Script

Run this complete test:

1. **Start application:**
   ```powershell
   py app.py
   ```
   ✅ Check: See agent startup messages

2. **Test NewOrderAlert:**
   - Login as basic user
   - Place an order
   - Login as admin
   - Check Alerts page
   ✅ Check: See "NEW ORDER PLACED" alert

3. **Test OrderStatusAgent:**
   - Go to Orders page
   - Change an order status
   - Wait 30 seconds
   - Check Alerts page
   ✅ Check: See status change alert

4. **Test StockAlertAgent:**
   - Go to Products page
   - Set a product stock to 5
   - Wait 60 seconds
   - Check Alerts page
   ✅ Check: See "LOW STOCK" alert

5. **Test DeliveryCheckAgent:**
   - Create order with past delivery time
   - Set status to "out_for_delivery"
   - Wait 60 seconds
   - Check Alerts page
   ✅ Check: See "OVERDUE" alert

---

## 🎯 Expected Behavior

### **Console Output:**
```
[Agent] OrderStatusAgent started.
[Agent] StockAlertAgent started.
[Agent] DeliveryCheckAgent started.
[Agents] All agents running.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000

[NewOrderAlert] 2026-04-21 10:25:30 — NEW ORDER PLACED: Order #5 by Basic User
[OrderStatusAgent] 2026-04-21 10:26:00 — Order #5 changed from 'pending' to 'confirmed'
[StockAlertAgent] 2026-04-21 10:27:00 — LOW STOCK: 'Fresh Eggs (Dozen)' has only 5 units left
```

### **Alerts Page:**
Shows a table with:
- Agent name
- Message
- Timestamp
- Read status

### **Database:**
`agent_notifications` table contains:
- id
- agent_name
- message
- is_read
- created_at

---

## 🎉 Success Criteria

Your agents are working correctly if:

✅ All 3 agents start when application launches  
✅ Agents detect events within their check intervals  
✅ Alerts appear in the Alerts page  
✅ Alerts are saved to database  
✅ Console shows agent activity  
✅ No errors in console  

---

## 📚 Additional Information

**Agent Architecture:**
- Agents run as daemon threads
- They stop automatically when app stops
- Each agent has its own check interval
- Agents are independent of each other

**Performance:**
- Agents use minimal resources
- Database queries are optimized
- No impact on main application performance

**Scalability:**
- Easy to add new agents
- Check intervals are configurable
- Can be disabled by commenting out in app.py

---

**All agents are properly configured and ready to test!** 🚀

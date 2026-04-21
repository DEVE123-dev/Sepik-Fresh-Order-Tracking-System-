-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2026 at 04:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sepik_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `agent_notifications`
--

CREATE TABLE `agent_notifications` (
  `id` int(11) NOT NULL,
  `agent_name` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `is_read` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contact_messages`
--

CREATE TABLE `contact_messages` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `is_read` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact_messages`
--

INSERT INTO `contact_messages` (`id`, `name`, `email`, `message`, `is_read`, `created_at`) VALUES
(5, 'Test User', 'test@example.com', 'This is a test message', 0, '2026-04-22 00:05:34');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `customer_number` varchar(50) NOT NULL,
  `registration_date` date NOT NULL DEFAULT curdate(),
  `preferred_contact_method` varchar(50) DEFAULT NULL,
  `status` enum('active','inactive') NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `user_id`, `customer_number`, `registration_date`, `preferred_contact_method`, `status`) VALUES
(2, 4, 'SF-CUST-00001', '2026-04-12', NULL, 'active'),
(3, 5, 'SF-CUST-00002', '2026-04-13', NULL, 'active'),
(4, 7, 'SF-CUST-00003', '2026-04-21', NULL, 'active');

-- --------------------------------------------------------

--
-- Table structure for table `email_notifications`
--

CREATE TABLE `email_notifications` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `type` varchar(50) NOT NULL,
  `sent` tinyint(1) NOT NULL DEFAULT 0,
  `sent_at` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `email_notifications`
--

INSERT INTO `email_notifications` (`id`, `user_id`, `email`, `subject`, `message`, `type`, `sent`, `sent_at`, `created_at`) VALUES
(1, 3, 'john.sepik@sepikfresh.pg', 'Order Confirmation - #7', '\n    <!DOCTYPE html>\n    <html>\n    <head>\n        <style>\n            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }\n            .container { max-width: 600px; margin: 0 auto; padding: 20px; }\n            .header { background: #2a7a30; color: white; padding: 20px; text-align: center; }\n            .content { padding: 20px; background: #f9f9f9; }\n            .order-details { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; }\n            .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }\n            .button { display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\">\n            <div class=\"header\">\n                <h1>Sepik Fresh</h1>\n                <p>Order Confirmation</p>\n            </div>\n            <div class=\"content\">\n                <h2>Thank you for your order, john paul!</h2>\n                <p>Your order has been received and is being processed.</p>\n                \n                <div class=\"order-details\">\n                    <h3>Order Details</h3>\n                    <p><strong>Order ID:</strong> #7</p>\n                    <p><strong>Total Amount:</strong> K18.00</p>\n                    <p><strong>Status:</strong> Pending</p>\n                    <p><strong>Order Date:</strong> 17 April 2026</p>\n                </div>\n                \n                <p>You can track your order status anytime by logging into your account.</p>\n                \n                <a href=\"http://localhost:5000/track/7\" class=\"button\">Track Order</a>\n                \n                <p>If you have any questions, please contact us at info@sepikfresh.pg</p>\n            </div>\n            <div class=\"footer\">\n                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>\n                <p>Wewak, East Sepik Province, PNG</p>\n            </div>\n        </div>\n    </body>\n    </html>\n    ', 'order_confirmation', 1, '2026-04-17 10:06:11', '2026-04-17 10:06:11'),
(2, 3, 'john.sepik@sepikfresh.pg', 'Order Update - #7', '\n    <!DOCTYPE html>\n    <html>\n    <head>\n        <style>\n            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }\n            .container { max-width: 600px; margin: 0 auto; padding: 20px; }\n            .header { background: #2a7a30; color: white; padding: 20px; text-align: center; }\n            .content { padding: 20px; background: #f9f9f9; }\n            .status-update { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2a7a30; }\n            .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }\n            .button { display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\">\n            <div class=\"header\">\n                <h1>Sepik Fresh</h1>\n                <p>Order Status Update</p>\n            </div>\n            <div class=\"content\">\n                <h2>Hello john paul,</h2>\n                \n                <div class=\"status-update\">\n                    <h3>Order #7</h3>\n                    <p><strong>Status:</strong> Pending</p>\n                    <p>Your order status has been updated.</p>\n                </div>\n                \n                <a href=\"http://localhost:5000/track/7\" class=\"button\">Track Order</a>\n            </div>\n            <div class=\"footer\">\n                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>\n            </div>\n        </div>\n    </body>\n    </html>\n    ', 'status_update', 1, '2026-04-17 12:02:11', '2026-04-17 12:02:11'),
(3, 3, 'john.sepik@sepikfresh.pg', 'Order Update - #7', '\n    <!DOCTYPE html>\n    <html>\n    <head>\n        <style>\n            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }\n            .container { max-width: 600px; margin: 0 auto; padding: 20px; }\n            .header { background: #2a7a30; color: white; padding: 20px; text-align: center; }\n            .content { padding: 20px; background: #f9f9f9; }\n            .status-update { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2a7a30; }\n            .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }\n            .button { display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\">\n            <div class=\"header\">\n                <h1>Sepik Fresh</h1>\n                <p>Order Status Update</p>\n            </div>\n            <div class=\"content\">\n                <h2>Hello john paul,</h2>\n                \n                <div class=\"status-update\">\n                    <h3>Order #7</h3>\n                    <p><strong>Status:</strong> Confirmed</p>\n                    <p>Your order has been confirmed and is being prepared.</p>\n                </div>\n                \n                <a href=\"http://localhost:5000/track/7\" class=\"button\">Track Order</a>\n            </div>\n            <div class=\"footer\">\n                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>\n            </div>\n        </div>\n    </body>\n    </html>\n    ', 'status_update', 1, '2026-04-17 12:02:16', '2026-04-17 12:02:16'),
(4, 3, 'john.sepik@sepikfresh.pg', 'Order Update - #7', '\n    <!DOCTYPE html>\n    <html>\n    <head>\n        <style>\n            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }\n            .container { max-width: 600px; margin: 0 auto; padding: 20px; }\n            .header { background: #2a7a30; color: white; padding: 20px; text-align: center; }\n            .content { padding: 20px; background: #f9f9f9; }\n            .status-update { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2a7a30; }\n            .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }\n            .button { display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\">\n            <div class=\"header\">\n                <h1>Sepik Fresh</h1>\n                <p>Order Status Update</p>\n            </div>\n            <div class=\"content\">\n                <h2>Hello john paul,</h2>\n                \n                <div class=\"status-update\">\n                    <h3>Order #7</h3>\n                    <p><strong>Status:</strong> Cancelled</p>\n                    <p>Your order has been cancelled.</p>\n                </div>\n                \n                <a href=\"http://localhost:5000/track/7\" class=\"button\">Track Order</a>\n            </div>\n            <div class=\"footer\">\n                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>\n            </div>\n        </div>\n    </body>\n    </html>\n    ', 'status_update', 1, '2026-04-17 12:03:49', '2026-04-17 12:03:49'),
(5, 3, 'john.sepik@sepikfresh.pg', 'Order Update - #7', '\n    <!DOCTYPE html>\n    <html>\n    <head>\n        <style>\n            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }\n            .container { max-width: 600px; margin: 0 auto; padding: 20px; }\n            .header { background: #2a7a30; color: white; padding: 20px; text-align: center; }\n            .content { padding: 20px; background: #f9f9f9; }\n            .status-update { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2a7a30; }\n            .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }\n            .button { display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\">\n            <div class=\"header\">\n                <h1>Sepik Fresh</h1>\n                <p>Order Status Update</p>\n            </div>\n            <div class=\"content\">\n                <h2>Hello john paul,</h2>\n                \n                <div class=\"status-update\">\n                    <h3>Order #7</h3>\n                    <p><strong>Status:</strong> Cancelled</p>\n                    <p>Your order has been cancelled.</p>\n                </div>\n                \n                <a href=\"http://localhost:5000/track/7\" class=\"button\">Track Order</a>\n            </div>\n            <div class=\"footer\">\n                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>\n            </div>\n        </div>\n    </body>\n    </html>\n    ', 'status_update', 1, '2026-04-17 12:04:08', '2026-04-17 12:04:08');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `order_date` datetime NOT NULL DEFAULT current_timestamp(),
  `total_amount` decimal(12,2) NOT NULL DEFAULT 0.00 CHECK (`total_amount` >= 0),
  `order_status` enum('pending','confirmed','processing','out_for_delivery','delivered','cancelled') NOT NULL DEFAULT 'pending',
  `estimated_delivery_time` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  `deleted_at` datetime DEFAULT NULL,
  `cancelled_at` datetime DEFAULT NULL,
  `cancellation_reason` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `item_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT 1,
  `unit_price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `token` varchar(255) NOT NULL,
  `expires_at` datetime NOT NULL,
  `used` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_category` enum('poultry','eggs') NOT NULL,
  `unit_price` decimal(10,2) NOT NULL CHECK (`unit_price` >= 0),
  `stock_quantity` int(11) NOT NULL DEFAULT 0 CHECK (`stock_quantity` >= 0),
  `description` text DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `is_available` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_category`, `unit_price`, `stock_quantity`, `description`, `image_url`, `is_available`, `created_at`, `updated_at`, `deleted_at`) VALUES
(2, 'Whole Fresh Chicken (1.5kg)', 'poultry', 28.90, 885, 'Locally raised whole chicken, cleaned and ready for cooking.', '/static/images/products/wholefreshchicken.jpg', 1, '2026-04-12 20:03:36', '2026-04-21 23:43:00', NULL),
(3, 'Chicken Pieces (1kg)', 'poultry', 18.00, 897, 'Mixed chicken pieces, ideal for soups and stews.', '/static/images/products/chickenpieces.jpg', 1, '2026-04-12 20:03:36', '2026-04-21 23:43:00', NULL),
(4, 'Fresh Eggs (Tray of 30)', 'eggs', 22.00, 8980, 'Farm fresh eggs, collected daily from local farms.', '/static/images/products/30eggs.jpg', 1, '2026-04-12 20:03:36', '2026-04-21 23:43:00', NULL),
(5, 'Fresh Eggs (Dozen)', 'eggs', 9.50, 8985, 'Fresh dozen eggs, perfect for everyday use.', '/static/images/products/dozeneggs.jpg', 1, '2026-04-12 20:03:36', '2026-04-21 23:43:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` enum('customer','admin','delivery_staff') NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `password_hash`, `role`, `phone`, `address`, `created_at`, `is_active`, `updated_at`) VALUES
(1, 'Penington', ' akamiau', 'penningtonakamiau@gmail.com', '$2b$12$1Hkyi5gAgQbrdnLszdGaAuZ3CfPgWABDuuB5ghcTUl5wx9lQDTnNm', 'delivery_staff', '+675 7123 4567', '14 Maprik Road, Wewak, East Sepik Province', '2025-01-10 08:30:00', 1, NULL),
(2, 'isho', 'jonduo', 'ishojonduo@gmail.com', '$2b$12$I5GMBqVRPYb0h1RibItlWOMM0D4V.U2pqLYHBE5zajCSk9LgAmY8G', 'admin', '+675 7200 0001', 'Sepik Fresh HQ, Wewak', '2024-12-01 07:00:00', 1, NULL),
(3, 'Benjamin', 'Bino', 'benjaminbino19@gmail.com', '$2b$12$vSnWUYYOv/PvYI10EygZh.x3FEbZca0seQU1f32tJHP5klQLI3N4q', 'delivery_staff', '+675 7300 0002', 'bomana,turnoff', '2024-12-05 07:00:00', 1, NULL),
(4, 'Peter', 'isho', 'devesmash79@gmail.com', '$2b$12$XryaAQXX9/3VDQj5hpaXseFXmkBADsUx.KDvUmCPLpvap8JyZaXVW', 'customer', '83182300', 'bomana', '2026-04-12 21:11:25', 1, NULL),
(5, 'john', 'paul', 'john.sepik@sepikfresh.pg', '$2b$12$ims7Xz4ufzCjvEgShtXpzeB//lR8hEGCwpZ5g0mPQWRIgcFvgv.jy', 'customer', '83182300', 'bomana', '2026-04-13 11:58:22', 1, NULL),
(6, 'Admin', 'User', 'admin', '$2b$12$WaEt9MEp938lKT3YLFzPf.OjPS2.kvMoZCkc340NCZJYmwuiaiYXK', 'admin', '+675 7200 0001', 'Sepik Fresh HQ, Wewak', '2026-04-21 10:29:41', 1, NULL),
(7, 'Basic', 'User', 'basic', '$2b$12$RERIl1dn99x9mJq3lbRFQuNsM44bQ8ukjLthZqE/nf15WGMT5VaPG', 'customer', '+675 7300 0002', 'Wewak, East Sepik Province', '2026-04-21 10:29:41', 1, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agent_notifications`
--
ALTER TABLE `agent_notifications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact_messages`
--
ALTER TABLE `contact_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `customer_number` (`customer_number`);

--
-- Indexes for table `email_notifications`
--
ALTER TABLE `email_notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `idx_orders_customer` (`customer_id`),
  ADD KEY `idx_orders_status` (`order_status`),
  ADD KEY `idx_orders_date` (`order_date`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`item_id`),
  ADD KEY `fk_item_order` (`order_id`),
  ADD KEY `fk_item_product` (`product_id`),
  ADD KEY `idx_order_items_order` (`order_id`),
  ADD KEY `idx_order_items_product` (`product_id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token` (`token`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `idx_products_category` (`product_category`),
  ADD KEY `idx_products_available` (`is_available`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `idx_users_email` (`email`),
  ADD KEY `idx_users_role` (`role`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agent_notifications`
--
ALTER TABLE `agent_notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `contact_messages`
--
ALTER TABLE `contact_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `email_notifications`
--
ALTER TABLE `email_notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `fk_customers_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `fk_orders_customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON UPDATE CASCADE;

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `fk_item_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_item_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE CASCADE;

--
-- Constraints for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD CONSTRAINT `fk_reset_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

"""
Unit tests for database models
Run with: pytest tests/test_models.py
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import User, Product, Order, Customer
import bcrypt


class TestUserModel:
    """Test User model operations"""
    
    def test_password_hashing(self):
        """Test that passwords are properly hashed"""
        password = "testpassword123"
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        # Verify password can be checked
        assert User.check_password(password, hashed) == True
        assert User.check_password("wrongpassword", hashed) == False
    
    def test_password_check_with_invalid_hash(self):
        """Test password check with invalid hash"""
        result = User.check_password("password", "invalid_hash")
        assert result == False
    
    def test_user_count(self):
        """Test user count method"""
        count = User.count()
        assert isinstance(count, int)
        assert count >= 0


class TestProductModel:
    """Test Product model operations"""
    
    def test_get_all_products(self):
        """Test retrieving all products"""
        products = Product.get_all()
        assert isinstance(products, list)
    
    def test_get_available_products(self):
        """Test retrieving only available products"""
        products = Product.get_available()
        assert isinstance(products, list)
        
        # All returned products should be available
        for product in products:
            assert product['is_available'] == 1
    
    def test_product_count(self):
        """Test product count method"""
        count = Product.count()
        assert isinstance(count, int)
        assert count >= 0
    
    def test_product_search(self):
        """Test product search functionality"""
        # Search for common term
        results = Product.search("chicken")
        assert isinstance(results, list)


class TestOrderModel:
    """Test Order model operations"""
    
    def test_get_all_orders(self):
        """Test retrieving all orders"""
        orders = Order.get_all()
        assert isinstance(orders, list)
    
    def test_order_count(self):
        """Test order count method"""
        count = Order.count()
        assert isinstance(count, int)
        assert count >= 0
    
    def test_active_order_count(self):
        """Test active order count"""
        count = Order.count_active()
        assert isinstance(count, int)
        assert count >= 0
    
    def test_order_search(self):
        """Test order search functionality"""
        results = Order.search("john")
        assert isinstance(results, list)


class TestCustomerModel:
    """Test Customer model operations"""
    
    def test_get_customer_by_user_id(self):
        """Test retrieving customer by user ID"""
        # Test with non-existent user
        customer = Customer.get_by_user_id(99999)
        assert customer is None or isinstance(customer, dict)


# Integration Tests
class TestIntegration:
    """Test integration between models"""
    
    def test_database_connection(self):
        """Test that database connection works"""
        try:
            count = User.count()
            assert isinstance(count, int)
        except Exception as e:
            pytest.fail(f"Database connection failed: {str(e)}")
    
    def test_user_customer_relationship(self):
        """Test User-Customer relationship"""
        users = User.get_all()
        if users:
            user = users[0]
            customer = Customer.get_by_user_id(user['user_id'])
            # Customer may or may not exist depending on role
            assert customer is None or isinstance(customer, dict)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

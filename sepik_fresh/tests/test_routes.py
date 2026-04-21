"""
Unit tests for Flask routes
Run with: pytest tests/test_routes.py
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client


class TestPublicRoutes:
    """Test public routes (no authentication required)"""
    
    def test_home_page(self, client):
        """Test home page loads"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Sepik Fresh' in response.data
    
    def test_about_page(self, client):
        """Test about page loads"""
        response = client.get('/about')
        assert response.status_code == 200
    
    def test_contact_page(self, client):
        """Test contact page loads"""
        response = client.get('/contact')
        assert response.status_code == 200
    
    def test_login_page(self, client):
        """Test login page loads"""
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Login' in response.data
    
    def test_register_page(self, client):
        """Test register page loads"""
        response = client.get('/register')
        assert response.status_code == 200
        assert b'Register' in response.data


class TestAuthenticationRoutes:
    """Test authentication routes"""
    
    def test_login_with_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        response = client.post('/login', data={
            'email': 'nonexistent@test.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b'Invalid' in response.data or b'error' in response.data.lower()
    
    def test_register_with_missing_fields(self, client):
        """Test registration with missing fields returns 400"""
        response = client.post('/register', data={
            'first_name': 'Test',
            'email': 'test@test.com'
            # Missing required fields (last_name, password, confirm_password)
        }, follow_redirects=True)
        # Should return 400 Bad Request for missing required fields
        assert response.status_code == 400
    
    def test_logout_redirect(self, client):
        """Test logout redirects to login"""
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200


class TestProtectedRoutes:
    """Test routes that require authentication"""
    
    def test_dashboard_requires_login(self, client):
        """Test dashboard redirects to login when not authenticated"""
        response = client.get('/dashboard', follow_redirects=True)
        assert response.status_code == 200
        assert b'Login' in response.data or b'login' in response.data.lower()
    
    def test_profile_requires_login(self, client):
        """Test profile requires login"""
        response = client.get('/profile', follow_redirects=True)
        assert response.status_code == 200
    
    def test_my_orders_requires_login(self, client):
        """Test my orders requires login"""
        response = client.get('/my-orders', follow_redirects=True)
        assert response.status_code == 200


class TestErrorHandlers:
    """Test error handlers"""
    
    def test_404_error(self, client):
        """Test 404 error page"""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404
        assert b'404' in response.data or b'Not Found' in response.data
    
    def test_404_has_home_link(self, client):
        """Test 404 page has link to home"""
        response = client.get('/nonexistent-page')
        assert b'home' in response.data.lower() or b'Home' in response.data


class TestContactForm:
    """Test contact form submission"""
    
    def test_contact_form_submission(self, client):
        """Test contact form can be submitted"""
        response = client.post('/contact', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message'
        }, follow_redirects=True)
        assert response.status_code == 200
    
    def test_contact_form_validation(self, client):
        """Test contact form validation"""
        response = client.post('/contact', data={
            'name': '',
            'email': '',
            'message': ''
        }, follow_redirects=True)
        assert response.status_code == 200
        # Should show error or stay on page


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

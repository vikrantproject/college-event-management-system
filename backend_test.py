import requests
import sys
import json
from datetime import datetime, timedelta

class CollegeEventAPITester:
    def __init__(self, base_url="https://eventify-portal.preview.emergentagent.com"):
        self.base_url = base_url
        self.admin_token = None
        self.user_token = None
        self.admin_user = None
        self.regular_user = None
        self.test_event_id = None
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, token=None):
        """Run a single API test"""
        url = f"{self.base_url}/api/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    return success, response.json()
                except:
                    return success, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"   Error: {error_detail}")
                except:
                    print(f"   Response: {response.text}")
                self.failed_tests.append(f"{name}: Expected {expected_status}, got {response.status_code}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append(f"{name}: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root API", "GET", "", 200)

    def test_admin_signup(self):
        """Test admin user signup"""
        admin_data = {
            "name": f"Admin User {datetime.now().strftime('%H%M%S')}",
            "email": f"admin_{datetime.now().strftime('%H%M%S')}@college.edu",
            "password": "AdminPass123!",
            "role": "admin"
        }
        
        success, response = self.run_test(
            "Admin Signup",
            "POST",
            "auth/signup",
            200,
            data=admin_data
        )
        
        if success and 'access_token' in response:
            self.admin_token = response['access_token']
            self.admin_user = response['user']
            return True
        return False

    def test_user_signup(self):
        """Test regular user signup"""
        user_data = {
            "name": f"Regular User {datetime.now().strftime('%H%M%S')}",
            "email": f"user_{datetime.now().strftime('%H%M%S')}@college.edu",
            "password": "UserPass123!",
            "role": "user"
        }
        
        success, response = self.run_test(
            "User Signup",
            "POST",
            "auth/signup",
            200,
            data=user_data
        )
        
        if success and 'access_token' in response:
            self.user_token = response['access_token']
            self.regular_user = response['user']
            return True
        return False

    def test_admin_login(self):
        """Test admin login"""
        if not self.admin_user:
            return False
            
        login_data = {
            "email": self.admin_user['email'],
            "password": "AdminPass123!"
        }
        
        success, response = self.run_test(
            "Admin Login",
            "POST",
            "auth/login",
            200,
            data=login_data
        )
        
        if success and 'access_token' in response:
            self.admin_token = response['access_token']
            return True
        return False

    def test_user_login(self):
        """Test user login"""
        if not self.regular_user:
            return False
            
        login_data = {
            "email": self.regular_user['email'],
            "password": "UserPass123!"
        }
        
        success, response = self.run_test(
            "User Login",
            "POST",
            "auth/login",
            200,
            data=login_data
        )
        
        if success and 'access_token' in response:
            self.user_token = response['access_token']
            return True
        return False

    def test_create_event(self):
        """Test event creation (admin only)"""
        if not self.admin_token:
            return False
            
        event_data = {
            "title": f"Test Event {datetime.now().strftime('%H%M%S')}",
            "description": "This is a test event for API testing",
            "date": (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            "location": "Test Auditorium",
            "image_url": "https://example.com/test-image.jpg"
        }
        
        success, response = self.run_test(
            "Create Event",
            "POST",
            "events",
            200,
            data=event_data,
            token=self.admin_token
        )
        
        if success and 'id' in response:
            self.test_event_id = response['id']
            return True
        return False

    def test_get_events(self):
        """Test getting all events"""
        return self.run_test("Get All Events", "GET", "events", 200)

    def test_get_event_by_id(self):
        """Test getting event by ID"""
        if not self.test_event_id:
            return False
            
        return self.run_test(
            "Get Event by ID",
            "GET",
            f"events/{self.test_event_id}",
            200
        )

    def test_search_events(self):
        """Test event search functionality"""
        return self.run_test(
            "Search Events",
            "GET",
            "events?search=Test",
            200
        )

    def test_update_event(self):
        """Test event update (admin only)"""
        if not self.admin_token or not self.test_event_id:
            return False
            
        update_data = {
            "title": f"Updated Test Event {datetime.now().strftime('%H%M%S')}",
            "description": "This event has been updated"
        }
        
        return self.run_test(
            "Update Event",
            "PUT",
            f"events/{self.test_event_id}",
            200,
            data=update_data,
            token=self.admin_token
        )

    def test_register_for_event(self):
        """Test event registration (user)"""
        if not self.user_token or not self.test_event_id:
            return False
            
        registration_data = {
            "event_id": self.test_event_id
        }
        
        return self.run_test(
            "Register for Event",
            "POST",
            "registrations",
            200,
            data=registration_data,
            token=self.user_token
        )

    def test_get_user_registrations(self):
        """Test getting user registrations"""
        if not self.user_token or not self.regular_user:
            return False
            
        return self.run_test(
            "Get User Registrations",
            "GET",
            f"registrations/user/{self.regular_user['id']}",
            200,
            token=self.user_token
        )

    def test_admin_stats(self):
        """Test admin stats endpoint"""
        if not self.admin_token:
            return False
            
        return self.run_test(
            "Admin Stats",
            "GET",
            "admin/stats",
            200,
            token=self.admin_token
        )

    def test_admin_registrations(self):
        """Test admin view all registrations"""
        if not self.admin_token:
            return False
            
        return self.run_test(
            "Admin All Registrations",
            "GET",
            "admin/registrations",
            200,
            token=self.admin_token
        )

    def test_unauthorized_access(self):
        """Test unauthorized access to admin endpoints"""
        success, _ = self.run_test(
            "Unauthorized Admin Stats",
            "GET",
            "admin/stats",
            401
        )
        return success

    def test_user_cannot_create_event(self):
        """Test that regular users cannot create events"""
        if not self.user_token:
            return False
            
        event_data = {
            "title": "Unauthorized Event",
            "description": "This should fail",
            "date": (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            "location": "Test Location"
        }
        
        return self.run_test(
            "User Cannot Create Event",
            "POST",
            "events",
            403,
            data=event_data,
            token=self.user_token
        )

    def test_delete_event(self):
        """Test event deletion (admin only)"""
        if not self.admin_token or not self.test_event_id:
            return False
            
        return self.run_test(
            "Delete Event",
            "DELETE",
            f"events/{self.test_event_id}",
            200,
            token=self.admin_token
        )

    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🚀 Starting College Event Management System API Tests")
        print(f"📍 Testing against: {self.base_url}")
        
        # Basic API test
        self.test_root_endpoint()
        
        # Authentication tests
        if not self.test_admin_signup():
            print("❌ Admin signup failed, stopping tests")
            return False
            
        if not self.test_user_signup():
            print("❌ User signup failed, stopping tests")
            return False
            
        # Login tests
        self.test_admin_login()
        self.test_user_login()
        
        # Event management tests
        self.test_create_event()
        self.test_get_events()
        self.test_get_event_by_id()
        self.test_search_events()
        self.test_update_event()
        
        # Registration tests
        self.test_register_for_event()
        self.test_get_user_registrations()
        
        # Admin tests
        self.test_admin_stats()
        self.test_admin_registrations()
        
        # Security tests
        self.test_unauthorized_access()
        self.test_user_cannot_create_event()
        
        # Cleanup
        self.test_delete_event()
        
        return True

    def print_summary(self):
        """Print test summary"""
        print(f"\n📊 Test Summary:")
        print(f"   Tests Run: {self.tests_run}")
        print(f"   Tests Passed: {self.tests_passed}")
        print(f"   Tests Failed: {self.tests_run - self.tests_passed}")
        print(f"   Success Rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        if self.failed_tests:
            print(f"\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"   - {test}")
        
        return self.tests_passed == self.tests_run

def main():
    tester = CollegeEventAPITester()
    
    try:
        tester.run_all_tests()
        success = tester.print_summary()
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Test execution failed: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
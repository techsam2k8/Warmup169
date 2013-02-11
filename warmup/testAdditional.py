"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib


class TestAddEmptyUser(testLib.RestTestCase):
    """Test adding user with empty user name"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

class TestAddLongUser(testLib.RestTestCase):
    """Test adding user with long user name"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        user = ''
        for num in range(130):
            user += 'A'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : user, 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)
    
class TestAddLongPassword(testLib.RestTestCase):
    """Test adding user with long password"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        password = ''
        for num in range(130):
            password += 'A'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : password} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestAddUserExists(testLib.RestTestCase):
    """Test adding user with same user name"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        
        self.assertResponse(respData, count = 1) 

        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'pass'} )

        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_USER_EXISTS) 

class TestAddTwoUsers(testLib.RestTestCase):
    """Test adding users with different names"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count = 1) 

        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'pass'} )

        self.assertResponse(respData, count = 1) 
        
class TestLoginBadCred(testLib.RestTestCase):
    """Test logging in with wrong password"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count = 1) 

        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'pass'} )

        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

        

class TestLoginUpdateCount(testLib.RestTestCase):
    """Test updating the count through multiple logins"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count = 1) 

        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )

        self.assertResponse(respData, count = 2)        
        
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )

        self.assertResponse(respData, count = 3) 

class TestReset(testLib.RestTestCase):
    """Test the reset by checking for the user in the database"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count = 1) 

        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST")

        self.assertResponse(respData, count = None)        
        
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )

        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)                   
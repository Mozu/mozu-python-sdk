import unittest
import logging
from mozurestsdk.security.appauthenticator import AppAuthenticator;
from mozurestsdk.config import __baseUrl__

class AppAuthenticator_Test(unittest.TestCase):
    def test_authenticate(self):
        logging.basicConfig(level=logging.INFO)
        authenticator = AppAuthenticator("mzint.sdk.1.0.0.release","32223d1c8c694c9196e95a032bb100b5",__baseUrl__, False);
        auth = authenticator.authenticate();
        self.assertIsNotNone(authenticator.auth["accessToken"]);
        self.assertIsNotNone(authenticator.auth["refreshToken"]);

if __name__ == '__main__':
    unittest.main()

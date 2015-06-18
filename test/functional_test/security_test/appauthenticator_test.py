import unittest
import logging
from mozurestsdk.security.appauthenticator import AppAuthenticator;
from mozurestsdk.config import __baseUrl__

class AppAuthenticator_Test(unittest.TestCase):
    def test_authenticate(self):
        logging.basicConfig(level=logging.INFO)
        authenticator = AppAuthenticator();
        auth = authenticator.authenticate("mzint.sdk.1.0.0.release","32223d1c8c694c9196e95a032bb100b5",__baseUrl__);
        self.assertIsNotNone(auth["accessToken"]);
        self.assertIsNotNone(auth["refreshToken"]);

if __name__ == '__main__':
    unittest.main()

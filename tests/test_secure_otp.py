import unittest
from secure_otp import generate_otp

class TestSecureOTP(unittest.TestCase):
    def test_otp_length_default(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

    def test_otp_length_custom(self):
        otp = generate_otp(8)
        self.assertEqual(len(otp), 8)
        self.assertTrue(otp.isdigit())

    def test_otp_randomness(self):
        otp1 = generate_otp()
        otp2 = generate_otp()
        self.assertNotEqual(otp1, otp2, "Two OTPs should not be the same")

if __name__ == "__main__":
    unittest.main()

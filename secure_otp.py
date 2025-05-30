import secrets

def generate_otp(length=6):
    """Generate a secure numeric OTP of given length."""
    return ''.join(str(secrets.randbelow(10)) for _ in range(length))

if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)

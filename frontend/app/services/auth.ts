import axios from 'axios';

export async function signInWithEmailOrPhone(emailOrPhone: string, password: string) {
  try {
    const response = await axios.post('/login', { email_or_phone: emailOrPhone, password });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

export async function sendMagicCode(emailOrPhone: string) {
  try {
    const response = await axios.post('/send_code', { email_or_phone: emailOrPhone });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

export async function verifyMagicCode(emailOrPhone: string, code: string) {
  try {
    const response = await axios.post('/verify_code', { email_or_phone: emailOrPhone, code });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

export async function signInWithGoogle() {
  // handle Google Sign In
}
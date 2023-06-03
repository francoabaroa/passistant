import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',
});

export async function signInWithEmailOrPhone(emailOrPhone: string, password: string) {
  try {
    const response = await api.post('/login', { email_or_phone: emailOrPhone, password });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

export async function sendMagicCode(emailOrPhone: string) {
  try {
    const response = await api.post('/send_code', { email_or_phone: emailOrPhone }, {
      headers: {
        'Content-Type': 'application/json'
      },
      withCredentials: true
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

export async function verifyMagicCode(emailOrPhone: string, code: string) {
  try {
    const response = await api.post('/verify_code', { email_or_phone: emailOrPhone, code }, {
      headers: {
        'Content-Type': 'application/json'
      },
      withCredentials: true
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export async function signInWithGoogle() {
  // handle Google Sign In
}
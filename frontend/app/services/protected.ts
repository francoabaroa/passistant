import axios from 'axios';

export async function getProtectedData(accessToken: string) {
  try {
    const response = await axios.get('/protected', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
'use client';

import React, { useState } from 'react';
import { signInWithGoogle, signInWithEmailOrPhone, sendMagicCode } from '../services/auth';

const LoginComponent: React.FC = () => {
  const [emailOrPhone, setEmailOrPhone] = useState('');
  const [password, setPassword] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.name === 'emailOrPhone') {
      setEmailOrPhone(e.target.value);
    } else if (e.target.name === 'password') {
      setPassword(e.target.value);
    }
  };

  const handleLogin = async () => {
    await signInWithEmailOrPhone(emailOrPhone, password);
  };

  const handleMagicCode = async () => {
    await sendMagicCode(emailOrPhone);
  };

  const handleGoogleSignIn = async () => {
    await signInWithGoogle();
  };

  return (
    <div className="mx-auto w-full max-w-md">
      <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in</h2>
      <form className="mt-8 space-y-6">
        <div className="rounded-md shadow-sm space-y-6">
          <div>
            <label htmlFor="emailOrPhone" className="sr-only">Email address or Phone number</label>
            <input
              id="emailOrPhone"
              name="emailOrPhone"
              type="text"
              autoComplete="off"
              required
              className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Email address or Phone number"
              value={emailOrPhone}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="password" className="sr-only">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              autoComplete="current-password"
              required
              className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Password"
              value={password}
              onChange={handleInputChange}
            />
          </div>
        </div>
        <div>
          <button
            type="button"
            onClick={handleLogin}
            className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Sign in
          </button>
          <button
            type="button"
            onClick={handleMagicCode}
            className="mt-4 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-500 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            Sign in with Magic Code
          </button>
          <button
            type="button"
            onClick={handleGoogleSignIn}
            className="mt-4 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Sign in with Google
          </button>
        </div>
      </form>
    </div>
  );
};

export default LoginComponent;
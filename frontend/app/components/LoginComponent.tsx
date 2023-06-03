'use client';

import React, { useState } from 'react';
import { signInWithGoogle, signInWithEmailOrPhone, sendMagicCode, verifyMagicCode } from '../services/auth';
import Modal from './Modal';

const LoginComponent: React.FC = () => {
  const [code, setCode] = useState('');
  const [emailOrPhone, setEmailOrPhone] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('');
  const [useMagicLogin, setUseMagicLogin] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.name === 'emailOrPhone') {
      setEmailOrPhone(e.target.value);
    } else if (e.target.name === 'password') {
      setPassword(e.target.value);
    } else if (e.target.name === 'code') {
      setCode(e.target.value);
    }
  };

  const handlePhoneInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.name === 'phone') {
      setPhone(e.target.value);
    }
  };

  const openMagicCodeModal = () => {
    setIsModalOpen(true);
    setUseMagicLogin(true);
  }

  const handleLogin = async () => {
    await signInWithEmailOrPhone(emailOrPhone, password);
  };

  const handleMagicCode = async () => {
    await sendMagicCode(phone);
    setIsModalOpen(false);
  };

  const handleGoogleSignIn = async () => {
    await signInWithGoogle();
  };

  const handleVerifyMagicCode = async () => {
    const response = await verifyMagicCode(phone, code);
    if (response.message === 'User verified') {
      window.location.href = 'http://localhost:3000//dashboard';
    }
  };

  const displayCorrectLogin = () => {
    if (useMagicLogin) {
      return (
        <>
          <div>
            <label htmlFor="phone" className="sr-only">Phone number</label>
            <input
              id="phone"
              name="phone"
              type="text"
              autoComplete="off"
              required
              className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Phone number"
              value={phone}
              onChange={handleInputChange}
            />
          </div>
          <div className="mt-4">
            <label htmlFor="code" className="sr-only">Code</label>
            <input
              id="code"
              name="code"
              autoComplete="off"
              type="text"
              required
              className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Enter code"
              value={code}
              onChange={handleInputChange}
            />
          </div>
        </>
      )
    } else {
      return (
        <>
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
          <div className="mt-4">
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
        </>
      )
    }
  };

  return (
    <div className="mx-auto w-full max-w-md">
      <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in</h2>
      <form className="mt-8 space-y-6">
        <div>
          { displayCorrectLogin() }
        </div>
        <div className="rounded-md shadow-sm space-y-6">
          <div>
            {
              !useMagicLogin ?
                <button
                  type="button"
                  onClick={handleLogin}
                  className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Sign in
                </button> :
                null
            }

            <button
              type="button"
              onClick={useMagicLogin ? handleVerifyMagicCode : openMagicCodeModal}
              className="mt-4 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-500 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
            >
              Sign in with Magic Code
            </button>

            {
              !useMagicLogin ?
                <button
                  type="button"
                  onClick={handleGoogleSignIn}
                  className="mt-4 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                >
                  Sign in with Google
                </button> :
                null
            }
          </div>
        </div>
      </form>
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} phone={phone} handlePhoneInputChange={handlePhoneInputChange} handleMagicCode={handleMagicCode} />
    </div>
  );
};

export default LoginComponent;
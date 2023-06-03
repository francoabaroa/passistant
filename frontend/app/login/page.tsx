import React from 'react';
import LoginComponent from '../components/LoginComponent';

const LoginPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <LoginComponent />
    </div>
  );
};

export default LoginPage;
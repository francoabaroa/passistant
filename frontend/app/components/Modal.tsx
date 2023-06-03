import React from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  phone: string;
  handlePhoneInputChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  handleMagicCode: () => void;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, handlePhoneInputChange, phone, handleMagicCode }) => {
  if (!isOpen) {
    return null;
  }

  return (
    <div className="App">
      <div className="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" onClick={onClose} />
          <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
          <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div className="sm:flex sm:items-start">
                <div className="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3 className="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                    Get Magic Code
                  </h3>
                  <div className="mt-2">
                    <p className="text-sm text-gray-500">
                      Enter phone number with country code (i.e. +13057863452)
                    </p>
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
                        onChange={handlePhoneInputChange}
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button type="button" className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm" onClick={onClose}>
                Close
              </button>
              <button type="button" className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm" onClick={handleMagicCode}>
                Get Code
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Modal;

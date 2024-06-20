// src/components/ParameterInput.js
import React from 'react';

const ParameterInput = ({ label, id, defaultValue, min, placeholder, onChange }) => {
  return (
    <div className="mb-4">
      <label htmlFor={id} className="block text-sm font-medium text-gray-700">
        {label}
      </label>
      <input
        type="number"
        id={id}
        defaultValue={defaultValue}
        min={min}
        placeholder={placeholder}
        className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        onChange={onChange}
      />
    </div>
  );
};

export default ParameterInput;

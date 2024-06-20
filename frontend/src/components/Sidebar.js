import React, { useState } from "react";

const Sidebar = () => {
  const [inputs, setInputs] = useState({
    input1: "",
    input2: "",
    input3: "",
    input4: "",
  });

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  return (
    <div className="w-1/4 bg-white shadow-md p-4 flex flex-col justify-center space-y-4 rounded-md">
      <input
        type="text"
        name="input1"
        value={inputs.input1}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        placeholder="Input 1"
      />
      <input
        type="text"
        name="input2"
        value={inputs.input2}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        placeholder="Input 2"
      />
      <input
        type="text"
        name="input3"
        value={inputs.input3}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        placeholder="Input 3"
      />
      <input
        type="text"
        name="input4"
        value={inputs.input4}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        placeholder="Input 4"
      />
    </div>
  );
};

export default Sidebar;

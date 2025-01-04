import React from 'react';
import singup_person_img from "../assets/signup-person-image.png"; // Desktop image

const SignupForm = () => {
  return (
    <div className="flex flex-col md:flex-row justify-between items-center p-5 max-w-5xl mx-auto shadow-lg rounded-lg bg-white my-8 font-montserrat">
      {/* Left side form */}
      <div className="w-full md:flex-1 p-5">
        <h1 className="text-3xl md:text-4xl mb-4 text-center">
          Signup <span className="text-green-600">Now!</span>
        </h1>
        <p className="text-sm text-gray-600 mb-5 text-center md:text-left">
          Let's get started. Make sure to use your legal name for payout purposes.
        </p>
        <form className="flex flex-col">
          <div className="flex flex-col md:flex-row gap-4 mb-4">
            <input 
              type="text" 
              placeholder="First Name" 
              className="w-full md:flex-1 p-3 text-lg rounded border border-gray-300" 
            />
            <input 
              type="text" 
              placeholder="Last Name" 
              className="w-full md:flex-1 p-3 text-lg rounded border border-gray-300" 
            />
          </div>
          <input 
            type="email" 
            placeholder="Email" 
            className="mb-4 p-3 text-lg rounded border border-gray-300" 
          />
          <button 
            type="submit" 
            className="p-3 text-lg bg-green-600 text-white rounded hover:bg-green-700">
            Signup
          </button>
        </form>
      </div>

      {/* Right side image */}
      <div className="hidden md:flex w-full md:flex-1 justify-center items-center mt-5 md:mt-0">
        <img
          src={singup_person_img} // Replace with your image path
          alt="Signup visual"
          className="max-w-full h-auto rounded-lg"
        />
      </div>
    </div>
  );
};

export default SignupForm;

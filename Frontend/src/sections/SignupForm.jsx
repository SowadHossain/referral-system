import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import signupImage from "../assets/signup-person-image.png"; // Replace with your image path

const SignupForm = () => {
  const location = useLocation();

  // Form state
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    referralCode: "",
  });

  // Message state for success or error messages
  const [message, setMessage] = useState("");

  // Extract referral code from the query string if available
  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const referralCode = params.get("ref");
    if (referralCode) {
      setFormData((prev) => ({ ...prev, referralCode }));
    }
  }, [location]);

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(""); // Clear previous messages

    try {
      const response = await fetch("http://127.0.0.1:5000/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: `${formData.firstName} ${formData.lastName}`,
          email: formData.email,
          password: formData.password,
          referral_code: formData.referralCode, // Send referral code if available
        }),
      });

      const result = await response.json();

      if (response.ok) {
        setMessage(`Signup successful! Referral code: ${result.referral_code}`);
        setFormData({
          firstName: "",
          lastName: "",
          email: "",
          password: "",
          referralCode: "",
        }); // Reset form on success
      } else {
        setMessage(result.error || "An error occurred. Please try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred. Please check your network connection.");
    }
  };

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
        <form onSubmit={handleSubmit} className="flex flex-col">
          <div className="flex flex-col md:flex-row gap-4 mb-4">
            <input
              type="text"
              name="firstName"
              placeholder="First Name"
              value={formData.firstName}
              onChange={handleChange}
              className="w-full md:flex-1 p-3 text-lg rounded border border-gray-300"
              required
            />
            <input
              type="text"
              name="lastName"
              placeholder="Last Name"
              value={formData.lastName}
              onChange={handleChange}
              className="w-full md:flex-1 p-3 text-lg rounded border border-gray-300"
              required
            />
          </div>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="mb-4 p-3 text-lg rounded border border-gray-300"
            required
          />
  
          {formData.referralCode && (
            <p className="text-sm text-gray-600 mb-4">
              Referral Code: <span className="font-bold">{formData.referralCode}</span>
            </p>
          )}
          <button
            type="submit"
            className="p-3 text-lg bg-green-600 text-white rounded hover:bg-green-700"
          >
            Signup
          </button>
        </form>
        {/* Display success or error message
        {message && (
          <p
            className={`mt-4 text-center text-lg ${
              message.includes("successful") ? "text-green-600" : "text-red-500"
            }`}
          >
            {message}
          </p>
        )} */}
      </div>

      {/* Right side image */}
      <div className="hidden md:flex w-full md:flex-1 justify-center items-center mt-5 md:mt-0">
        <img
          src={signupImage}
          alt="Signup visual"
          className="max-w-full h-auto rounded-lg"
        />
      </div>
    </div>
  );
};

export default SignupForm;

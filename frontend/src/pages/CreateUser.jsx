import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import { api } from "../api/client";

export default function CreateUser() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    password: "",
    first_name: "",
    last_name: "",
    role: "",
    phone_number: "",
    department: "",
    job_title: "",
    is_active: true,
  });

  function handleChange(event) {
    const { name, value, type, checked } = event.target;

    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      const response = await api.post(
        "/accounts/users/",
        form
      );

      console.log("SUCCESS:", response.data);

      toast.success("User created successfully");

      navigate("/users");
    } catch (error) {
      console.error("FULL ERROR:", error);

      const errorData =
        error.response?.data || {
          message: "Unknown error",
        };

      console.log(
        "BACKEND RESPONSE:",
        errorData
      );

      alert(
        JSON.stringify(
          errorData,
          null,
          2
        )
      );

      toast.error("Failed to create user");
    }
  }

  return (
    <div className="max-w-3xl">
      <div className="card">
        <h1 className="text-3xl font-bold mb-6">
          Create User
        </h1>

        <form
          onSubmit={handleSubmit}
          className="space-y-4"
        >
          <input
            className="input"
            name="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
          />

          <input
            className="input"
            type="password"
            name="password"
            placeholder="Password"
            value={form.password}
            onChange={handleChange}
            required
          />

          <input
            className="input"
            name="first_name"
            placeholder="First Name"
            value={form.first_name}
            onChange={handleChange}
            required
          />

          <input
            className="input"
            name="last_name"
            placeholder="Last Name"
            value={form.last_name}
            onChange={handleChange}
            required
          />

          <input
            className="input"
            name="role"
            placeholder="Role UUID"
            value={form.role}
            onChange={handleChange}
          />

          <input
            className="input"
            name="phone_number"
            placeholder="Phone Number"
            value={form.phone_number}
            onChange={handleChange}
          />

          <input
            className="input"
            name="department"
            placeholder="Department"
            value={form.department}
            onChange={handleChange}
          />

          <input
            className="input"
            name="job_title"
            placeholder="Job Title"
            value={form.job_title}
            onChange={handleChange}
          />

          <label className="flex gap-2 items-center">
            <input
              type="checkbox"
              name="is_active"
              checked={form.is_active}
              onChange={handleChange}
            />
            Active User
          </label>

          <button
            className="btn btn-primary"
            type="submit"
          >
            Create User
          </button>
        </form>
      </div>
    </div>
  );
}
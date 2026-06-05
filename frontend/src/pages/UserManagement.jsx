import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";

export default function UserManagement() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers();
  }, []);

  async function fetchUsers() {
    try {
      const response = await api.get("/accounts/users/");
      setUsers(response.data.results || response.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <div>Loading users...</div>;
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">
          User Management
        </h1>

        <Link
          to="/users/create"
          className="btn btn-primary"
        >
          Create User
        </Link>
      </div>

      <div className="card overflow-auto">
        <table className="w-full">
          <thead>
            <tr>
              <th className="text-left p-3">Email</th>
              <th className="text-left p-3">Name</th>
              <th className="text-left p-3">Department</th>
              <th className="text-left p-3">Job Title</th>
              <th className="text-left p-3">Status</th>
            </tr>
          </thead>

          <tbody>
            {users.map((user) => (
              <tr
                key={user.id}
                className="border-t"
              >
                <td className="p-3">
                  {user.email}
                </td>

                <td className="p-3">
                  {user.first_name} {user.last_name}
                </td>

                <td className="p-3">
                  {user.department}
                </td>

                <td className="p-3">
                  {user.job_title}
                </td>

                <td className="p-3">
                  {user.is_active
                    ? "Active"
                    : "Inactive"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
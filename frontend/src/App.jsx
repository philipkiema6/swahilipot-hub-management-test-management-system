import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "react-hot-toast";

import { AppLayout } from "./layouts/AppLayout";
import { ProtectedRoute } from "./routes/ProtectedRoute";

import { Login } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
import { ModulePage } from "./pages/ModulePage";

import UserManagement from "./pages/UserManagement";
import CreateUser from "./pages/CreateUser";

import { modules } from "./constants/modules";

export function App() {
  return (
    <BrowserRouter>
      <Toaster />

      <Routes>
        <Route path="/login" element={<Login />} />

        <Route
          path="/"
          element={
            <ProtectedRoute>
              <AppLayout />
            </ProtectedRoute>
          }
        >
          <Route index element={<Dashboard />} />

          <Route path="users" element={<UserManagement />} />
          <Route path="users/create" element={<CreateUser />} />

          {modules
            .filter((m) => m.key !== "users")
            .map((m) => (
              <Route
                key={m.key}
                path={m.key}
                element={<ModulePage module={m} />}
              />
            ))}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
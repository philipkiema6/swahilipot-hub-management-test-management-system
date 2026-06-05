import{Navigate}from'react-router-dom';import{useAuthStore}from'../store/authStore';export function ProtectedRoute({children}){return useAuthStore(s=>s.accessToken)?children:<Navigate to='/login'/>}

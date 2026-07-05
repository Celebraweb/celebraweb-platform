import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "./auth.service";

export default function LoginPage() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleLogin() {
    try {
      const token = await login({
        email,
        password,
      });

      localStorage.setItem(
        "access_token",
        token.access_token
      );

      navigate("/dashboard");

    } catch (error: any) {

      console.error("ERROR:", error);
      console.error("STATUS:", error?.response?.status);
      console.error("DATA:", error?.response?.data);

      if (error?.response?.data?.detail) {
        setMessage(error.response.data.detail);
      } else {
        setMessage("Error al iniciar sesión.");
      }
    }
  }

  return (
    <div
      style={{
        maxWidth: "420px",
        margin: "40px auto",
        background: "#ffffff",
        padding: "30px",
        borderRadius: "10px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.10)",
      }}
    >
      <h1>Iniciar Sesión</h1>

      <p>Portal Plataforma - CelebraWeb XOP</p>

      <div style={{ marginTop: "20px" }}>
        <label>Correo electrónico</label>

        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "5px",
            marginBottom: "20px",
          }}
        />
      </div>

      <div>
        <label>Contraseña</label>

        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "5px",
            marginBottom: "20px",
          }}
        />
      </div>

      <button
        onClick={handleLogin}
        style={{
          width: "100%",
          padding: "12px",
          cursor: "pointer",
        }}
      >
        Iniciar Sesión
      </button>

      {message && (
        <p
          style={{
            marginTop: "20px",
            color: "red",
          }}
        >
          {message}
        </p>
      )}
    </div>
  );
}
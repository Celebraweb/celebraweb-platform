import { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;

  variant?: "primary" | "secondary" | "danger";
}

export default function Button({
  children,
  variant = "primary",
  style,
  ...props
}: ButtonProps) {
  const background =
    variant === "primary"
      ? "#2563eb"
      : variant === "secondary"
      ? "#6b7280"
      : "#dc2626";

  return (
    <button
      {...props}
      style={{
        background,
        color: "#ffffff",
        border: "none",
        borderRadius: "6px",
        padding: "10px 18px",
        cursor: "pointer",
        fontSize: "14px",
        fontWeight: 600,
        ...style,
      }}
    >
      {children}
    </button>
  );
}
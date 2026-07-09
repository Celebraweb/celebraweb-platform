import {
  forwardRef,
  InputHTMLAttributes,
} from "react";

interface InputProps
  extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      label,
      error,
      style,
      ...props
    },
    ref
  ) => {
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "6px",
          marginBottom: "18px",
        }}
      >
        {label && (
          <label
            style={{
              fontWeight: 600,
              fontSize: "14px",
            }}
          >
            {label}
          </label>
        )}

        <input
          ref={ref}
          {...props}
          style={{
            padding: "10px 12px",
            border: "1px solid #d1d5db",
            borderRadius: "6px",
            fontSize: "14px",
            outline: "none",
            ...style,
          }}
        />

        {error && (
          <span
            style={{
              color: "#dc2626",
              fontSize: "12px",
            }}
          >
            {error}
          </span>
        )}
      </div>
    );
  }
);

Input.displayName = "Input";

export default Input;
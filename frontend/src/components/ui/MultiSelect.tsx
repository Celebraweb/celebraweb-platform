import { useMemo } from "react";

interface MultiSelectOption {
  value: string;
  label: string;
}

interface MultiSelectProps {
  label: string;
  options: MultiSelectOption[];
  values: string[];
  onChange: (values: string[]) => void;
  required?: boolean;
}

export default function MultiSelect({
  label,
  options,
  values,
  onChange,
  required = false,
}: MultiSelectProps) {

  const selected = useMemo(
    () => new Set(values),
    [values],
  );

  function handleChange(
    value: string,
    checked: boolean,
  ) {

    const next = new Set(selected);

    if (checked) {

      next.add(value);

    } else {

      next.delete(value);

    }

    onChange(
      Array.from(next),
    );

  }

  return (

    <div
      style={{
        marginBottom: "20px",
      }}
    >

      <label
        style={{
          display: "block",
          fontWeight: 600,
          marginBottom: "8px",
        }}
      >
        {label}
        {required && " *"}
      </label>

      <div
        style={{
          border: "1px solid #dcdcdc",
          borderRadius: "8px",
          padding: "12px",
          maxHeight: "220px",
          overflowY: "auto",
        }}
      >

        {options.map((option) => (

          <label
            key={option.value}
            style={{
              display: "flex",
              alignItems: "center",
              gap: "8px",
              marginBottom: "8px",
              cursor: "pointer",
            }}
          >

            <input
              type="checkbox"
              checked={selected.has(
                option.value,
              )}
              onChange={(event) =>
                handleChange(
                  option.value,
                  event.target.checked,
                )
              }
            />

            {option.label}

          </label>

        ))}

      </div>

    </div>

  );

}